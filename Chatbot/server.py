# -*- coding: utf-8 -*-
import json
import socket
import re
import Responses as resp


# the words we want the bot to recognize will be the "recognized_words"
def message_probability(user_message, recoginzed_words, single_response=False,required_words=[]):
    message_certainty = 0
    has_required_words = True

    # checking if the user message has a word that is in the recognized word array (which we provide)
    # if so it will increment the messsage certainity by 1 (the sentence is more accurate)
    for word in user_message:
        if word in recoginzed_words:
            message_certainty +=1

    # percentage of sentence accuracy
    # depending on hoe many of the words we wont the bot to recognize in the user message 
    percentage = float(message_certainty)/float(len(recoginzed_words))

    # check if no required or key word is in the user_message if so we set the has_required_words to false
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # returns the sentance accuracy to return the best possible response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    # a dectionary to contain high prob messages
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dictionary
    # bot_response is what the bot will say to the user
    # list_of_words is there to act as a look up table for the bot
    # required words must be insde user message to get the corressponding bot response
    #
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('This patient might have Arrithmia',['slow','fast','shortness','fluttering','ECG','ecg'],required_words=['heart','rate'])
    response('Thank you!', ['thanks', 'thanks alot', 'much appreciated'], required_words=['thanks', 'thank you', 'appreciated'])
    response('The patients musle health is deteriorating (a sign of musclar dystrophy)',['EMG','emg','disability','falls','stiffness'],single_response=True)
    response('The patients musle health is Optimal (a sign of musclar dystrophy)',['EMG','emg'],required_words=['regular','normal'])
    response('This patient doesnt have Arrithmia',['normal','ECG','ecg'],required_words=['normal','regular'])

    # Advice responses
    response(resp.R_ADVICE, ['give', 'advice'], required_words=['advice'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return resp.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    # split the message into an array to analyze each word of it sepretly
    split_message = re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    # sends the splitted array to a function that checks all the words and see if we have a designated response for it
    response = check_all_messages(split_message)
    return response



# HOST & PORT
with open('HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)

HOST = HOST_PORT['HOST']
PORT = int(HOST_PORT['PORT'])

# using tcp socet connection from socket library (AF_INET means it utilizes internet connection)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding the server to the host ip and port number from the json file
server.bind((HOST, PORT))
# marking our socket to be a passive socket ( it will accept incoming connection requests ). the server can listen to up to 5 clients
server.listen(5)


while True:
    # accepting the client handshake
    conn, addr = server.accept()
    # recieving the client message with a limit of 1024 bytes max
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    # a print statement to check the client recieved message
    print('Client message is:', clientMessage)
    # Repeat

    #setting server time out to 100 seconds of inactivity
    server.settimeout(100)
    # keywords = ['cancer', 'hepatitis' , 'cold', 'flu','headaches', 'arrhythmia']
    # responses = ['Patient might have the disease', 'Patient doesnt have the disease']
    # for i in range(len(keywords)):
    #     if keywords[i] in clientMessage:
    #             serverMessage = random.choice(responses) + keywords[i]
    #     else:
    #             serverMessage = clientMessage

    serverMessage = get_response(clientMessage)
    

    conn.sendall(serverMessage.encode())
    # close connection after sending the response
    conn.close()
