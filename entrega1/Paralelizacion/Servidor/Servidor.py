import socket
import pickle  # Para serializar/deserializar objetos

class Server:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print("Servidor listo para recibir conexiones...")

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Conexión aceptada de {client_address}")
            
            ## Recibir los datos enviados por el cliente
            serialized_data = client_socket.recv(1024)  # Tamaño del buffer
            data = pickle.loads(serialized_data)
            
            # Imprimir los datos recibidos
            print("Datos recibidos del cliente:", data)
            
            client_socket.close()

server = Server()
server.start()
