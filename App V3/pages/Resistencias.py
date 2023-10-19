import pandas as pd
import dash
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import plotly.express as px


#leyendas y margen
res_legend = dict(orientation="h", y=-0.4, yanchor="bottom", x=0.5, xanchor="center")
res_margin = dict(t=20)

# Gráfica de Resistencias de MOs
Res = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/Resistencias.csv")
f_Res = px.box(Res, y="Porcentaje de Resistencia", x="Clínica", color="MO", points="all")
f_Res.update_layout(legend=res_legend, margin=res_margin)

#Sexo
SexBar = px.histogram(Res, x="Sexo", color="Sexo")
#Edad
AgeViolin = px.violin(Res, y="Edad", color="Sexo", points="all")


dash.register_page(__name__, path="/resistencias")

layout = html.Div(children=[
    html.H1(children='Resistencias a antibióticos',style={'textAlign': 'center'}),

    html.Div(children=[
        html.H2(children="Porcentajes de Resistencia por Microorganismo", style={'textAlign': 'center'}),
        dcc.Graph(
            id="ResNL",
            figure=f_Res)
    ]),

    html.Div(children=[
        html.H2(children="Resistencia a Antibióticos", style={'textAlign': 'center'}),
        dcc.Dropdown(["Ampicilina", "Ampicilina.Sulbactam", "Piperacilina.Tazobactam", "Cefoxitina", "Cefalotina",
                      "Cefuroxima..oral.", "Cefuroxima..otra.",
                      "Cefotaxima", "Ceftazidima", "Ceftriaxona", "Cefepima", "Doripenem", "Ertapenem", "Imipenem",
                      "Meropenem", "Amicacina", "Gentamicina",
                      "Ciprofloxacino", "Tigeciclina", "Norfloxacino", "Nitrofurantoina", "Trimetoprima.Sulfametoxazol",
                      "Amoxicilina"], "Ampicilina",
                     id="Antibiotic_dropdown"),
        dcc.Graph(id="Antibiotic-Graph")
    ]),
])

@callback(
    Output('Antibiotic-Graph', 'figure'),
    Input('Antibiotic_dropdown', 'value'))
def update_antibiotic_graph(Antibiotico):
    fig_Antibiotic_Hist = px.histogram(Res, x=Antibiotico, color="MO")
    fig_Antibiotic_Hist.update_layout(legend=res_legend, margin=res_margin)
    return fig_Antibiotic_Hist
