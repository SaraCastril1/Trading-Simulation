import socket
import threading
import time
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

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

def receive_candle(host, port, currency):
    global dictionary

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(buffer).decode('utf-8')
        print(data)
        # print(data)
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
    
def main():
    global dictionary

    # Configura el cliente
    host = '127.0.0.1'
    ports = [6000, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007]

    dictionary = {currency: None for currency in tcurrency}

    threads = []

    for i, port in enumerate(ports):
        currency = tcurrency[i]
        thread = threading.Thread(target=receive_candle, args=(host, port, currency))
        threads.append(thread)
        thread.start()

    trading_threads = [threading.Thread(target=trading, args=(currency, i // 3, i % 3)) for i, currency in enumerate(tcurrency)]

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
    main()


