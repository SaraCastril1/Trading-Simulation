import csv
import gc
import json
import os
#from Chart import Chart
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
import time
from Server import Server 

class Scanner:

    def __init__(self):
        self.ini = 0
        self.final = 10
        self.end_ofFile = False
        

    def leer_csv(self, ruta):
        try:
            with open(ruta, 'r') as f:
                reader = csv.reader(f)
                first_10_lines = []

                #Verificar si has llegado al final del archivo
                if f.tell() == os.fstat(f.fileno()).st_size:
                    self.end_ofFile = True
                    return first_10_lines
            
                for i, row in enumerate(reader):
                    if i < self.ini:
                        continue

                    if i >= self.final:
                        self.ini = self.final
                        self.final += 10
                        return first_10_lines
                    else:
                        print(i)
                        #first_10_lines.append(row)
                        first_10_lines.append({
                            'Fecha': datetime.strptime(row[0], "%Y-%m-%d %H:%M"),
                            'Apertura': row[1],
                            'Alto': row[2],
                            'Bajo': row[3],
                            'Cierre': row[4]
                     })
                
                return first_10_lines
                # for row in reader:
                #     self.chart.data.append({
                #         'Fecha': datetime.strptime(row[0], "%Y-%m-%d %H:%M"),
                #         'Apertura': row[1],
                #         'Alto': row[2],
                #         'Bajo': row[3],
                #         'Cierre': row[4]
                #     })
            #self.chart.graficar_velas_chinas()
            #self.server.send_data(next(reader))
            #f.close()

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
