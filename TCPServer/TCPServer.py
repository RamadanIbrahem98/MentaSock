from datetime import datetime


class TCPServer():
    '''
    A Simple TCP Server that handles one client at a time
    '''

    def __init__(self, host='127.0.0.1', port=8080):
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
