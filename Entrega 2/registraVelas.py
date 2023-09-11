import os
from celery import Celery, shared_task
from dotenv import load_dotenv
import datetime
import sqlite3
import json


load_dotenv()

#Declara el app de celery
app = Celery('registra-velas',
             broker = 'amqp://{}:{}@54.85.196.208:5672/sara_vhost'.format(os.environ.get('user'), os.environ.get('password')))

#Declara un fichero sqlite
now = datetime.datetime.now()
registro = sqlite3.connect("comandos-{}-{}-{}-{}-{}-{}.db".format(now.year, now.month, now.day, now.hour, now.minute ))
registro.execute('''CREATE TABLE IF NOT EXISTS registro
                 (repeticiones INT, comando VARCHAR(32) unique)''') 

#Declara la tarea
@shared_task #Función que devuelve otra función
def registrar(comando):
	with registro:
		resultado = registro.execute("SELECT REPETICIONES FROM REGISTRO where comando = \"{}\"".format(comando)).fetchall()
