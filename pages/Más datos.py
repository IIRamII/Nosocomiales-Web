import pandas as pd
import dash
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc


# Gráfica de Resistencias de MOs
Res = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/Resistencias.csv")

dash.register_page(
    __name__,
    path='/masdatos',
    title='Más datos',
    name='Más datos'
)

layout = html.Div([
    dbc.Row([
        dbc.Col(
            [
                html.H1(children="Sexo y Edad de los pacientes", style={'textAlign': 'center'})
            ], width=12
        ),
        dbc.Col(
            [
                dcc.Graph(
                    id="Sex-Graph"
                )
            ],xs=12, sm=12, md=12, lg=6, xl=6, xxl=6
        ),
        dbc.Col(
            [
                dcc.Graph(
                    id="Age-Graph"
                )
            ],xs=12, sm=12, md=12, lg=6, xl=6, xxl=6
        )
    ]),
    dbc.Row([
        dbc.Col(
            [
                html.Label("Seleccione lugar de toma de muestra"),
                dcc.RadioItems(["Clínica 25", "Hospital 28", "Ambos"], "Ambos",
                               id="F-lugar")
            ], width=6
        ),
        dbc.Col(
            [
                html.Label("Filtrar datos por"),
                dcc.RadioItems(["Mes", "Año", "Todo"], "Todo",
                               id="F-temp")
            ], width=6
        ),
        dbc.Col(
            [
                html.Label("Seleccionar Mes"),
                dcc.Slider(
                    Res['Mes'].min(),
                    Res['Mes'].max(),
                    step=None,
                    value=Res['Mes'].min(),
                    marks={
                        1: {"label": "Enero"},
                        2: {"label": "Febrero"},
                        3: {"label": "Marzo"},
                        4: {"label": "Abril"},
                        5: {"label": "Mayo"}
                    },
                    id='Map-Slider-SA'
                )
            ]
        )
    ])
])

@callback(
    Output('Sex-Graph', 'figure'),
    Input('F-lugar', 'value'),
    Input('F-temp', 'value'),
    Input('Map-Slider-SA', 'value'))
def update_sex_graph(lugar, filtro, selected_month):
    if filtro == "Mes":
        filtered_Sex = Res[Res.Mes == selected_month]
        if lugar == "Ambos":
            fig_Sex_Bar = px.histogram(filtered_Sex, x="Sexo", color="Sexo")
            return fig_Sex_Bar
        else:
            ffiltered_Sex = filtered_Sex[filtered_Sex.Clínica == lugar]
            fig_Sex_Bar = px.histogram(ffiltered_Sex, x="Sexo", color="Sexo")
            return fig_Sex_Bar

    else:
        if lugar == "Ambos":
            fig_Sex_Bar = px.histogram(Res, x="Sexo", color="Sexo")
            return fig_Sex_Bar
        else:
            filtered_Sex = Res[Res.Clínica == lugar]
            fig_Sex_Bar = px.histogram(filtered_Sex, x="Sexo", color="Sexo")
            return fig_Sex_Bar


@callback(
    Output('Age-Graph', 'figure'),
    Input('F-lugar', 'value'),
    Input('F-temp', 'value'),
    Input('Map-Slider-SA', 'value'))
def update_sex_graph(lugar, filtro, selected_month):
    if filtro == "Mes":
        filtered_Age = Res[Res.Mes == selected_month]
        if lugar == "Ambos":
            fig_Age_Bar = px.violin(filtered_Age, y="Edad", color="Sexo", points="all")
            return fig_Age_Bar
        else:
            ffiltered_Age = filtered_Age[filtered_Age.Clínica == lugar]
            fig_Age_Bar = px.violin(ffiltered_Age, y="Edad", color="Sexo", points="all")
            return fig_Age_Bar

    else:
        if lugar == "Ambos":
            fig_Age_Bar = px.violin(Res, y="Edad", color="Sexo", points="all")
            return fig_Age_Bar
        else:
            filtered_Age = Res[Res.Clínica == lugar]
            fig_Age_Bar = px.histogram(filtered_Age, x="Sexo", color="Sexo")
            return fig_Age_Bar
