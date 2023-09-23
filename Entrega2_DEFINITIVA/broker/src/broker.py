#import srv_al_cliente
import consume_al_mercado
from dotenv import load_dotenv
import os

def main():
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
    # Recibe la comunicación del cliente
    #srv_al_cliente.server(PORT)
    print(PORT_9)
    consume_al_mercado.server(PORT_9)

    # # Levanta la comunicación con el mercado
    # moneda = srv_al_cliente.moneda
    # periodo = srv_al_cliente.periodo
    # print('YA VOY A LLAMAR AL MERCADO CO LOS SIGUIENTES PARAMETROS', moneda, periodo)
    # consume_al_mercado.server(HOST_MERCADO, moneda, periodo)
if __name__ == '__main__':
    main()