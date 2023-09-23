import srv_al_cliente
import consume_al_mercado
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    PORT = os.environ.get("PORT")
    # Recibe la comunicación del cliente
    #srv_al_cliente.server(PORT)
    consume_al_mercado.server("PORT")

    # # Levanta la comunicación con el mercado
    # moneda = srv_al_cliente.moneda
    # periodo = srv_al_cliente.periodo
    # print('YA VOY A LLAMAR AL MERCADO CO LOS SIGUIENTES PARAMETROS', moneda, periodo)
    # consume_al_mercado.server(HOST_MERCADO, moneda, periodo)
if __name__ == '__main__':
    main()