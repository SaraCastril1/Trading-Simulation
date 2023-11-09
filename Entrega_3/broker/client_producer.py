import time
import socket
import linecache
import threading


clients = 0
clients_lock = threading.Lock()

# current_candle = ""
# current_threads = 0 
# barrier = threading.Barrier(current_threads)

first = False
second = False









def handle_client(client_socket, data_queue, index_market, data_in_memory):
    
    global clients, clients_lock, first, second
    

    with clients_lock:
        clients += 1
    print(f"CLIENT NUMBER = {clients}")

    if clients > 9 and first:
        print("THIS IS NOT THE FIRST CLIENT")

        
        if clients > 18 and first and second:
            print("THIS IS NOT THE FIRST/SECOND CLIENT")
            

            for data in data_in_memory:
                # print(index_market, "->", "index = ", data[1], "date = ", data[0])
                file_index = data[1]
                candle = linecache.getline("monedas.txt", file_index)
                if candle:
                    # print(index_market, "->", "index = ", data[1], "date = ", data[0], "\n", candle)
                    client_socket.send(candle.encode('utf-8'))
                    time.sleep(0.01)

                    with open("{}.txt".format(index_market), "a") as file:
                        file.write(str(data) + "\n")
                else:
                    print("THERE IS NO MORE DATA IN DATA_IN_MEMORY")
                    time.sleep(1)
                    continue
            

            # print("THERE IS NO MORE DATA IN DATA_IN_MEMORY")
            # current_threads +=1 
            # barrier = threading.Barrier(current_threads)
            # print(current_threads)

            # mutex = threading.Lock()

            # while True:
            #     # with mutex:
            #     my_candle = current_candle
            #     barrier.wait() 
            #     if my_candle == 'DONE':
            #         break
            #     try:
            #         client_socket.send(my_candle.encode('utf-8'))
            #     except Exception as e:
            #         print("Ocurrió un error al enviar datos al cliente:", str(e))
                



                
                

            

        else:
            print("I AM THE SECOND CLIENT")
            second = True
           

            
            with open("monedas.txt", 'r') as f_in:
                # next(f_in) 
                file_conuter = 1
                for row in f_in:
                    try:
                        index_list = row.split(',')
                        my_index = index_list[-1].strip()
                        if my_index == index_market:
                            candle_tup = (index_list[0].strip(), file_conuter)
                            # print(index_market, "--->", candle_tup)
                            data_in_memory.append(candle_tup)
                            client_socket.send(row.encode('utf-8'))
                            file_conuter+=1
                            time.sleep(0.01)
                        else:
                            file_conuter+=1
                        
                    except Exception as e:
                        print("Ocurrió un error al enviar datos al cliente:", str(e))

 
    

    else:

        print("I AM THE FIRST CLIENT")
        first = True
        print(clients)
        print(first)
        print(second)

        while True:
            data = data_queue.get()
            # current_candle = data
            # barrier.wait()
            if data == 'DONE':
                break
            try:
                client_socket.send(data.encode('utf-8'))
            except Exception as e:
                print("Ocurrió un error al enviar datos al cliente:", str(e))

    # with clients_lock:
    #     clients -= 1
    # client_socket.close()

        
    




def connect_to_client(host, port, data_queue, index_market, data_in_memory, client_connected):

    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Waiting for client connection {host}:{port}")


    while True:
        client_socket, addr = server_socket.accept()
        print(f"Succesfuly connected {addr}")

        client_connected.set()

    

        client_thread = threading.Thread(target=handle_client, args=(client_socket, data_queue, index_market, data_in_memory))
        client_thread.start()









        
   



        
   

