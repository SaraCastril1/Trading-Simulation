import pika
import os
import json
#import time
from dotenv import load_dotenv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from mplfinance.original_flavor import candlestick_ohlc
import datetime
import numpy as np

#Variables GLOBALES para el CHART -----------------------------------------------
data = []
fig, ax = plt.subplots()
index = 0

# CHART ---------------------------------------------------

def animate(i):
    global data, fig, ax, index
    #plt.ion()
    if index < len(data):
        ax.clear()
        segmento_data = data[:index+1]
        if len(segmento_data) >= 20:  # Si hay 20 datos
            del segmento_data[0] 
            del data[0]
        else:
            pass
        
        fechas = [item['Fecha'] if isinstance(item['Fecha'], datetime.datetime) else datetime.datetime.strptime(item['Fecha'], '%Y-%m-%d %H:%M:%S') for item in segmento_data]
        fechas_num = mdates.date2num(fechas)
        quotes = [(fechas_num[i], float(item['Apertura']), float(item['Alto']), float(item['Bajo']), float(item['Cierre'])) for i, item in enumerate(segmento_data)]
        
        # Calculate the SMA of 5 and 13 periods
        cierres = [float(item['Cierre']) for item in segmento_data]
        sma5 = np.convolve(cierres, np.ones(5)/5, mode='valid')
        sma13 = np.convolve(cierres, np.ones(13)/13, mode='valid')
        
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
        plt.xticks(rotation=45)
        
        candlestick_ohlc(ax, quotes, width=0.01, colorup='g', colordown='r')
        
        # Plot the SMA
        if index >= 4:  # Only plot the 5-period SMA if there are at least 5 data points
            ax.plot(fechas_num[4:index+1], sma5, label='SMA 5', color='blue')
            # Show the legend
            ax.legend()
        if index >= 12:  # Only plot the 13-period SMA if there are at least 13 data points
            ax.plot(fechas_num[12:index+1], sma13, label='SMA 13', color='orange')
            # Show the legend
            ax.legend()
        
        
        index += 1


def graficar_velas_japonesas():
    global data, fig, ax
    try:
        ani = FuncAnimation(fig, animate, interval=1000, repeat=False)
        plt.show()
    except KeyboardInterrupt:
        print("Interrupted by user. Closing the plot...")
        plt.close(fig)

# ---------------------------------------------------------



def on_message_received(ch, method, properties, body):
    global data
    message = json.loads(body)
    data.append(message)
    print("message received{}: ".format(message))
    graficar_velas_japonesas()
    #time.sleep(3)


def main():
    global data, fig, ax

# VARIABLES DE ENTORNO -----------------------------------------------
    load_dotenv()
    # Obtener valores de variables de entorno
    rabbitmq_host = os.environ.get("RABBITMQ_HOST")
    rabbitmq_port = int(os.environ.get("RABBITMQ_PORT"))
    rabbitmq_virtual_host = os.environ.get("RABBITMQ_VIRTUAL_HOST")
    rabbitmq_username = os.environ.get("RABBITMQ_USERNAME")
    rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")


# RabbitMQ -----------------------------------------------------------

    #connection_parameters = pika.ConnectionParameters('54.85.196.208', 5672, '/', pika.PlainCredentials("user", "password"))
    connection_parameters = pika.ConnectionParameters(
        host=rabbitmq_host,
        port=rabbitmq_port,
        virtual_host=rabbitmq_virtual_host,
        credentials=pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
    )
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    #Declare my queue
    channel.queue_declare(queue= "candles")

    channel.basic_consume(queue= 'candles', auto_ack=True, on_message_callback=on_message_received)
    
    print("Esperando mensajes... Presiona Ctrl+C para salir.")
    channel.start_consuming()
    
    

# GRAFICO


if __name__ == "__main__":
    #data = []
    #fig, ax = plt.subplots()
    #index = 0
    main()