from dash import html, dcc, callback, Input, Output
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Home", title="UIMO - Home")

#Cardsizes
homecard_small = 12
homecard_large_Img = 5
homecard_large_Txt = 7

cardsize_small = 10
cardsize_large = 5

card_y_sep = "g-4"

layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.Col([
                        html.Video(src="/assets/homebac-vid_A.mp4", autoPlay=True, loop=True, muted=True, className="img-fluid rounded")
                    ], xs=homecard_small, sm=homecard_small, md=homecard_small, lg=homecard_large_Img,
                        xl=homecard_large_Img, xxl=homecard_large_Img, className="g-0 d-flex"),
                    dbc.Col([
                        dbc.CardBody([
                            html.H2("Infecciones Nosocomiales", className="card-title", style={"color":"black"}),
                            html.H4("en Nuevo León", className="card-text", style={"color":"black"}),
                            html.P("Las infecciones nosocomiales son un problema de salud actual y se cree que serán la "
                                   "causa de la siguiente pandemia. Esta base de datos guarda registros de las infecciones "
                                   "nosocomiales en Nuevo León con el objetivo de monitorear las bacterias farmacorresistentes "
                                   "y posibles focos de infección.",
                                   className="card-text", style={"color":"black"}),
                            html.P("Todos nuestros gráficos son interactivos", style={"color":"black", "font-style":"italic"}),
                            dbc.CardLink("¿Qué es una Infección Nosocomial?", style={"color":"black"},
                                         href="https://www.saludsavia.com/contenidos-salud/enfermedades/infeccion-nosocomial")
                        ])
                    ], xs=homecard_small, sm=homecard_small, md=homecard_small, lg=homecard_large_Txt,
                        xl=homecard_large_Txt, xxl=homecard_large_Txt, className="g-0")
                ], className="g-0")
            ], outline=True, color="primary")
        ], width=11)
    ], justify="evenly", className="my-4 mx-0"),

    dbc.Row([
        dbc.Col([
            html.Hr(),
            html. H3("Registros y Estadísticas"),
            html.Hr(style={"margin-bottom":"0"}),
        ], width=11)
    ], justify="evenly", className="my-1 mx-0"),

    dbc.Row([
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/map-transformed.jpeg", style={"opacity": 0.6}, className="rounded"),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Casos por Clínica", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
            href="/casos-clinica")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        ),
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/home-resistance.png", bottom=True, style={"opacity": 0.6}, className="rounded"),
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
                    dbc.CardImg(src="/assets/demodemo.png", bottom=True, style={"opacity": 0.6}, className="rounded"),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Datos Demográficos", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
                href="/datos-demograficos")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        ),
        dbc.Col(
            [html.A(
                dbc.Card([
                    dbc.CardImg(src="/assets/home-map.png", bottom=True, style={"opacity": 0.6}, className="rounded"),
                    dbc.CardImgOverlay(
                        dbc.CardBody([
                            html.H3("Casos por Estado y Municipio", className="card-title")
                        ])
                    )
                ], color="primary", inverse=True),
                href="/casos-estado")
            ], xs=cardsize_small, sm=cardsize_small, md=cardsize_small, lg=cardsize_large, xl=cardsize_large, xxl=cardsize_large,
            className=card_y_sep
        )
    ], justify="evenly")
], fluid=True)
