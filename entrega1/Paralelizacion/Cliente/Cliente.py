import socket
import pickle

class Client:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Cliente conectado al servidor...")

    def send_data(self, data):
        # Serializa el objeto usando pickle y envíalo al servidor
        serialized_data = pickle.dumps(data)
        self.client_socket.send(serialized_data)

    def close(self):
        self.client_socket.close()

# Crear una instancia del cliente
client = Client()

# Ejemplo de envío de datos al servidor
data_to_send = {'Fecha': '2023-08-14', 'Apertura': 100, 'Alto': 110, 'Bajo': 90, 'Cierre': 105}
client.send_data(data_to_send)

# Cierra la conexión
client.close()
