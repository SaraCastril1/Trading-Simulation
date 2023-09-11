import os
from celery import Celery, shared_task
from dotenv import load_dotenv
from datetime import time
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
		print(resultado)
		if resultado:
			#Prueba almacenar varias veces durante 30 segundos sin bloquear el cliente
			cuantos = resultado[0][0]
		print("Comandos{} -> {}".format(comando, cuantos))
		for x in range(0,30):
			try:
				with registro:
					registro.execute("INSERT OR REPLACE INTO registro(repeticiones, comando) VALUES({},\"{}\");".format(cuantos+1, comando))
			except:
				time.sleep(1)
				pass
			finally:
				break
