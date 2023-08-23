#LECTURA DE LAS VELAS
import socket
import pickle  # Para serializar/deserializar objetos



class Server:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 1236
        self.HEADERSIZE = 10
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Waiting for connection...")



    def receive_data(self):
        full_msg = b''
        new_msg = True

        while True:
            msg = self.client_socket.recv(16)

            if new_msg:
                msglen = int(msg[:self.HEADERSIZE].decode('utf-8'))
                new_msg = False

            full_msg += msg

            if len(full_msg)-self.HEADERSIZE == msglen:
                #print("Full message recovered: ")
                #print(full_msg[self.HEADERSIZE:])
                data = pickle.load(io.BytesIO(full_msg[self.HEADERSIZE:]))
                print(data)
                new_msg = True
                full_msg = b''


    def send_data(self, data, client_socket):
        msg = pickle.dumps(data)
        #print(msg)
        msg = bytes(f'{len(msg):<{server.HEADERSIZE}}', "utf-8")+msg

        client_socket.send(msg)



    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from  {client_address} has been established!")
            #server.send_data("Welcome to the server!", client_socket)

            
            

                
# d = {1:"hi", 2: "there"}
# msg = pickle.dumps(d)
# print(msg)


#server = Server()
#server.start()
