import socket
import threading
import time
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import argparse
from collections import deque

buffer = 2048
# Data storage
dictionary = None

# Variables
fields = ["Open", "High", "Low", "Close"]
tcurrency = ['BRENTCMDUSD', 'BTCUSD', 'EURUSD', 'GBPUSD', 'USA30IDXUSD', 'USA500IDXUSD', 'USATECHIDXUSD', 'XAGUSD', 'XAUUSD',]
mc = mpf.make_marketcolors(up='g', down='r')
colors = mpf.make_mpf_style(marketcolors=mc)
pkwargs = dict(type='candle', mav=(5, 13), style=colors)
thread_count = 0

main_fig, main_axes = plt.subplots(3, 3)
plt.ion()

# Conditions
data_condition = threading.Condition()
lock = threading.Lock()

def trading(currency, positionx, positiony):
    global dictionary, main_axes, main_fig

    content = {"Open": [], "High": [], "Low": [], "Close": []}
    date = []
    df = None

    while True:
        with data_condition:
            data_condition.wait()

        if currency in dictionary:
            data = dictionary[currency]
            if data is not None:  # Verifica que data no sea None
                date.append(data['Date'])
                for key in fields:
                    content[key].append(data[key])

                df = pd.DataFrame(content, index=date)
                df.index.name = 'Date'
                df.index = pd.to_datetime(df.index)

                lock.acquire()
                mpf.plot(df, **pkwargs, axtitle=f"{currency}", ax=main_axes[positionx, positiony])
                plt.draw()
                lock.release()
        else:
            continue


# def trading(currency, positionx, positiony):
#     global dictionary, main_axes, main_fig

#     # Usar una cola con longitud máxima de 20 para almacenar los últimos 20 datos
#     data_queue = deque(maxlen=20)

#     while True:
#         with data_condition:
#             data_condition.wait()

#         if currency in dictionary:
#             data = dictionary[currency]
#             if data is not None:
#                 data_queue.append(data)  # Agrega el nuevo dato a la cola

#                 # Verifica si la cola contiene 20 datos antes de generar el gráfico
#                 if len(data_queue) == 20:
#                     content = {key: [] for key in fields + ['Date']}

#                     for data_item in data_queue:
#                         for key in fields + ['Date']:
#                             content[key].append(data_item[key])

#                     df = pd.DataFrame(content)
#                     df.set_index('Date', inplace=True)
#                     df.index = pd.to_datetime(df.index)

#                     lock.acquire()
#                     main_axes[positionx, positiony].clear()
#                     mpf.plot(df, **pkwargs, axtitle=f"{currency}", ax=main_axes[positionx, positiony])
#                     plt.draw()
#                     lock.release()
#         else:
#             continue

# def trading(currency, positionx, positiony):
#     global dictionary, main_axes, main_fig

#     content = {"Open": [], "High": [], "Low": [], "Close": []}
#     date = []
#     df = None

#     data_counter = 0  # Contador para controlar los datos a mostrar

#     while True:
#         with data_condition:
#             data_condition.wait()

#         if currency in dictionary:
#             data = dictionary[currency]
#             if data is not None:  # Verifica que data no sea None
#                 date.append(data['Date'])
#                 for key in fields:
#                     content[key].append(data[key])

#                 df = pd.DataFrame(content, index=date)
#                 df.index.name = 'Date'
#                 df.index = pd.to_datetime(df.index)

#                 # Limita el rango de datos mostrados en el gráfico
#                 if len(df) > 20:
#                     df = df[-20:]  # Selecciona solo los últimos 20 datos

#                 lock.acquire()
#                 mpf.plot(df, **pkwargs, axtitle=f"{currency}", ax=main_axes[positionx, positiony])
#                 plt.draw()
#                 lock.release()
#         else:
#             continue

def receive_candle(host, port, currency):
    global dictionary

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(buffer).decode('utf-8')
        if not data:
            break
        # Procesa datos CSV
        rows = data.split('\n')
        for row in rows:
            if row:
                values = row.split(',')
                if len(values) == 6:  # Asegura que hay al menos 5 columnas: Date, Open, High, Low, Close
                    date, open_price, high, low, close = values[:5]  # Ignora la última columna si hay más de 5
                    dictionary[currency] = {
                        "Date": date,
                        "Open": float(open_price),
                        "High": float(high),
                        "Low": float(low),
                        "Close": float(close)
                    }

    client_socket.close()
    
def main(markets_to_monitor):
    global dictionary

    # Configura el cliente
    host = '127.0.0.1'
    ports = [6000, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007]

    if not markets_to_monitor:
        markets_to_monitor = ['BRENTCMDUSD', 'BTCUSD', 'EURUSD', 'GBPUSD', 'USA30IDXUSD', 'USA500IDXUSD', 'USATECHIDXUSD', 'XAGUSD', 'XAUUSD']

    dictionary = {currency: None for currency in markets_to_monitor}

    threads = []

    for i, port in enumerate(ports):
        currency = tcurrency[i]
        if currency in markets_to_monitor:
            thread = threading.Thread(target=receive_candle, args=(host, port, currency))
            threads.append(thread)
            thread.start()

    # Gráficos solo para los mercados seleccionados
    trading_threads = []
    for i, currency in enumerate(markets_to_monitor):
        if i < 9:  # Limitar el número de hilos a 9
            trading_threads.append(threading.Thread(target=trading, args=(currency, i // 3, i % 3)))

    for thread in trading_threads:
        thread.start()

    while True:
        plt.pause(0.0001)
        plt.tight_layout()
        plt.show()

        with data_condition:
            data_condition.notify_all()
            time.sleep(0.001)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Market Client')
    parser.add_argument('-m', '--markets', nargs='*', choices=['BRENTCMDUSD', 'BTCUSD', 'EURUSD', 'GBPUSD', 'USA30IDXUSD', 'USA500IDXUSD', 'USATECHIDXUSD', 'XAGUSD', 'XAUUSD'],
                        default=['BRENTCMDUSD', 'BTCUSD', 'EURUSD', 'GBPUSD', 'USA30IDXUSD', 'USA500IDXUSD', 'USATECHIDXUSD', 'XAGUSD', 'XAUUSD'],
                        help='Choose which markets to monitor')

    args = parser.parse_args()
    markets_to_monitor = args.markets

    main(markets_to_monitor)