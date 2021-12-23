# -*- coding: utf-8 -*-
import sys
import json
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from TCPClient.TCPClient import TCPClient
from Security.Security import Security

# setting up the HOST ip & PORT number from the HOST_PORT.json file
with open('HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # attaching the gui to our client
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # appending a message when the program first runs
        self.ui.textBrowser.append(
            '<font color="#FF0000">' 
            'Bot :Please read each statement and circle a number 0, 1, 2 or 3 which indicates how much the statement' 
            '<br> applied to you over the past week. There are no right or wrong answers'
            ' Do not spend too muchtime on any statement <br> <br> '
            '0 Did not apply to me at all <br> <br> '
            '1 Applied to me to some degree, or some of the time <br> <br>'
            '2 Applied to me to a considerable degree or a good part of time<br> <br>'
            '3 Applied to me very much or most of the time<br> <br>'
            '<br> Bot : are you ready ? yes/no</font>')
        # setting the client port and host of the client as those inside the json file
        self.HOST = HOST_PORT['HOST']
        self.PORT = int(HOST_PORT['PORT'])
        #creat client tcp connectin
        self.client = TCPClient(self.HOST,self.PORT)
        # attaching the button click event to a connection function responsible for sending data to server
        self.ui.pushButton.setDisabled(True)
        self.ui.textEdit.textChanged.connect(self.setButtton)

        self.ui.pushButton.clicked.connect(self.buttonEvent)
    def setButtton(self):
        if len(self.ui.textEdit.toPlainText()) > 0:
            self.ui.pushButton.setDisabled(False)
        else : self.ui.pushButton.setDisabled(True)
    #actint taken after button cliked 
    def buttonEvent(self):
        # sotore the uese message in text variable 
        text = self.ui.textEdit.toPlainText()


        #clear the text after storage it in variable 
        self.ui.textEdit.clear()

        #appending the user message with you int textBrowser widget
        self.ui.textBrowser.append('You: '+text)
        #cerate sockt connection 
        self.client.create_socket()
        #get the server meassge 
        serverMessage = self.client.interact_with_server(text)
        #retrieve the message from server to textBrowser widget
        self.ui.textBrowser.append(
            '<font color="#FF0000">Bot : '+serverMessage+'</font>')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    #show the window of GUI
    window.show()
    sys.exit(app.exec_())
