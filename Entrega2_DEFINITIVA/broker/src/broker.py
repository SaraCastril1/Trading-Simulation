import srv_al_cliente
import consume_al_mercado
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    PORT = os.environ.get("PORT")
    srv_al_cliente.server(PORT)