from concurrent import futures
import consume_al_mercado
from dotenv import load_dotenv
import os

import grpc
#import os
#from dotenv import load_dotenv
import moneda_pb2
import moneda_pb2_grpc

# Variables globales 
moneda = None
periodo = None

# CONEXIÓN CON EL CLIENTE ------------------------------------------------------------------------

class Parameters(moneda_pb2_grpc.ParametersServicer):

    def send_parameters(self, request, context):

        global moneda, periodo

        moneda = request.moneda
        periodo = request.periodo

        # Realiza el procesamiento necesario con moneda y período aquí.
        # Puedes agregar tu lógica de procesamiento personalizada.
        print("Moneda recivida: ", moneda)
        print("Periodo recivida: ", periodo)

        # # Levanta la comunicación con el mercado
        print('YA VOY A LLAMAR AL MERCADO CO LOS SIGUIENTES PARAMETROS', moneda, periodo)
        consume_al_mercado.server(os.environ.get("HOST_MERCADO-9"), moneda, periodo)

        # Envía una respuesta de confirmación (ACK).
        response = moneda_pb2.ACK(ack=True)
        return response


def server_client(PORT):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    moneda_pb2_grpc.add_ParametersServicer_to_server(Parameters(), server)

    # Cambia la dirección y el puerto según tus necesidades.
    server.add_insecure_port(PORT)
    server.start()
    print("Broker en ejecución en el puerto {}...".format(PORT))
    server.wait_for_termination()

# if __name__ == '__main__':
#     load_dotenv()
#     HOST = os.environ.get("HOST") 
#     server(HOST)
