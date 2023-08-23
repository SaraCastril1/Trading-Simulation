#VISUALIZACION DE LAS VELAS

import socket
import pickle
import io
from datetime import datetime, timedelta
from Chart import Chart


class Visualizer:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.HEADERSIZE = 10
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        #print("Succesfully connected to the server...")


    

    def receive_data(self):
        chart = Chart()
        
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
                #print(data)
                chart.data.extend(data)
                print("Data: ")
                print(data)
                print("Chart.data: ")
                print(chart.data)
                data.clear()
                print("Data: ")
                print(data)
            
                new_msg = True
                full_msg = b''

            chart.graficar_velas_chinas()
                #self.client_socket.close()
                #chart.data.clear()
                


        


            

    def close(self):
        self.client_socket.close()

def main():
    # Crear una instancia del cliente
    visualizer = Visualizer()
    #chart = Chart()
    visualizer.receive_data()




    #visualizer.close()

if __name__ == "__main__":
    main()
