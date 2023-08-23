import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
#import time
#import random
from datetime import timedelta
import numpy as np

class Chart:

    def __init__(self):
        self.data = []
        self.fig, self.ax = plt.subplots()
        self.inicio = 0
        self.final = 0



    def graficar_velas_chinas(self):
        plt.ion()

        
        while self.final < len(self.data):  # Condición de salida cuando no hay más datos
            self.ax.clear()
            # Tomar un segmento de datos hasta el índice actual
            segmento_data = self.data[self.inicio:self.final+1]
            #segmento_data = self.data[:final+1]
            fechas_num = [mdates.date2num(item['Fecha']) for item in segmento_data]
            quotes = [(fechas_num[i], float(item['Apertura']), float(item['Alto']), float(item['Bajo']), float(item['Cierre'])) for i, item in enumerate(segmento_data)]
            
            self.ax.xaxis_date()
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            plt.xticks(rotation=45)
            
            candlestick_ohlc(self.ax, quotes, width=0.01, colorup='g', colordown='r')

            # if final >= 4:
            #     sma5 = np.mean([item['Cierre'] for item in segmento_data[final-4:final+1]])
            #     self.ax.plot(fechas_num[4:final+1], [sma5] * (final - 4 + 1), label='SMA 5', color='blue')
            #     #self.ax.plot(fechas_num[4:final+1], sma5, label= 'SMA 5', color='blue')
            # if final >= 12:
            #     self.ax.plot(fechas_num[12:final+1], sma13, label= 'SMA 13', color='orange')



            if self.final - self.inicio > 10:
                self.inicio+=1
                #self.data.pop(0)
                #self.data.remove(self.data[0])

            
            plt.pause(1)  # Pausa para una actualización más lenta (puedes ajustar este valor)
            
            self.final += 1  # Incrementar el índice para avanzar a través de los datos