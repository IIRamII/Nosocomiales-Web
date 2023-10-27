from dash import html, dcc, callback, Input, Output
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/mapapuntos", name="Home", title="Home")

cardsize_small = 10
cardsize_large = 5

card_y_sep = "g-4"

layout = html.Div([
    dbc.Row([
        dbc.Col(
            [
                html.H1("Infecciones Nosocomiales", style={"textAlign":"center"}, className="my-0"),#Buscar como eliminar el borde inferior
                html.H4("en Nuevo León", style={"textAlign":"center"})
            ], className="g-3"
        )
    ]),

    dbc.Row([
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/map-transformed.jpeg", bottom=True, style={"opacity": 0.6}),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Casos por Clínica", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
            href="/mapapuntos")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        ),
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/resistencias.jpg", bottom=True, style={"opacity": 0.6}),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Resistencia a Antibióticos", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
                href="/resistencias")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        ),
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/demografia.png", bottom=True, style={"opacity": 0.6}),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Datos Demográficos", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
                href="/masdatos")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        ),
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/mexico.jpg", bottom=True, style={"opacity": 0.6}),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Casos por Estado y Municipio", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
                href="/mapamexico")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        )
    ], justify="evenly")
])
