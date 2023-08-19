import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from mplf_inance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.ticker as mticker
import time
#import random

from datetime import datetime
import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime


class Chart:

  def __init__(self):
    self.data = {
        "Fecha": [],
        "Apertura": [],
        "Alto": [],
        "Bajo": [],
        "Cierre": []
    }
    #self.data = []
    #self.start_date = datetime.date(2000, 1, 1)
    #self.end_date = datetime.date(2023, 12, 31)
    #self.Assets = moneda

    #self.import_ticks_method(self.Assets, self.start_date, self.end_date, 1, TimeFrame.TICK, ".", True)

    #GENERATE THE CANDLESTICK CHART
    self.fig = plt.figure(figsize=(8.5, 6.0))
    self.ax1 = plt.subplot2grid((1, 1), (0, 0))

    #candle_counter = range(len(self.data["Fecha"]) - 1)

  def graficar_velas_chinas(self):
    #print(self.start_date)
    #print(self.end_date)
    #print(self.Assets)

    ohlc_data = []
    for i in range(len(self.data["Fecha"])):
      ohlc_data.append(
          (mdates.date2num(self.data["Fecha"][i]),
           float(self.data["Apertura"][i]),
           float(self.data["Alto"][i]),
           float(self.data["Bajo"][i]),
           float(self.data["Cierre"][i])
          ))

    candlestick_ohlc(self.ax1,
                     ohlc_data,
                     width=0.2,
                     colorup='#075105',
                     colordown='#AF141A')

    for label in self.ax1.xaxis.get_ticklabels():
      label.set_rotation(45)

    self.ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    self.ax1.grid(True)
    plt.xlabel('Candle counter')
    plt.ylabel('Price')
    plt.title('Candlestick sample representation')
    plt.grid(False)

    plt.subplots_adjust(left=0.09,
                        bottom=0.20,
                        right=0.94,
                        top=0.90,
                        wspace=0.2,
                        hspace=0)
    plt.show()
