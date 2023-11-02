import time
import socket
import threading


clients = 0
clients_lock = threading.Lock()

def handle_client(client_socket, data_queue, index_market):
    
    global clients, clients_lock
    with clients_lock:
        clients += 1
    print(f"CLIENT NUMBER = {clients}")

    if clients > 9:
        print("THIS IS NOT THE FIRST CLIENT")

        with open("monedas.txt", 'r') as f_in:
            next(f_in) 
            for row in f_in:
                try:
                    index_list = row.split(',')
                    my_index = index_list[-1].strip()
                    if my_index == index_market:
                        # fecha = row[0]
                        # apertura = row[1]
                        # alto = row[2]
                        # bajo = row[3]
                        # cierre = row[4]
                        # candle = f"{fecha},{apertura},{alto},{bajo},{cierre}"
                        # print(candle)
                        client_socket.send(row.encode('utf-8'))
                        time.sleep(0.01)
                    else:
                        continue 
                    
                except Exception as e:
                    print("Ocurrió un error al enviar datos al cliente:", str(e))

 
    

    else:
        print("I AM THE FIRST CLIENT")

        while True:
            data = data_queue.get()
            if data == 'DONE':
                break
            try:
                client_socket.send(data.encode('utf-8'))
            except Exception as e:
                print("Ocurrió un error al enviar datos al cliente:", str(e))

    with clients_lock:
        clients -= 1
    client_socket.close()

        
    




def connect_to_client(host, port, data_queue, index_market, client_connected):
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Waiting for client connection {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Succesfuly connected {addr}")

        client_connected.set()
        

        client_thread = threading.Thread(target=handle_client, args=(client_socket, data_queue, index_market))
        client_thread.start()









        
   



        
   

