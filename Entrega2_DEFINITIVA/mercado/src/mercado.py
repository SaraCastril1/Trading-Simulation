from concurrent import futures

import grpc
import sys
import os
import moneda_pb2
import moneda_pb2_grpc
from dotenv import load_dotenv


# # CONEXIÓN CON EL BROKER ------------------------------------------------------------------------

# class Parameters(moneda_pb2_grpc.ParametersServicer):

#     def send_parameters(self, request, context):
#         moneda = request.moneda
#         periodo = request.periodo

#         # Realiza el procesamiento necesario con moneda y período aquí.
#         # Puedes agregar tu lógica de procesamiento personalizada.
#         print("Moneda recivida: ", moneda)
#         print("Periodo recivida: ", periodo)

#         # Envía una respuesta de confirmación (ACK).
#         response = moneda_pb2.ACK(ack=True)
#         return response

# def server(PORT):
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
#     moneda_pb2_grpc.add_ParametersServicer_to_server(Parameters(), server)

#     # Cambia la dirección y el puerto según tus necesidades.
#     server.add_insecure_port(PORT)
#     server.start()
#     print("Mercado en ejecución en el puerto {}...".format(PORT))
#     server.wait_for_termination()


# EN ESTA PARTE SE COMPORTA COMO PRODUCTOR PARA MANDAR EL PING AL BROKER
def send_parameters(stub, moneda, periodo):
    request = moneda_pb2.message_parameters(moneda=moneda, periodo=periodo)
    response = stub.send_parameters(request)
    print("ACK:", response.ack)

def conexion_up(stub, mercado):
    request = moneda_pb2.ping(mercado=mercado)
    response = stub.send_parameters(request)
    print("ACK:", response.ack)


def server(HOST, mercado):
    # LEVANTA LA CONEXIÓN CON EL BROKER ---------------------------------------------------------
    with grpc.insecure_channel(HOST) as channel:
        stub = moneda_pb2_grpc.ParametersStub(channel)

        conexion_up(stub, mercado)
        #send_parameters(stub,moneda, periodo)





def main():
    load_dotenv()
    #print(len(sys.argv))
    if len(sys.argv) > 1:
        #print(sys.argv[1])
        
        if sys.argv[1] == '1':
            HOST = os.environ.get("HOST-1")
        elif sys.argv[1] == '2':
            HOST = os.environ.get("HOST-2")
        elif sys.argv[1] == '3':
            HOST = os.environ.get("HOST-3")
        elif sys.argv[1] == '4':
            HOST = os.environ.get("HOST-4")
        elif sys.argv[1] == '5':
            HOST = os.environ.get("HOST-5")
        elif sys.argv[1] == '6':
            HOST = os.environ.get("HOST-6")
        elif sys.argv[1] == '7':
            HOST = os.environ.get("HOST-7")
        elif sys.argv[1] == '8':
            HOST = os.environ.get("HOST-8")
        elif sys.argv[1] == '9':
            HOST = os.environ.get("HOST-9")
        else:
            print("El mercado especificado no está en el rango válido (1-9).")
            sys.exit(1)

        # Now you can use the PORT variable here or pass it to another function.
        print("La petición se enviará a {}...".format(HOST))
        server(HOST, int(sys.argv[1]))

    else:
        print("Se necesita especificar el mercado a ejecutar.")
        sys.exit(1)

if __name__ == '__main__':
    main()
