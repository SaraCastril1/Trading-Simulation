from concurrent import futures

import sys
import os
import grpc
from dotenv import load_dotenv
import moneda_pb2
import moneda_pb2_grpc

# def send_parameters(stub, moneda, periodo):
#     request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
#     response = stub.send_parameters(request)
#     print("ACK:", response.ack)

def send_parameters(stub, moneda, periodo):
    if moneda is None or periodo is None:
        print("Moneda y período deben especificarse...")
        return(1)
    
    request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
    response = stub.send_parameters(request)
    print("ACK:", response.ack)




def serve(HOST):
    # LEVANTA LA CONEXIÓN CON EL BROKER ---------------------------------------------------------
    parsed_args = {"-p": None, "-m": None} 
    with grpc.insecure_channel(HOST) as channel:
        stub = moneda_pb2_grpc.ParametersStub(channel)

        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            elif arg.startswith("-m="):
                parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        print("Moneda:", parsed_args["-m"])

        send_parameters(stub,parsed_args["-m"], parsed_args["-p"])
    




def main():

# ELEGIR PARAMETROS PARA ENVIARLOS AL BROKER  -----------------------------------------------------------
    # sys.argv[0] es el nombre del script en sí mismo, los argumentos comienzan desde sys.argv[1]
    load_dotenv()
    HOST = os.environ.get("HOST_BROKER")   

    if len(sys.argv) > 2:
        serve(HOST)

    else:
        print("Se necesitan al menos 2 argumentos.")
        return(1)


    
if __name__ == "__main__":
    main()