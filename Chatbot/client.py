# -*- coding: utf-8 -*-
import sys
import json
import socket
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow


# setting up the HOST ip & PORT number from the HOST_PORT.json file
with open('HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # attaching the gui to our client
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # appending a welcoming message when the program first runs
        self.ui.textBrowser.append(
            '<font color="#FF0000">Bot : I am ready for your Questions doctor. Go ahead ask me any thing You want</font>')
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
        except ConnectionRefusedError as e:
            self.ui.textBrowser.append(
                '<font color="#FF0000">500: Internal Server Error</font>')
            self.client.close()
            return ''
        # sending the encoded user message
        self.client.sendall(text.encode())

        # Recieving server message (not more than 1024 bytes with encoding type of utf-8)
        serverMessage = str(self.client.recv(1024), encoding='utf-8')
        # appending the server response to the textBrowser widget in the GUI
        self.ui.textBrowser.append(
            '<font color="#FF0000">Bot : '+serverMessage+'</font>')
        # closing the connection
        self.client.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
