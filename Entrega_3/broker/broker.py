from market_consume import connect_to_market
from client_producer import connect_to_client
from queue import Queue
import threading
import sys
import os

# DATA IN MEMORY
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
m6 = []
m7 = []
m8 = []
m9 = []


    # Mercado 1 = BRENTCMDUSD
    # Mercado 2 = BTCUSD
    # Mercado 3 = EURUSD
    # Mercado 4 = GBPUSD
    # Mercado 5 = USA30IDXUSD
    # Mercado 6 = USA500IDXUSD
    # Mercado 7 = USATECHIDXUSD
    # Mercado 8 = XAGUSD
    # Mercado 9 = XAUUSD

data_queue1 = Queue()
data_queue2 = Queue()
data_queue3 = Queue()
data_queue4 = Queue()
data_queue5 = Queue()
data_queue6 = Queue()
data_queue7 = Queue()
data_queue8 = Queue()
data_queue9 = Queue()

client_connected = threading.Event()

def debug_print(market):
    print("{}****************************************************************".format(market))
    with open("data_in_memory.txt", "a") as file:
        for data in market:
            file.write(data + "\n")



def main():
    # global data_queue
    #EXCHANGES
    market_host = '127.0.0.1'
    market_port1 = 12345
    market_port2 = 50051
    market_port3 = 8080
    market_port4 = 7000
    market_port5 = 9000
    market_port6 = 9500
    market_port7 = 7500
    market_port8 = 8500
    market_port9 = 8443
    
    #QUEUES
    client_host = '127.0.0.1'
    client_port1 = 6000
    client_port2 = 5000
    client_port3 = 5001
    client_port4 = 5002
    client_port5 = 5003
    client_port6 = 5004
    client_port7 = 5005
    client_port8 = 5006
    client_port9 = 5007



    # RECIBE VALORES POR LA TERMINAL ------------------------------------------------------
    parsed_args = {"-p": None}    

    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            # elif arg.startswith("-m="):
            #     parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        # print("Moneda:", parsed_args["-m"])

    else:
        print("Se necesitan al menos 1 argumento.")
        print("D1, H1, H4, M1, M5, M15, M30")
        return(1)

    
    # nombre_archivo = f"{parsed_args['-m']}_{parsed_args['-p']}.csv"
    # ruta = os.path.join('./MonedasCSV', nombre_archivo)
    # print("Ruta: ",ruta)

    name1 = f"BRENTCMDUSD_{parsed_args['-p']}.csv"
    name2 = f"BTCUSD_{parsed_args['-p']}.csv"
    name3 = f"EURUSD_{parsed_args['-p']}.csv"
    name4 = f"GBPUSD_{parsed_args['-p']}.csv"
    name5 = f"USA30IDXUSD_{parsed_args['-p']}.csv"
    name6 = f"USA500IDXUSD_{parsed_args['-p']}.csv"
    name7 = f"USATECHIDXUSD_{parsed_args['-p']}.csv"
    name8 = f"XAGUSD_{parsed_args['-p']}.csv"
    name9 = f"XAUUSD_{parsed_args['-p']}.csv"


    ruta1 = os.path.join('./MonedasCSV', name1)
    ruta2 = os.path.join('./MonedasCSV', name2)
    ruta3 = os.path.join('./MonedasCSV', name3)
    ruta4 = os.path.join('./MonedasCSV', name4)
    ruta5 = os.path.join('./MonedasCSV', name5)
    ruta6 = os.path.join('./MonedasCSV', name6)
    ruta7 = os.path.join('./MonedasCSV', name7)
    ruta8 = os.path.join('./MonedasCSV', name8)
    ruta9 = os.path.join('./MonedasCSV', name9)

    print("RUTAS:")
    print(name1)
    print(name2)
    print(name3)
    print(name4)
    print(name5)
    print(name6)
    print(name7)
    print(name8)
    print(name9)
    


    # Activar hilo de el mercado BRENTCMDUSD
    consume_market_thread1 = threading.Thread(target=connect_to_market, args=(market_host, market_port1, ruta1, data_queue1, client_connected,))
    consume_market_thread1.start()

    # Activar hilo de el mercado BTCUSD
    consume_market_thread2 = threading.Thread(target=connect_to_market, args=(market_host, market_port2, ruta2, data_queue2, client_connected,))
    consume_market_thread2.start() 


    # Activar hilo de el mercado EURUSD
    consume_market_thread3 = threading.Thread(target=connect_to_market, args=(market_host, market_port3, ruta3, data_queue3, client_connected,))
    consume_market_thread3.start() 

    # Activar hilo de el mercado GBPUSD
    consume_market_thread4 = threading.Thread(target=connect_to_market, args=(market_host, market_port4, ruta4, data_queue4, client_connected,))
    consume_market_thread4.start() 

    # Activar hilo de el mercado USA30IDXUSD
    consume_market_thread5 = threading.Thread(target=connect_to_market, args=(market_host, market_port5, ruta5, data_queue5, client_connected,))
    consume_market_thread5.start() 

    # Activar hilo de el mercado USA500IDXUSD
    consume_market_thread6 = threading.Thread(target=connect_to_market, args=(market_host, market_port6, ruta6, data_queue6, client_connected,))
    consume_market_thread6.start() 

    # Activar hilo de el mercado USATECHIDXUSD
    consume_market_thread7 = threading.Thread(target=connect_to_market, args=(market_host, market_port7, ruta7, data_queue7, client_connected,))
    consume_market_thread7.start() 

    # Activar hilo de el mercado XAGUSD
    consume_market_thread8 = threading.Thread(target=connect_to_market, args=(market_host, market_port8, ruta8, data_queue8, client_connected,))
    consume_market_thread8.start() 

    # Activar hilo de el mercado XAUUSD
    consume_market_thread9 = threading.Thread(target=connect_to_market, args=(market_host, market_port9, ruta9, data_queue9, client_connected,))
    consume_market_thread9.start() 

    

    








    # Activar hilo del cliente BRENTCMDUSD
    producer_client_thread1 = threading.Thread(target=connect_to_client, args=(client_host, client_port1, data_queue1, "m1", m1, client_connected ))
    producer_client_thread1.start()

    # Activar hilo del cliente BTCUSD
    producer_client_thread2 = threading.Thread(target=connect_to_client, args=(client_host, client_port2, data_queue2, "m2", m2, client_connected ))
    producer_client_thread2.start()

    # Activar hilo del cliente EURUSD
    producer_client_thread3 = threading.Thread(target=connect_to_client, args=(client_host, client_port3, data_queue3, "m3", m3, client_connected ))
    producer_client_thread3.start()

    # Activar hilo del cliente GBPUSD
    producer_client_thread4 = threading.Thread(target=connect_to_client, args=(client_host, client_port4, data_queue4, "m4", m4, client_connected))
    producer_client_thread4.start()

    # Activar hilo del cliente USA30IDXUSD
    producer_client_thread5 = threading.Thread(target=connect_to_client, args=(client_host, client_port5, data_queue5, "m5", m5, client_connected))
    producer_client_thread5.start()

    # Activar hilo del cliente USA500IDXUSD
    producer_client_thread6 = threading.Thread(target=connect_to_client, args=(client_host, client_port6, data_queue6, "m6", m6, client_connected))
    producer_client_thread6.start()

    # Activar hilo del cliente USATECHIDXUSD
    producer_client_thread7 = threading.Thread(target=connect_to_client, args=(client_host, client_port7, data_queue7, "m7", m7, client_connected))
    producer_client_thread7.start()

    # Activar hilo del cliente XAGUSD
    producer_client_thread8 = threading.Thread(target=connect_to_client, args=(client_host, client_port8, data_queue8, "m8", m8, client_connected))
    producer_client_thread8.start()

    # Activar hilo del cliente XAUUSD
    producer_client_thread9 = threading.Thread(target=connect_to_client, args=(client_host, client_port9, data_queue9, "m9", m9, client_connected))
    producer_client_thread9.start()


    # FINALMENTE ------------------------------------------------------------------------
    consume_market_thread1.join()
    consume_market_thread2.join()
    consume_market_thread3.join()
    consume_market_thread4.join()
    consume_market_thread5.join()
    consume_market_thread6.join()
    consume_market_thread7.join()
    consume_market_thread8.join()
    consume_market_thread9.join()
    producer_client_thread1.join()
    producer_client_thread2.join()
    producer_client_thread3.join()
    producer_client_thread4.join()
    producer_client_thread5.join()
    producer_client_thread6.join()
    producer_client_thread7.join()
    producer_client_thread8.join()
    producer_client_thread9.join()


    # print("m1****************************************************************")
    # with open("data_in_memory.txt", "a") as file:
    #     for data in m1:
    #         file.write(data + "\n")

    # debug_print(m1)









if __name__ == "__main__":
    main()
