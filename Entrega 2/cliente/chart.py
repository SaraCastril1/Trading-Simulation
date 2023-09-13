import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from mplfinance.original_flavor import candlestick_ohlc
import datetime
import numpy as np

class Chart:

    def __init__(self):
        self.data = []
        self.fig, self.ax = plt.subplots()
        self.index = 0

    def animate(self, i):
        plt.ion()
        if self.index < len(self.data):
            self.ax.clear()
            segmento_data = self.data[:self.index+1]
            if len(segmento_data) >= 20:  # Si hay 20 datos
                del segmento_data[0] 
                del self.data[0]
            else:
                pass
            
            fechas = [item['Fecha'] if isinstance(item['Fecha'], datetime.datetime) else datetime.datetime.strptime(item['Fecha'], '%Y-%m-%d %H:%M:%S') for item in segmento_data]
            fechas_num = mdates.date2num(fechas)
            quotes = [(fechas_num[i], float(item['Apertura']), float(item['Alto']), float(item['Bajo']), float(item['Cierre'])) for i, item in enumerate(segmento_data)]
            
            # Calculate the SMA of 5 and 13 periods
            cierres = [float(item['Cierre']) for item in segmento_data]
            sma5 = np.convolve(cierres, np.ones(5)/5, mode='valid')
            sma13 = np.convolve(cierres, np.ones(13)/13, mode='valid')
            
            self.ax.xaxis_date()
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
            plt.xticks(rotation=45)
            
            candlestick_ohlc(self.ax, quotes, width=0.01, colorup='g', colordown='r')
            
            # Plot the SMA
            if self.index >= 4:  # Only plot the 5-period SMA if there are at least 5 data points
                self.ax.plot(fechas_num[4:self.index+1], sma5, label='SMA 5', color='blue')
                # Show the legend
                self.ax.legend()
            if self.index >= 12:  # Only plot the 13-period SMA if there are at least 13 data points
                self.ax.plot(fechas_num[12:self.index+1], sma13, label='SMA 13', color='orange')
                # Show the legend
                self.ax.legend()
            
            
            self.index += 1

    def graficar_velas_japonesas(self):
        try:
            ani = FuncAnimation(self.fig, self.animate, interval=1000, repeat=False)
            plt.show()
        except KeyboardInterrupt:
            print("Interrupted by user. Closing the plot...")
            plt.close(self.fig)