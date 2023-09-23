#from concurrent import futures

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
    


