import socket
from datetime import datetime
from Security.Security import Security
from GUI import Ui_MainWindow

class TCPClient:
    ''' A simple TCP Client that uses IPv4 '''

    def __init__(self, host, port):
        self.host = host        # host address
        self.port = port        # host port
        self.conn_sock = None   # connection socket
        self.message_security = Security()

    def logging(self, msg):
        ''' Print message with current date and time '''

        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_date_time}] {msg}')

    def create_socket(self):
        ''' Create a socket that uses IPv4 and TCP '''

        self.logging('Creating connection socket ...')
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock.settimeout(100)

        self.logging('Socket created')

    def interact_with_server(self , clientMessage):
        ''' Connect and interact with a TCP Server. '''

        try:
            # connect to server
            self.logging(f'Connecting to server [{self.host}] on port [{self.port}] ...')
            self.conn_sock.connect((self.host, self.port))
        except socket.gaierror as err:
            #Except Address-related errors
            self.conn_sock.close()
            self.logging(err)
            return "Address-related Error"
        except socket.error as err:
            #Except connection errors
            self.conn_sock.close()
            self.logging(err)
            return "Connection Error"
            

        #  tring to send data
        try :
            self.logging('Sending name to server to get the questions ...')
            self.conn_sock.sendall(self.message_security.Encrypt(clientMessage))
            self.logging('[ SENT ]')
            print('\n', clientMessage, '\n')
        except socket.error as err:
            # Except Errors related to sending data
            self.logging(err)
            return "Error in sending message"

        # receive data
        try:
            resp = self.conn_sock.recv(1024)
            self.logging('[ RECEIVED ]')
            self.logging('Interaction completed successfully...')
            return self.message_security.Decrept(resp)
        except socket.error as err:
            self.logging(err)
            return "Error in recieving message"

        

        finally:
            # close socket
            self.logging('Closing connection socket...')
            self.conn_sock.close()
            self.logging('Socket closed')

