import csv
import gc
import json
from Chart import Chart
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time


class Scanner:

  def __init__(self):
    #self.moneda = moneda
    self.chart = Chart()  # Crear una instancia única de la clase Chart

  def leer_csv(self, ruta):
    try:
      with open(ruta, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
          #self.chart.data.append({
          #    'Fecha':
          #    datetime.strptime(row[0], "%Y-%m-%d %H:%M"),
          #    'Apertura':
          #    row[1],
          #    'Alto':
          #    row[2],
          #    'Bajo':
          #    row[3],
          #    'Cierre':
          #    row[4]
          #})
          self.chart.data["Fecha"].append(datetime.strptime(row[0], "%Y-%m-%d %H:%M") )
          self.chart.data["Apertura"].append(row[1])
          self.chart.data["Alto"].append(row[2])
          self.chart.data["Bajo"].append(row[3])
          self.chart.data["Cierre"].append(row[4])

      
      self.chart.graficar_velas_chinas()
      f.close()

    except FileNotFoundError:
      print("No se encontró en la ruta especificada.")
    except Exception as e:
      print("Ocurrió un error:", str(e))

  def leer_json(self, ruta):
    print("Leyendo archivo JSON...")
    try:
      with open(ruta, 'r') as f:
        contenido = json.load(f)
        fecha_inicial = datetime(2000, 1, 1)
        for i in range(len(contenido['time'])):
          fecha = fecha_inicial + timedelta(minutes=contenido['time'][i])
          self.chart.data.append({
              'Fecha': fecha,
              'Apertura': contenido['open'][i],
              'Alto': contenido['high'][i],
              'Bajo': contenido['low'][i],
              'Cierre': contenido['close'][i]
          })
      self.chart.graficar_velas_chinas()
      f.close()

    except FileNotFoundError:
      print("No se encontró en la ruta especificada.")
    except Exception as e:
      print("Ocurrió un error:", str(e))
