import socket
import csv
import time
from datetime import datetime

def enviar_velas(client_socket, server_socket, archivo_entrada):
    try:
        with open(archivo_entrada, 'r') as f_in:
            reader = csv.reader(f_in)
            #next(reader)  

            for row in reader:
                fecha = None
                try:
                    fecha = datetime.strptime(row[0], "%Y-%m-%d %H:%M")
                    apertura = float(row[1])
                    alto = float(row[2])
                    bajo = float(row[3])
                    cierre = float(row[4])

                    # Envía los datos de la vela al cliente
                    mensaje = f"{fecha},{apertura},{alto},{bajo},{cierre},m8\n"
                    client_socket.send(mensaje.encode('utf-8'))
                    time.sleep(0.01)  
            
                except Exception as e:
                    print("Ocurrió un error al procesar una fila:", str(e))

            
    except FileNotFoundError:
        print("No se encontró el archivo de entrada en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", str(e))

    print("LLEGUÉ AL FINAL DE EL ARCHIVO")
    f_in.flush()
    client_socket.close()
    server_socket.close()



def main():
    # Configura el servidor
    host = '127.0.0.1'
    port = 8500

    # Crea un socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    # Espera a que un cliente se conecte
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    # Recibe la ruta del cliente
    ruta = client_socket.recv(1024).decode('utf-8')
    print(f"Ruta recibida: {ruta}")

    # Envía las velas al cliente
    enviar_velas(client_socket, server_socket, ruta)

    

    # Comunicación con el cliente
    # while True:
    #     data = client_socket.recv(1024).decode('utf-8')
    #     if not data:
    #         break
    #     print(f"Mensaje recivido: {data}")

    #     #Respuesta al cliente ---------------------------------------------------------
    #     message = input("Respuesta al cliente: ")
    #     client_socket.send(message.encode('utf-8'))


if __name__ == "__main__":
    main()
