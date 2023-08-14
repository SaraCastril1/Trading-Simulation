import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import time
import random
from datetime import timedelta

class Chart:

    def __init__(self):
        self.data = []

    def graficar_velas_chinas(self):
        plt.ion()
        fig, ax = plt.subplots()
        index = 0  # Índice para rastrear la posición actual en los datos
        while index < len(self.data):  # Condición de salida cuando no hay más datos
            ax.clear()
            # Tomar un segmento de datos hasta el índice actual
            segmento_data = self.data[:index+1]
            fechas_num = [mdates.date2num(item['Fecha']) for item in segmento_data]
            quotes = [(fechas_num[i], float(item['Apertura']), float(item['Alto']), float(item['Bajo']), float(item['Cierre'])) for i, item in enumerate(segmento_data)]
            
            ax.xaxis_date()
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            plt.xticks(rotation=45)
            
            candlestick_ohlc(ax, quotes, width=0.02, colorup='g', colordown='r')
            
            plt.pause(1)  # Pausa para una actualización más lenta (puedes ajustar este valor)
            
            index += 1  # Incrementar el índice para avanzar a través de los datos
