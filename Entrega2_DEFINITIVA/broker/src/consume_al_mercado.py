from concurrent import futures
from dotenv import load_dotenv
import os

import grpc
#from dotenv import load_dotenv
import moneda_pb2
import moneda_pb2_grpc

def send_parameters(stub, moneda, periodo):
    request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
    response = stub.send_parameters(request)
    print("ACK:", response.ack)

def conexion_up(stub):
    request = moneda_pb2.ping()
    response = stub.send_parameters(request)
    print("ACK:", response.ack)


def server(HOST, moneda, periodo):
    # LEVANTA LA CONEXIÓN CON EL MERCADO ---------------------------------------------------------
    with grpc.insecure_channel(HOST) as channel:
        stub = moneda_pb2_grpc.ParametersStub(channel)

        #conexion_up(stub)
        send_parameters(stub,moneda, periodo)
    

# CONEXIÓN CON EL MERCADO ------------------------------------------------------------------------
# Contador para llevar un registro de las conexiones de mercado recibidas.
# market_connections = []
# mercados_conectados = []

# class Parameters(moneda_pb2_grpc.ParametersServicer):


#     def send_parameters(self, request, context):
#         # Implementa la lógica del servidor aquí
#         response = moneda_pb2.ACK(ack=True)  # Por ejemplo, aquí puedes devolver una respuesta de confirmación
#         return response
    

#     def conexion_up(self, request, context):
#         global market_connections, mercados_conectados

#         mercado = request.mercado
#         print("Mercado recibido: ", mercado)
#         mercados_conectados.append(mercado)
#         market_connections.append(context)

#         # Realiza el procesamiento necesario con moneda y período aquí.
#         # Puedes agregar tu lógica de procesamiento personalizada.

#         # Verifica si se han recibido conexiones de 5 mercados.
#         if len(market_connections) >= 5:
#             # Envía un ACK a cada conexión de mercado en la lista.
#             for connection in market_connections:
#                 response = moneda_pb2.ACK(ack=True, mensaje="Se han recibido conexiones de 5 mercados.")
#                 connection.write(response)

#         # No envíes ACK en esta etapa.
#         return moneda_pb2.ACK(ack=False)
        
        
#         # Devuelve los datos que deseas imprimir como parte de la respuesta
#         # response = moneda_pb2.ACK(ack=True)
#         # return response



# def server(PORT_1, PORT_2, PORT_3,PORT_4, PORT_5, PORT_6, PORT_7, PORT_8, PORT_9):#, PORT_2, PORT_3, PORT_4, PORT_5, PORT_6, PORT_7, PORT_8, PORT_9):
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     moneda_pb2_grpc.add_ParametersServicer_to_server(Parameters(), server)

#     # Cambia la dirección y el puerto según tus necesidades.
#     server.add_insecure_port(PORT_1)
#     server.add_insecure_port(PORT_2)
#     server.add_insecure_port(PORT_3)
#     server.add_insecure_port(PORT_4)
#     server.add_insecure_port(PORT_5)
#     server.add_insecure_port(PORT_6)
#     server.add_insecure_port(PORT_7)
#     server.add_insecure_port(PORT_8)
#     server.add_insecure_port(PORT_9)

#     server.start()
#     print("Escuchando en:\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}...".format(PORT_1, PORT_2, PORT_3,PORT_4, PORT_5, PORT_6, PORT_7, PORT_8, PORT_9))
#     server.wait_for_termination()





    

