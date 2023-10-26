from dash import html, dcc, callback, Input, Output
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/home", name="Home", title="Home")

cardsize_small = {"size":10, "offset":1}
cardsize_large = {"size":4, "offset":1}


layout = html.Div([
    dbc.Row([
        dbc.Col(
            [
                html.H1("Infecciones Nosocomiales", style={"textAlign":"center"}),#Buscar como eliminar el borde inferior
                html.H4("en Nuevo León", style={"textAlign":"center"})
            ], className="g-3"
        )
    ]),

    dbc.Row([
        dbc.Col(
            [
                dbc.Card([
                    dbc.CardBody(html.H3("Mapa de Puntos", className="card-title")),
                    dbc.CardImg(src="/assets/Mapa.png", bottom=True)
                ]) #Buscar como añadir marcos o bordes a la card
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large
        ),
        dbc.Col(
            [
                dbc.Card([
                    dbc.CardBody(html.H3("Mapa de Puntos", className="card-title")),
                    dbc.CardImg(src="/assets/Mapa.png", bottom=True)
                ])  # Buscar como añadir marcos o bordes a la card
            ], xs=12, sm=12, md=12, lg=6, xl=6, xxl=6,
        ),
        dbc.Col(
            [
                dbc.Card([
                    dbc.CardBody(html.H3("Mapa de Puntos", className="card-title")),
                    dbc.CardImg(src="/assets/Mapa.png", bottom=True)
                ])  # Buscar como añadir marcos o bordes a la card
            ], xs=12, sm=12, md=12, lg=6, xl=6, xxl=6
        ),
        dbc.Col(
            [
                dbc.Card([
                    dbc.CardBody(html.H3("Mapa de Puntos", className="card-title")),
                    dbc.CardImg(src="/assets/Mapa.png", bottom=True)
                ])  # Buscar como añadir marcos o bordes a la card
            ], xs=12, sm=12, md=12, lg=6, xl=6, xxl=6
        ),
    ])
])
