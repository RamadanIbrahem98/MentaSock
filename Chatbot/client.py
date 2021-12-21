# -*- coding: utf-8 -*-
import sys
import json
import socket
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from security import Security

# setting up the HOST ip & PORT number from the HOST_PORT.json file
with open('HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # attaching the gui to our client
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.message_security = Security()
        # appending a welcoming message when the program first runs
        self.ui.textBrowser.append(
            '<font color="#FF0000">' 
            'Bot :Please read each statement and circle a number 0, 1, 2 or 3 which indicates how much the statement' 
            '<br> applied to you over the past week. There are no right or wrong answers'
            ' Do not spend too muchtime on any statement <br> <br> '
            '0 Did not apply to me at all <br> <br> '
            '1 Applied to me to some degree, or some of the time <br> <br>'
            '2 Applied to me to a considerable degree or a good part of time<br> <br>'
            '3 Applied to me very much or most of the time<br> <br>'
            '<br> Bot : are you ready ?</font>')
        # setting the client port and host of the client as those inside the json file
        self.HOST = HOST_PORT['HOST']
        self.PORT = int(HOST_PORT['PORT'])
        # attaching the button click event to a connection function responsible for sending data to server
        self.ui.pushButton.clicked.connect(self.buttonEvent)
    def buttonEvent(self):
        # appending the text hte user sends through the textEdit widget to the textBrowser widget with the "you" key word preciding it
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.clear()
        self.ui.textBrowser.append('You: '+text)
        # using tcp socet connection from socket library (AF_INET means it utilizes internet connection)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connecting to the host ip and port provided by the json file
        try:
            self.client.connect((self.HOST, self.PORT))
        except socket.gaierror as err:
            self.ui.textBrowser.append(
                '<font color="#FF0000">500: Address-related Error</font>')
            self.client.close()
            return ''
        except socket.error as err:
            self.ui.textBrowser.append(
                '<font color="#FF0000">500: Connection Error</font>')
            self.client.close()

        try:
            self.client.sendall(self.message_security.Encrypt(text))
            
        
        except socket.error as err:
            self.ui.textBrowser.append('<font color="#FF0000">500: Error of Sending Message</font>')

        # Recieving server message (not more than 1024 bytes with encoding type of utf-8)
        try:
            serverMessage = (self.client.recv(1024))
            
        except socket.error as err:
            self.ui.textBrowser.append('<font color="#FF0000">500: Error of Recieving Message</font>')
        

        # appending the server response to the textBrowser widget in the GUI
        self.ui.textBrowser.append('<font color="#FF0000">Bot : '+self.message_security.Decrept(serverMessage)+'</font>')
        
        # closing the connection
        self.client.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
