from datetime import datetime
import socket
from . import Response
import os
from dotenv import load_dotenv
from Security.Security import Security

load_dotenv(dotenv_path=os.path.dirname(__file__)+'../.SECRETS.env')

host = os.getenv("HOST")
port = os.getenv("PORT")

HOST_PORT = {'HOST': host, 'PORT': port}

class TCPServer(Response.Response):
    '''
    A Simple TCP Server that handles one client at a time
    '''

    def __init__(self, host=HOST_PORT['HOST'], port=HOST_PORT['PORT']):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = None
        # Delete this line after implementing the TCP server
        self.logging('Initializing the TCP Server')

    def logging(self, msg):
        ''' Print message with current date and time '''

        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_date_time}] {msg}')

    def configure_server(self):
        '''
        TODO: Configure the TCP serve
        '''
        # create TCP socket with IPv4 addressing
        self.logging('Creating socket...')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(100)

        self.logging('Socket created')

        # bind server to the address
        self.logging(f'Binding server to {self.host}:{self.port}...')
        self.sock.bind((self.host, self.port))
        self.logging(f'Server binded to {self.host}:{self.port}')

    def wait_for_client(self):
        ''' Wait for a client to connect '''

        # start listening for incoming connections
        self.logging('Listening for incoming connection...')
        self.sock.listen(1)


        # accept a connection
        client_sock, client_address = self.sock.accept()
        self.logging(f'Accepted connection from {client_address}')
        self.handle_client(client_sock, client_address)

    def handle_client(self, client_sock, client_address):
        """ Handle the accepted client's requests """

        try:
            data_enc = client_sock.recv(1024)
            while data_enc:
                # client's request
                name = data_enc.decode()

                # resp = 'Hello From Server'
                resp = self.get_response(name)
                print(resp)
                self.logging(f'[ REQUEST from {client_address} ]')
                print('\n', name, '\n')

                # send response
                self.logging(f'[ RESPONSE to {client_address} ]')
                client_sock.sendall(resp.encode('utf-8'))
                print('\n', resp, '\n')

                # get more data and check if client closed the connection
                data_enc = client_sock.recv(1024)
            self.logging(f'Connection closed by {client_address}')

        except OSError as err:
            self.logging(err)
        except socket.error as err:
            self.logging(err)

        finally:
            self.logging(f'Closing client socket for {client_address}...')
            client_sock.close()
            self.logging(f'Client socket closed for {client_address}')

    def shutdown_server(self):
        ''' Shutdown the server '''

        self.logging('Shutting down server...')
        self.sock.close()
