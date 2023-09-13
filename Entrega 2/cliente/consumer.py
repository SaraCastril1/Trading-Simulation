import pika
import os
import json
from dotenv import load_dotenv
from chart import Chart

def on_message_received_wrapper(chart):
    def on_message_received(ch, method, properties, body):
        print("Received{}".format(body))
        try:
            message = json.loads(body)
            
            # Procesa el mensaje y genera la gráfica de vela
            chart.data.append(message)
            chart.graficar_velas_japonesas()

            # Confirma el mensaje (ACK) para eliminarlo de la cola
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print("Error al procesar el mensaje:", str(e))
    return on_message_received



def main():

    chart = Chart()
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

    channel.basic_consume(queue= 'candles', auto_ack=True, on_message_callback=on_message_received_wrapper(chart))

    print("Esperando mensajes... Presiona Ctrl+C para salir.")
    channel.start_consuming()
    

# GRAFICO


if __name__ == "__main__":
    main()