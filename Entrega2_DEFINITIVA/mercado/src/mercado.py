from concurrent import futures

import grpc
import sys
import os
import moneda_pb2
import moneda_pb2_grpc
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




def main():
    load_dotenv()
    #print(len(sys.argv))
    if len(sys.argv) > 1:
        #print(sys.argv[1])
        
        if sys.argv[1] == '1':
            PORT = os.environ.get("PORT-1")
        elif sys.argv[1] == '2':
            PORT = os.environ.get("PORT-2")
        elif sys.argv[1] == '3':
            PORT = os.environ.get("PORT-3")
        elif sys.argv[1] == '4':
            PORT = os.environ.get("PORT-4")
        elif sys.argv[1] == '5':
            PORT = os.environ.get("PORT-5")
        elif sys.argv[1] == '6':
            PORT = os.environ.get("PORT-6")
        elif sys.argv[1] == '7':
            PORT = os.environ.get("PORT-7")
        elif sys.argv[1] == '8':
            PORT = os.environ.get("PORT-8")
        elif sys.argv[1] == '9':
            PORT = os.environ.get("PORT-9")
        else:
            print("El mercado especificado no está en el rango válido (1-9).")
            sys.exit(1)

        # Now you can use the PORT variable here or pass it to another function.
        server(PORT)

    else:
        print("Se necesita especificar el mercado a ejecutar.")
        sys.exit(1)

if __name__ == '__main__':
    main()
