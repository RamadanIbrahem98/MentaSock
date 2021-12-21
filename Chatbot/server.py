# -*- coding: utf-8 -*-
import json
import socket
import re
from responce import Responce

client_responce = Responce()

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
    

    serverMessage = client_responce.get_response(clientMessage)
    

    conn.sendall(serverMessage.encode())
    # close connection after sending the response
    conn.close()
