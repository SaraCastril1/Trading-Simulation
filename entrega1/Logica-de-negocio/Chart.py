import plotly.graph_objects as go

class Chart:
    
    def __init__(self):
        self.fig = go.Figure()  # Crear una instancia del gráfico al inicio

    def crear_grafico(self, timestamp, open_price, high_price, low_price, close_price):
        # Añadir una nueva vela al gráfico existente
        self.fig.add_trace(go.Candlestick(x=[timestamp],
                                          open=[open_price],
                                          high=[high_price],
                                          low=[low_price],
                                          close=[close_price]))

        self.fig.show()