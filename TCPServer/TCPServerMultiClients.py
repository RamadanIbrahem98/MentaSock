import socket
import threading
from datetime import datetime
from TCPServer import TCPServer
import json


with open('../HOST_PORT.json', 'r', encoding='utf-8') as f:
    HOST_PORT = json.load(f)

class TCPServerMultiClient(TCPServer):
    def __init__(self, host, port, max_connections):
        super().__init__(host, port)
        self.max_connections = max_connections

    def wait_for_client(self):
        ''' Wait for clients to connect '''
        self.logging('Listening for incoming connection')
        # 10 clients before server refuses connections
        self.sock.listen(self.max_connections)

        while True:
            try:
                client_sock, client_address = self.sock.accept()
                self.logging(f'Accepted connection from {client_address}')
                c_thread = threading.Thread(target=self.handle_client,
                                            args=(client_sock, client_address))
                c_thread.start()
            except KeyboardInterrupt:
                self.logging('Server stopped by user')
                self.shutdown_server()
                break


def main():
    ''' Create a TCP Server and handle multiple clients simultaneously '''

    tcp_server_multi_client = TCPServerMultiClient(HOST_PORT["HOST"], HOST_PORT["PORT"], 10)
    tcp_server_multi_client.configure_server()
    tcp_server_multi_client.wait_for_client()


if __name__ == '__main__':
    main()
