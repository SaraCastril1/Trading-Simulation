import pika
import os
from dotenv import load_dotenv

class Conexion:
    #Esta clase encapsula  la conexión a RabbitMQ
    enlace = None
    canal = None

    def __init__(self, dotenv_path = ".env"): #el fichero estará en el mismo directorio
        load_dotenv(dotenv_path=dotenv_path)
        
        #Coneccion a rabbitMQ con un URL -> amqp+ip+nombre de host virtual

        #sudo rabbitmqctl add_vhost <nombre_vhost>
        #sudo rabbitmqctl add_user <nombre de usuario> <password usuario>
        #sudo rabbitmqctl set_permissions -p <nombre vhost> <nombre de usuario> ".*" ".*" ".*"
        parameters = pika.URLParameters('amqp://{}:{}@54.85.196.208:5672/sara_vhost'.format(os.environ.get('user'), os.environ.get('password')))

        self.enlace = pika.BlockingConnection(parameters)
        self.canal = self.enlace.channel

        self.canal.queue_declare(queue = 'my_queue')