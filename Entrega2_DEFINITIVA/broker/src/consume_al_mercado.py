from concurrent import futures

from srv_al_cliente import Parameters
import sys
import os
import grpc
from dotenv import load_dotenv
import moneda_pb2
import moneda_pb2_grpc

def send_parameters(stub, moneda, periodo):
    request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
    response = stub.send_parameters(request)
    print("ACK:", response.ack)



def serve(HOST, moneda, periodo):
    # LEVANTA LA CONEXIÓN CON EL MERCADO ---------------------------------------------------------
    with grpc.insecure_channel(HOST) as channel:
        stub = moneda_pb2_grpc.ParametersStub(channel)

        send_parameters(stub,parsed_args["-m"], parsed_args["-p"])
    


