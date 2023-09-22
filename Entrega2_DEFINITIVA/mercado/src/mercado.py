from concurrent import futures

import grpc
import moneda_pb2
import moneda_pb2_grpc
import os
from dotenv import load_dotenv


# CONEXIÓN CON EL BROKER ------------------------------------------------------------------------

class Parameters(moneda_pb2_grpc.ParametersServicer):

    def send_parameters(self, request, context):
        moneda = request.moneda
        periodo = request.periodo

        # Realiza el procesamiento necesario con moneda y período aquí.
        # Puedes agregar tu lógica de procesamiento personalizada.
        print("Moneda recivida: ", moneda)
        print("Periodo recivida: ", periodo)

        # Envía una respuesta de confirmación (ACK).
        response = moneda_pb2.ACK(ack=True)
        return response

def server(PORT):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    moneda_pb2_grpc.add_ParametersServicer_to_server(Parameters(), server)

    # Cambia la dirección y el puerto según tus necesidades.
    server.add_insecure_port(PORT)
    server.start()
    print("Mercado en ejecución en el puerto {}...".format(PORT))
    server.wait_for_termination()

if __name__ == '__main__':
    load_dotenv()
    PORT = os.environ.get("PORT") 
    server(PORT)
