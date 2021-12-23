# -*- coding: utf-8 -*-
import json
import socket
from GUI import Ui_MainWindow
import io
import pyAesCrypt
from src.Security.Security import Security
from responce import Responce
message_security = Security()
client_responce = Responce()
ui = Ui_MainWindow()
# HOST & PORT
with open('HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)

HOST = HOST_PORT['HOST']
PORT = int(HOST_PORT['PORT'])

# using tcp socet connection from socket library (AF_INET means it utilizes internet connection)
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    ui.textBrowser.append('<font color="#FF0000">500: Error of Creating socket</font>')


# binding the server to the host ip and port number from the json file
try:
    server.bind((HOST, PORT))
except socket.gaierror as err:
    ui.textBrowser.append('<font color="#FF0000">500: Address-related Error</font>')
    server.close()
except socket.error as err:
    ui.textBrowser.append('<font color="#FF0000">500: Connection Error</font>')
    server.close()


# marking our socket to be a passive socket ( it will accept incoming connection requests ). the server can listen to up to 5 clients
server.listen(5)


while True:
    
    # accepting the client handshake
    conn, addr = server.accept()
    # recieving the client message with a limit of 1024 bytes max
    try:
        clientMessage = (conn.recv(1024))
    except socket.error as err:
        ui.textBrowser.append('<font color="#FF0000">500: Error of Recieving Message</font>')


	
	

    # a print statement to check the client recieved message
    #print('Client message is:', clientMessage)
    # Repeat

    # setting server time out to 100 seconds of inactivity
    server.settimeout(100)


    
    

    serverMessage = client_responce.get_response(message_security.Decrept(clientMessage))
    
    
    try:
        conn.sendall(message_security.Encrypt(serverMessage))
    except socket.error as err:
        ui.textBrowser.append('<font color="#FF0000">500: Error of Sending Message</font>')
    # close connection after sending the response
    finally: conn.close()
