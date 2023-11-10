import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc


# leyendas y margen de graficas
res_legend = dict(orientation="h", y=-0.4, yanchor="bottom", x=0.5, xanchor="center")
res_margin = dict(t=20)

# Gráfica de Resistencias de MOs
Res = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/Resistencias.csv")
f_Res = px.box(Res, y="Porcentaje de Resistencia", x="Clínica", color="MO", points="all")
f_Res.update_layout(legend=res_legend, margin=res_margin)

# Sexo
SexBar = px.histogram(Res, x="Sexo", color="Sexo")
# Edad
AgeViolin = px.violin(Res, y="Edad", color="Sexo", points="all")

# Card sizes
cardsize = 11


# Dropdown Antibiotics Options
antibioticos = ["Ampicilina", "Ampicilina.Sulbactam", "Piperacilina.Tazobactam", "Cefoxitina", "Cefalotina",
                "Cefuroxima..oral.", "Cefuroxima..otra.", "Cefotaxima", "Ceftazidima", "Ceftriaxona", "Cefepima",
                "Doripenem", "Ertapenem", "Imipenem", "Meropenem", "Amicacina", "Gentamicina", "Ciprofloxacino",
                "Tigeciclina", "Norfloxacino", "Nitrofurantoina", "Trimetoprima.Sulfametoxazol", "Amoxicilina"]

dash.register_page(__name__, path="/resistencias", name="Resistencias", title="UIMO - Resistencias")

layout = html.Div(children=[
    # JUMBOTRON
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Resistencia a Antibióticos", className="display-2",
                        style={"color": "white", "background-color": "rgba(0,0,0,0.55)"}),
            ], width="auto", className="px-5 py-1"),
        ]),
        dbc.Row([
            dbc.Col([
                html.P("Distribución de porcentajes de resistencia ante varios antibióticos y Conteo de bacterias "
                       "resistentes y susceptibles",
                       className="lead", style={"color": "white", "background-color": "rgba(0,0,0,0.55)"})
            ], width="auto", className="px-5 py-1")
        ])
    ], className="py-3", style={"background-image": "url(/assets/banner2.png)", "background-size": "cover"},
        fluid=True),
    # Content
    dbc.Container([
        dbc.Row([
           dbc.Col([
               dbc.Card([
                   dbc.CardBody([
                       html.H4("Porcentaje de Resistencia por Bacteria", className="card-title", style={"color":"black"}),
                       html.P("Se realizaron varias pruebas de resistencia y se calculó el porcentaje de resistencia "
                              "en base a las pruebas totales. Cada punto representa una muestra."),
                       html.Hr(style={"border-color":"#446e9b"}),
                   ], className="pb-0"),
                   dcc.Graph(
                       id="ResNL",
                       figure=f_Res)
               ], color="primary", outline=True)
           ], width=cardsize)
        ], justify="center", className="my-3"),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Resistencia por Antibiótico", className="card-title", style={"color": "black"}),
                        html.P("Antibióticos que fueron utilizados para las purebas de resistencia."),
                        html.Hr(style={"border-color":"#446e9b"}),
                        dbc.Row([
                            dbc.Col([
                                html.P("Seleccione un Antibiótico:", className="mt-1")
                            ], width="auto"),
                            dbc.Col([
                                dcc.Dropdown(
                                    antibioticos,
                                    "Ampicilina",
                                    id="Antibiotic_dropdown")
                            ], xs=12, sm=12, md=12, lg=9, xl=9, xxl=10)
                        ])
                    ], className="pb-0"),
                    dcc.Graph(id="Antibiotic-Graph")
                ], color="primary", outline=True)
            ], width=cardsize)
        ], justify="center", className="mt-2")
    ], fluid=True)
])


@callback(
    Output('Antibiotic-Graph', 'figure'),
    Input('Antibiotic_dropdown', 'value'))
def update_antibiotic_graph(antibiotico):
    fig_Antibiotic_Hist = px.histogram(Res, x=antibiotico, color="MO")
    fig_Antibiotic_Hist.update_layout(legend=res_legend, margin=res_margin)
    return fig_Antibiotic_Hist
