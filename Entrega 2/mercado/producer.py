import pika
import os
import sys
import csv
import json
import gc
from dotenv import load_dotenv
from datetime import datetime, timedelta



def main():
    #Variables de entorno
    load_dotenv()
    # Obtener valores de variables de entorno
    rabbitmq_host = os.environ.get("RABBITMQ_HOST")
    rabbitmq_port = int(os.environ.get("RABBITMQ_PORT"))
    rabbitmq_virtual_host = os.environ.get("RABBITMQ_VIRTUAL_HOST")
    rabbitmq_username = os.environ.get("RABBITMQ_USERNAME")
    rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")

# PARAMETROS POR CONSOLA -------------------------------------------------------------------

    # sys.argv[0] es el nombre del script en sí mismo, los argumentos comienzan desde sys.argv[1]
    parsed_args = {"-p": None,  "-m": None}    

    if len(sys.argv) > 2:
        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            elif arg.startswith("-m="):
                parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        print("Moneda:", parsed_args["-m"])

    else:
        print("Se necesitan al menos 2 argumentos.")
        return(1)
    


# RABBIT_MQ --------------------------------------------------------------------------------
    connection_parameters = pika.ConnectionParameters(
        host=rabbitmq_host,
        port=rabbitmq_port,
        virtual_host=rabbitmq_virtual_host,
        credentials=pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
    )

    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel = connection.channel()
    print("Server is running...")

    #Declare my queue
    channel.queue_declare(queue= "candles")



# SIMTRADING -> Lectura de datos y envio hacia el MOM ------------------------------------------------------------

    nombre_archivo = ruta = f"{parsed_args['-m']}_{parsed_args['-p']}.csv"
    ruta = os.path.join('.\MonedasCSV', nombre_archivo)

    try:
        with open(ruta, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                message ={
                    'Fecha': datetime.strptime(row[0], "%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M"),
                    'Apertura': row[1],
                    'Alto': row[2],
                    'Bajo': row[3],
                    'Cierre': row[4]
                }
                    
                channel.basic_publish(exchange="", routing_key="candles", body=json.dumps(message))
                print("Message sent:", message)


        f.close()



    except FileNotFoundError:
        print("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


    # Cerrar la conexión a RabbitMQ
    connection.close()

    #message = "Hello this is my first message"

    # Publicar el mensaje y esperar ACK
    #channel.basic_publish(exchange="", routing_key="candles", body=message, mandatory=True)
    #print("Message sent")

    #connection.close()



if __name__ == "__main__":
    main()