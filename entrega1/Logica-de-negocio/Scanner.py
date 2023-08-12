import csv
import gc
from Chart import Chart

class Scanner:

    def __init__(self):
        self.chart = Chart()  # Crear una instancia única de la clase Chart



    def leer_csv(self, ruta):
        #datos_todos = []

        try:
            with open(ruta, 'r') as f:
                lector = csv.reader(f)
                for fila in lector:
                    # timestamp = fila[0]
                    # open_price = float(fila[1])
                    # high_price = float(fila[2])
                    # low_price = float(fila[3])
                    # close_price = float(fila[4])
                    #crear_grafico(fila[0], float(fila[1]), float(fila[2]), float(fila[3]), float(fila[4]))

                    #datos_todos.append(fila)
                    #print(fila)
                    self.chart.crear_grafico(fila[0], float(fila[1]), float(fila[2]), float(fila[3]), float(fila[4]))

        except FileNotFoundError:
            print("El archivo no se encontró en la ruta especificada.")
        except Exception as e:
            print("Ocurrió un error:", str(e))

        

        
        del lector    # Liberar manualmente el objeto lector
        gc.collect()  # Invocar al recolector de basura
        print("Se ha eliminado el lector csv de la memoria")

        del chart    # Liberar manualmente el objeto lector
        gc.collect()  # Invocar al recolector de basura
        print("Se ha eliminado el objeto chart de la memoria")



    def leer_json(self, ruta):
        print("Soy JSON")