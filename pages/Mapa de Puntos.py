from dash import html, dcc, callback, Input, Output
import pandas as pd
import dash
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/casos-clinica", name="Casos por Clínica", title="UIMO - Casos por Clínica")

# MO x Fechas
d_MOxF = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MOxFechas_Map.csv")
data_MOxF = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MOxFechas.csv")

#Mo sin Fechas
d_MOxA = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NLPointMap.csv")
data_MOxA = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NLPointMapData.csv")

#CardSizes
cardsize_small = 11
cardsize_large = 6

layout = html.Div([
    #JUMBOTRON
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Casos por Clínica", className="display-2",
                        style={"color":"white", "background-color":"rgba(0,0,0,0.55)"}),
            ], width="auto", className="px-5 py-1"),
        ]),
        dbc.Row([
            dbc.Col([
                html.P("Cantidad de casos de infecciones nosocomiales registrados en clínicas del IMSS",
                       className="lead", style={"color": "white", "background-color":"rgba(0,0,0,0.55)"})
            ], width="auto", className="px-5 py-1")
        ])
    ], className="py-3", style={"background-image": "url(/assets/banner1.png)", "background-size": "cover"}, fluid=True),

    #Content
    dbc.Container([
        #Radio Selection
        dbc.Row([
            dbc.Col(
                [
                    html.Label("Ordenar casos por:"),
                ], width="auto", className="gx-2"
            ),
            dbc.Col(
                [
                    dcc.RadioItems(["Mes", "Año", "Todo"], "Mes", id="orden-temp", inline=True, labelClassName="px-1")
                ], width="auto", className="g-0"
            )
        ], className="m-2 mt-3 mb-1"),
        #Graph Cards
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Casos de la Clínica 25 y Hospital 28", className="card-title", style={"color":"black"}),
                        html.Hr(style={"border-color":"#446e9b"})
                    ], className="pb-0"),
                    dcc.Graph(
                        id="PointMapxFecha",
                        clickData={'points': [{'hovertext': 'Clínica 25'}]}
                    )
                ], color="primary", outline=True)
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className="my-2"),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4(id="pie-header", className="card-title", style={"color":"black"}),
                        html.Hr(style={"border-color":"#446e9b"})
                    ], className="pb-0"),
                    dcc.Graph(id="Graph-MapDate")
                ], color="primary", outline=True)
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className="my-2")
        ], justify="evenly"),

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
    ], fluid=True)
])

#@callback(
#    Output('text-temp', 'children'),
#    Input('orden-temp', 'value'))
#def update_map_header(selected_temp):
#    if selected_temp == "T#odo":
#        return "Todos los casos"
#    else:
#        return ("Casos por " + selected_temp)


@callback(
    Output('PointMapxFecha', 'figure'),
    Input('Map-Slider', 'value'),
    Input('orden-temp', 'value'))
def update_date(selected_month, selected_temp):
    #Margenes del mapa (left, right, top, bottom)
    map_margin = dict(l=20, r=20, t=0, b=20)

    #Hoverdata
    map_hover_data = {
        "lat":False,
        "lon":False,
        "Casos":True
    }

    if selected_temp == "Mes":
        filtered_MOxF = d_MOxF[d_MOxF.Mes == selected_month]
        fig_MOxF = px.scatter_mapbox(filtered_MOxF, lat="lat", lon="lon", hover_name="Clínica",
                                     color="Casos", size="Casos", color_continuous_scale=px.colors.sequential.Viridis,
                                     size_max=15, zoom=10, mapbox_style="carto-positron", hover_data=map_hover_data)
        fig_MOxF.update_layout(margin=map_margin)
        return fig_MOxF
    else:
        fig_MOxF = px.scatter_mapbox(d_MOxA, lat="lat", lon="lon", hover_name="Clínica",
                                     color="Casos", size="Casos", color_continuous_scale=px.colors.sequential.Viridis,
                                     size_max=15, zoom=10, mapbox_style="carto-positron", hover_data=map_hover_data)
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
    sim=50

    #Color de microorganismos
    color_MOOs = {
        "Klebsiella pneumoniae":"#FF86E4",
        "Pseudomonas aeruginosa":"#FFA646",
        "Acinetobacter baumannii":"#8761FF"
    }

    color_MOOs2 = {
        "Klebsiella pneumoniae":"rgb(55,126,184)",
        "Pseudomonas aeruginosa":"rgb(77,175,74)",
        "Acinetobacter baumannii":"rgb(152,78,163)"
    }

    pie_margin = dict(l=sim, r=sim, t=sim, b=sim)
    #Condicional de filtrado por Mes o por Año/Todos
    if selected_temp == "Mes":
        filtered_data_MOxF = data_MOxF[data_MOxF.Mes == selected_month]
        ffiltered_data_MOxF = filtered_data_MOxF[filtered_data_MOxF.Clínica == clickData["points"][0]["hovertext"]]
        fig_MOxF_pie = px.pie(ffiltered_data_MOxF, values='Casos', names='Microorganismo')
                              #color_discrete_map=color_MOOs2, color="Microorganismo")
        fig_MOxF_pie.update_layout(legend=pie_legend, transition_duration=500, margin=pie_margin)
        return fig_MOxF_pie
    else:
        filtered_data_MOxA = data_MOxA[data_MOxA.Clínica == clickData["points"][0]["hovertext"]]
        fig_MOxF_pie = px.pie(filtered_data_MOxA, values='Casos', names='Microorganismo')
        fig_MOxF_pie.update_layout(legend=pie_legend, transition_duration=500, margin=pie_margin)
        return fig_MOxF_pie

@callback(
    Output("pie-header", "children"),
    Input('PointMapxFecha', 'clickData'))
def update_pie_header(clickData):
    pie_header = "Prevalencias de Microorganismos en " + clickData["points"][0]["hovertext"]
    return pie_header


@callback(
    Output('Slider-Container', 'style'),
    Input('orden-temp', 'value'))
def update_slider_test(selected_temp):
    if selected_temp == "Mes":
        return {"display": "block"}
    else:
        return {"display": "none"}
