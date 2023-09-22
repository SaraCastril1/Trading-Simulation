import srv_al_cliente
import consume_al_mercado
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    HOST = os.environ.get("HOST_MERCADO")
    srv_al_cliente.server(HOST)