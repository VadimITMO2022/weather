import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="🌦 Привет! Прогноз погоды на сегодня:)))))))) 🌦",
            brand_href="#",
            color="primary",
            dark=True,
            className="mb-4 flex justify-content-between",
        ),
        dbc.Row([
            dbc.Col([
                dbc.Input(id='city-input', value='Санкт-Петербург', type='text', placeholder="Введите город", debounce=True),
            ], width=6, xs=12, md=6),
            dbc.Col(dbc.Card(id='weather-output', body=True), width=6, xs=12, md=6),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='temp-graph'), width=6, xs=12, md=6),
            dbc.Col(dcc.Graph(id='ap-graph'), width=6, xs=12, md=6),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='wind-dir-graph'), width=12, xs=12, md=12),
        ], className="mb-3"),

        
    ], fluid=True)