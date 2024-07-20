import threading
import socket
from config_read import read_config


class Proxy():
    def __init__(self):
        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port   
        self.serverSocket.bind((read_config['proxy']['HOST'], read_config['proxy']['PORT']))
        
        self.serverSocket.listen(10) # become a server socket
        self.__clients = {}

    def run(self):
        while True:
            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept() 
            
            d = threading.Thread(name=self._getClientName(client_address), 
            target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()