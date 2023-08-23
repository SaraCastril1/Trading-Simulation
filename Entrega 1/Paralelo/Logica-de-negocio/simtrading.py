import sys
import os
import gc
import time
import io
from Scanner import Scanner
import socket
import pickle  # Para serializar/deserializar objetos

HEADERSIZE = 10
    
#def receive_data(self):
        # full_msg = b''
        # new_msg = True

        # while True:
        #     msg = self.client_socket.recv(16)

        #     if new_msg:
        #         msglen = int(msg[:HEADERSIZE].decode('utf-8'))
        #         new_msg = False

        #     full_msg += msg

        #     if len(full_msg)-self.HEADERSIZE == msglen:
        #         #print("Full message recovered: ")
        #         #print(full_msg[self.HEADERSIZE:])
        #         data = pickle.load(io.BytesIO(full_msg[self.HEADERSIZE:]))
        #         print(data)
        #         new_msg = True
        #         full_msg = b''


def send_data(data, client_socket):
    msg = pickle.dumps(data)
    #print(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+msg

    client_socket.send(msg)




def main():
    # sys.argv[0] es el nombre del script en sí mismo, los argumentos comienzan desde sys.argv[1]
    parsed_args = {"-p": None, "-f": None, "-m": None}    

    if len(sys.argv) > 3:
        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            elif arg.startswith("-f="):
                parsed_args["-f"] = arg.split("=")[1]
            elif arg.startswith("-m="):
                parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        print("Formato:", parsed_args["-f"])
        print("Moneda:", parsed_args["-m"])

    else:
        print("Se necesitan al menos 3 argumentos.")
        return(1)
    

#SERVER----------------------------------------------------------------
    host = '127.0.0.1'
    port = 1236
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Waiting for connection...")

    while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from  {client_address} has been established!")

    #SCANNER--------------------------------------------------------------        

            scanner = Scanner()
            nombre_archivo = ruta = f"{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"

            if parsed_args["-f"] == "CSV":
                #ModedasCSV\BRENTCMDUSD_H1.csv
                #ruta = f".\MonedasCSV\{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
                ruta = os.path.join('.\MonedasCSV', nombre_archivo)
                print("Ruta: ",ruta)
            
                # while True:
                #     send_data(scanner.leer_csv(ruta), client_socket)
                #     time.sleep(0.5)
                #client_socket.close()
                send_data(ruta, client_socket)
                send_data(scanner.leer_csv(ruta), client_socket)
                time.sleep(0.5)
                send_data(scanner.leer_csv(ruta), client_socket)
                time.sleep(0.5)
                #send_data(scanner.leer_csv(ruta), client_socket)
                
                
                            
                

            elif parsed_args["-f"] == "JSON":
                #ruta = f"./MonedasJSON/{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
                ruta = os.path.join('.\MonedasJSON', nombre_archivo)
                print("Ruta: ",ruta)
                #scanner.leer_json(ruta)

            else:
                print("Formato de archivo NO valido.")
                return(1)

            # del scanner    # Liberar manualmente el objeto lector
            # gc.collect()  # Invocar al recolector de basura
            # print("Se ha eliminado el scanner csv de la memoria")



    
if __name__ == "__main__":
    main()

