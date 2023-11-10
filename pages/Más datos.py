import pandas as pd
import dash
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc

# Gráfica de Resistencias de MOs
Res = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/Resistencias.csv")

dash.register_page(
    __name__,
    path='/datos-demograficos',
    title='UIMO - Datos demográficos',
    name='Datos demográficos'
)

# Card sizes
cardsize_small = 11
cardsize_large = 6

layout = html.Div([
    # JUMBOTRON
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Datos Demográficos", className="display-2",
                        style={"color": "white", "background-color": "rgba(0,0,0,0.55)"}),
            ], width="auto", className="px-5 py-1"),
        ]),
        dbc.Row([
            dbc.Col([
                html.P("Datos demográficos de los pacientes con infecciones nosocomiales",
                       className="lead", style={"color": "white", "background-color": "rgba(0,0,0,0.55)"})
            ], width="auto", className="px-5 py-1")
        ])
    ], className="py-3", style={"background-image": "url(/assets/banner3.png)", "background-size": "cover"},
        fluid=True),
    # Content
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Sexo de los pacientes", className="card-title", style={"color": "black"}),
                        html.Hr(style={"border-color":"#446e9b"}),
                        dcc.Graph(id="Sex-Graph")
                    ], className="pb-0"),
                ], color="primary", outline=True),
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Edades de los pacientes", className="card-title", style={"color": "black"}),
                        html.Hr(style={"border-color": "#446e9b"}),
                        dcc.Graph(id="Age-Graph")
                    ], className="pb-0"),
                ], color="primary", outline=True)
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large)
        ], justify="evenly", className="my-3"),
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
                ], id="slider-data", style={"display": "none"}, className="pt-1"
            )
        ], justify="evenly")
    ], fluid=True)
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
def update_age_graph(lugar, filtro, selected_month):
    if filtro == "Mes":
        filtered_Age = Res[Res.Mes == selected_month]
        if lugar == "Ambos":
            fig_Age_Violin = px.violin(filtered_Age, y="Edad", color="Sexo", points="all")
            return fig_Age_Violin
        else:
            ffiltered_Age = filtered_Age[filtered_Age.Clínica == lugar]
            fig_Age_Violin = px.violin(ffiltered_Age, y="Edad", color="Sexo", points="all")
            return fig_Age_Violin

    else:
        if lugar == "Ambos":
            fig_Age_Violin = px.violin(Res, y="Edad", color="Sexo", points="all")
            return fig_Age_Violin
        else:
            filtered_Age = Res[Res.Clínica == lugar]
            fig_Age_Violin = px.violin(filtered_Age, y="Edad", color="Sexo", points="all")
            return fig_Age_Violin


@callback(
    Output('slider-data', 'style'),
    Input('F-temp', 'value'))
def update_slider_test(selected_temp):
    if selected_temp == "Mes":
        return {"display": "block"}
    else:
        return {"display": "none"}
