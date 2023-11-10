import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import requests
import dash_bootstrap_components as dbc


##Set de datos de México
# Abrir archivo de datos
d_m = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MEXICO.csv")
# Obtener geojson que funciona como el mapa
url_mx = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json'
mx_region = requests.get(url_mx).json()

# Mapa de México
f_mx = px.choropleth(data_frame=d_m, geojson=mx_region, locations='Estado', featureidkey='properties.name',
                     hover_name="Estado", hover_data=["Casos", "Defunciones"],
                     color='Casos', color_continuous_scale="Darkmint")
f_mx.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")
f_mx.update_layout(margin={"r":0,"t":0,"l":0,"b":10})
f_mx.update_traces(colorbar={"orientation":"h"})

# MAPA NUEVO LEON
#with open('municipal.json', 'r', encoding='utf-8') as f:
#    NLMap = json.load(f)

NLMap = requests.get("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/municipal.json").json()


d_NL = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NUEVOLEON.csv")

f_NL = px.choropleth(data_frame=d_NL, geojson=NLMap, locations='Municipio', featureidkey='properties.NOMBRE',
                     hover_name="Municipio", hover_data=["Casos", "Defunciones"],
                     color='Casos', color_continuous_scale="Darkmint")
f_NL.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

#Card sizes
cardsize_small = 11
cardsize_large = 6

dash.register_page(__name__, path="/casos-estado", title="UIMO - Casos por Estado", name="Casos por Estado")

layout = html.Div(children=[
    # JUMBOTRON
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Casos por Estado", className="display-2",
                        style={"color": "white", "background-color": "rgba(0,0,0,0.55)"}),
            ], width="auto", className="px-5 py-1"),
        ]),
        dbc.Row([
            dbc.Col([
                html.P("Cantidad de casos de infecciones nosocomiales registrados en los estados de México y los "
                       "municipios de Nuevo León",
                       className="lead", style={"color": "white", "background-color": "rgba(0,0,0,0.55)"})
            ], width="auto", className="px-5 py-1")
        ])
    ], className="py-3", style={"background-image": "url(/assets/banner4.png)", "background-size": "cover"},
        fluid=True),
    # Content
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Casos en México", className="card-title", style={"color": "black"}),
                        html.P("Por el momento solo contamos con casos de Nuevo León. Esperamos expandir nuestra base "
                               "de datos en el futuro."),
                        html.Hr(style={"border-color": "#446e9b"}),
                        dcc.Graph(
                            id="mapaMexico",
                            figure=f_mx),
                    ], className="pb-0"),
                ], color="primary", outline=True)
            ],width=11),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Casos en Nuevo León", className="card-title", style={"color": "black"}),
                        html.P("Por el momento solo contamos con casos de un municipio. Esperamos expandir nuestra base "
                               "de datos en el futuro."),
                        html.Hr(style={"border-color": "#446e9b"}),
                        dcc.Graph(
                            id="mapaNL",
                            figure=f_NL)
                    ], className="pb-0"),
                ], color="primary", outline=True)
            ], width=11, className="pt-3")
        ], justify="evenly", className="my-3")
    ], fluid=True)
])
