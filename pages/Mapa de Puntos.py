from dash import html, dcc, callback, Input, Output
import pandas as pd
import dash
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Mapa de Puntos", title="Mapa de Puntos", )

# MO x Fechas
d_MOxF = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MOxFechas_Map.csv")
data_MOxF = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MOxFechas.csv")

#Mo sin Fechas
d_MOxA = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NLPointMap.csv")
data_MOxA = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NLPointMapData.csv")

layout = html.Div(children=[

    dbc.Row([
        dbc.Col(
            [
                html.H1(id="text-temp", style={"textAlign":"center"})
            ], width=12
        ),
        dbc.Col(
            [
                html.Label("Ordenar casos por:"),
            ], width="auto", className="gx-1"
        ),
        dbc.Col(
            [
                dcc.RadioItems(["Mes", "Año", "Todo"], "Mes", id="orden-temp", inline=True, labelClassName="px-1")
            ], width="auto", className="g-0"
        )
    ]),

    dbc.Row([
        dbc.Col(
            [
                dcc.Graph(
                    id="PointMapxFecha",
                    clickData={'points': [{'hovertext': 'Clínica 25'}]}
                )
            ], xs=12, sm=12, md=12, lg=6, xl=6, xxl=6, className="g-0"),

        dbc.Col(
            [
                dcc.Graph(id="Graph-MapDate")
            ], xs=12, sm=12, md=12, lg=6, xl=6, xxl=6, className="g-0")
    ]),

    dbc.Row([
       dbc.Col(
           [
                html.Label("Filtrar por Mes"),
                dcc.Slider(
                    d_MOxF['Mes'].min(),
                    d_MOxF['Mes'].max(),
                    step=None,
                    value=d_MOxF['Mes'].min(),
                    marks={
                        1: {"label": "Enero"},
                        2: {"label": "Febrero"},
                        3: {"label": "Marzo"},
                        4: {"label": "Abril"},
                        5: {"label": "Mayo"}
                    },
                    id='Map-Slider')
           ], id="Slider-Container", style={"display": "block"}
       )
    ])
],className="gap-0")

@callback(
    Output('text-temp', 'children'),
    Input('orden-temp', 'value'))
def update_map_header(selected_temp):
    if selected_temp == "Todo":
        return "Todos los casos"
    else:
        return ("Casos por " + selected_temp)


@callback(
    Output('PointMapxFecha', 'figure'),
    Input('Map-Slider', 'value'),
    Input('orden-temp', 'value'))
def update_date(selected_month, selected_temp):
    #Margenes del mapa (left, right, top, bottom)
    map_margin = dict(l=20, r=10, t=60, b=15)

    if selected_temp == "Mes":
        filtered_MOxF = d_MOxF[d_MOxF.Mes == selected_month]
        fig_MOxF = px.scatter_mapbox(filtered_MOxF, lat="lat", lon="lon", hover_name="Clínica",
                                 color="Casos", size="Casos", color_continuous_scale=px.colors.sequential.Viridis,
                                 size_max=15, zoom=10, mapbox_style="carto-positron", title='Mapa de Puntos')
        fig_MOxF.update_layout(margin=map_margin)
        return fig_MOxF
    else:
        fig_MOxF = px.scatter_mapbox(d_MOxA, lat="lat", lon="lon", hover_name="Clínica",
                                 color="Casos", size="Casos", color_continuous_scale=px.colors.sequential.Viridis,
                                 size_max=15, zoom=10, mapbox_style="carto-positron", title='Mapa de Puntos')
        fig_MOxF.update_layout(margin=map_margin)
        return fig_MOxF


@callback(
    Output('Graph-MapDate', 'figure'),
    Input('Map-Slider', 'value'),
    Input('PointMapxFecha', 'clickData'),
    Input('orden-temp', 'value'))
def update_pie_map(selected_month, clickData, selected_temp):
    #Graph_legend modifica donde aparecen las leyendas de los moos
    pie_legend = dict(
                title=None, orientation="h", y=-0.2, yanchor="bottom", x=0.5, xanchor="center"
            )
    sim=70
    pie_margin = dict(l=sim, r=sim, t=sim, b=sim)
    #Condicional de filtrado por Mes o por Año/Todos
    if selected_temp == "Mes":
        filtered_data_MOxF = data_MOxF[data_MOxF.Mes == selected_month]
        ffiltered_data_MOxF = filtered_data_MOxF[filtered_data_MOxF.Clínica == clickData["points"][0]["hovertext"]]
        fig_MOxF_pie = px.pie(ffiltered_data_MOxF, values='Casos', names='Microorganismo',
                              title=("Porcentaje de microorganismos de " + clickData["points"][0]["hovertext"]))
        fig_MOxF_pie.update_layout(legend=pie_legend, transition_duration=500, margin=pie_margin)
        return fig_MOxF_pie
    else:
        filtered_data_MOxA = data_MOxA[data_MOxA.Clínica == clickData["points"][0]["hovertext"]]
        fig_MOxF_pie = px.pie(filtered_data_MOxA, values='Casos', names='Microorganismo',
                              title=("Porcentaje de microorganismos de " + clickData["points"][0]["hovertext"]))
        fig_MOxF_pie.update_layout(legend=pie_legend, transition_duration=500, margin=pie_margin)
        return fig_MOxF_pie


@callback(
    Output('Slider-Container', 'style'),
    Input('orden-temp', 'value'))
def update_slider_test(selected_temp):
    if selected_temp == "Mes":
        return {"display": "block"}
    else:
        return {"display": "none"}
