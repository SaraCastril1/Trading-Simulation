import sys
import os
import csv
import plotly.graph_objects as go


def crear_grafico(timestamp, open_price, high_price, low_price, close_price):
    # Crear el gráfico de velas japonesas
    #fig = go.Figure()fig.add_trace
    fig = go.Figure(data=[go.Candlestick(x=[timestamp],
                                          open=[open_price],
                                          high=[high_price],
                                          low=[low_price],
                                          close=[close_price])])


    fig.show()


def leer_csv(ruta):
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
                crear_grafico(fila[0], float(fila[1]), float(fila[2]), float(fila[3]), float(fila[4]))

                #datos_todos.append(fila)
                #print(fila)
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", str(e))

    #return datos_todos


#def leer_csv(ruta):

    


def main():
    # sys.argv[0] es el nombre del script en sí mismo, los argumentos comienzan desde sys.argv[1]
    parsed_args = {"-p": None, "-f": None, "-m": None}    

    if len(sys.argv) > 3:
        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            elif arg.startswith("-f="):
                parsed_args["-f"] = arg.split("=")[1]
            elif arg.startswith("-m="):
                parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        print("Formato:", parsed_args["-f"])
        print("Moneda:", parsed_args["-m"])

    else:
        print("Se necesitan al menos 3 argumentos.")
        return(1)

    
    nombre_archivo = ruta = f"{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
    if parsed_args["-f"] == "CSV":
        #ModedasCSV\BRENTCMDUSD_H1.csv
        #ruta = f".\MonedasCSV\{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
        ruta = os.path.join('.\MonedasCSV', nombre_archivo)
        print("Ruta: ",ruta)
        leer_csv(ruta)
        #for fila in datos:
        #    print(fila)
        

    elif parsed_args["-f"] == "JSON":
        #ruta = f"./MonedasJSON/{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
        ruta = os.path.join('.\MonedasJSON', nombre_archivo)
        print("Ruta: ",ruta)
        #leer_json(ruta)

    else:
        print("Formato de archivo NO valido.")
        return(1)



    
if __name__ == "__main__":
    main()

