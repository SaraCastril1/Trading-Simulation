from concurrent import futures
from dotenv import load_dotenv
import os

import grpc
#from dotenv import load_dotenv
import moneda_pb2
import moneda_pb2_grpc

# def send_parameters(stub, moneda, periodo):
#     request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
#     response = stub.send_parameters(request)
#     print("ACK:", response.ack)

# def conexion_up(stub):
#     request = moneda_pb2.ping()
#     response = stub.send_parameters(request)
#     print("ACK:", response.ack)


# def server(HOST, moneda, periodo):
#     # LEVANTA LA CONEXIÓN CON EL MERCADO ---------------------------------------------------------
#     with grpc.insecure_channel(HOST) as channel:
#         stub = moneda_pb2_grpc.ParametersStub(channel)

#         #conexion_up(stub)
#         send_parameters(stub,moneda, periodo)
    

# CONEXIÓN CON EL MERCADO ------------------------------------------------------------------------

class Parameters(moneda_pb2_grpc.ParametersServicer):

    def conexion_up(self, request, context):

        mercado = request.mercado
        # Realiza el procesamiento necesario con moneda y período aquí.
        # Puedes agregar tu lógica de procesamiento personalizada.
        print("Mercado recivido: ", mercado)

        # Envía una respuesta de confirmación (ACK).
        response = moneda_pb2.ACK(ack=True)
        return response


def server(PORT_1, PORT_2, PORT_3, PORT_4, PORT_5, PORT_6, PORT_7, PORT_8, PORT_9):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    moneda_pb2_grpc.add_ParametersServicer_to_server(Parameters(), server)

    # Cambia la dirección y el puerto según tus necesidades.
    server.add_insecure_port(PORT_1)
    server.add_insecure_port(PORT_2)
    server.add_insecure_port(PORT_3)
    server.add_insecure_port(PORT_4)
    server.add_insecure_port(PORT_5)
    server.add_insecure_port(PORT_6)
    server.add_insecure_port(PORT_7)
    server.add_insecure_port(PORT_8)
    server.add_insecure_port(PORT_9)

    server.start()
    print("Broker en ejecución en el puerto {}...".format(PORT_1))
    server.wait_for_termination()



if __name__ == '__main__':
    load_dotenv()
    PORT_1 = os.environ.get("PORT-1")
    PORT_2 = os.environ.get("PORT-2")
    PORT_3 = os.environ.get("PORT-3")
    PORT_4 = os.environ.get("PORT-4")
    PORT_5 = os.environ.get("PORT-5")
    PORT_6 = os.environ.get("PORT-6")
    PORT_7 = os.environ.get("PORT-7")
    PORT_8 = os.environ.get("PORT-8")
    PORT_9 = os.environ.get("PORT-9")

    server(PORT_1, PORT_2, PORT_3, PORT_4, PORT_5, PORT_6, PORT_7, PORT_8, PORT_9)
    #AÑADIR TODOS LOS PUERTOS