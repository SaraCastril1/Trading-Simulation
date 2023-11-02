import threading
from queue import Queue
import socket
import time



data_list = []
data_available = threading.Condition()


# lOCK para proteger el acceso al archivo
file_lock = threading.Lock()

# Cuando un hilo entra en el bloque with data_available, 
# adquiere el bloqueo asociado con el objeto de condición data_available. 
# Esto significa que el hilo obtiene el control exclusivo sobre la condición y 
# bloquea otros hilos que intenten acceder a ella.

def write_data_to_file(filename, client_connected):
    global data_list, data_available, file_lock
    
    while True:
        # Espera a que un cliente se conecte antes de continuar
        client_connected.wait() 
        with data_available:
            data_available.wait_for(lambda: len(data_list) > 0)

            data = data_list.pop(0)
            if data == 'DONE':
                break
            
            with file_lock:
                with open(filename, 'a') as monedas_file:
                    monedas_file.write(data)



def debug_data_queue(data_queue):
    while True:
        print("Data Queue Contents:")
        with data_queue.mutex:
            for item in data_queue.queue:
                print(item)
        print("*************************")
        time.sleep(10)




def connect_to_market(host, port, ruta, data_queue, client_connected):
    global  data_list, data_available

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(ruta.encode('utf-8'))

    write_thread = threading.Thread(target=write_data_to_file, args=('monedas.txt', client_connected,))
    write_thread.start() 

    # debug_thread = threading.Thread(target=debug_data_queue, args=(data_queue,))
    # debug_thread.start() 

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        data_queue.put(data)
        
        with data_available:
            data_list.append(data)
            data_available.notify()

    data_queue.put('DONE')
    write_thread.join()

    # Vaciar la cola antes de finalizar
    #data_queue.join()

    client_socket.close()
