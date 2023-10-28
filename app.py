import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
], )
server = app.server

#Sección de hyperlinks para cada pagina
leNav = dbc.Nav([
    dbc.NavItem(dbc.NavLink("Inicio", href="/")),
    dbc.NavItem(dbc.NavLink("Mapa de Puntos", href="/mapapuntos")),
    dbc.NavItem(dbc.NavLink("Resistencias", href="/resistencias")),
    dbc.NavItem(dbc.NavLink("Más datos", href="/masdatos")),
    dbc.NavItem(dbc.NavLink("Mapa México", href="/mapamexico"))
], pills=True, navbar=True
)

#Barra superior de navegación. Logo + leNav
leNavbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.Col(
                    [
                        html.Img(src="assets/UIMO.png", height="60px")
                    ],
                    width="auto", align="center"
                ),
                dbc.Col([
                    dbc.NavbarBrand("Nosocomiales UIMO", className="ms-3", href="/")
                ], width="auto", align="center"
                ),
                dbc.Col([
                    dbc.Collapse(
                        leNav,
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True
                    )
                ], width="auto", className="g-0")

            ],
                align="center", className="g-0"
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
)

footer = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                [
                    html.A(className="bi bi-github", style={"font-size":"2rem","color":"white"},
                           href="https://github.com/IIRamII/Nosocomiales-Web/tree/main")
                ], width="auto"
            ),
            dbc.Col(
                [
                    html.A(className="bi bi-linkedin", style={"font-size":"2rem","color":"white"})
                ], width="auto"
            ),
            dbc.Col(
                [
                    html.A(className="bi bi-instagram", style={"font-size":"2rem","color":"white"},
                           href="https://www.instagram.com/dr.micobrio/")
                ], width="auto"
            ),
        ], justify="evenly")
    ], style={"display":"block"}),
    color="primary",
    dark=True
)

app.layout = dbc.Container([

    dbc.Row([leNavbar]),

    dbc.Row(
        [
            dbc.Col(
                [
                    dash.page_container
                ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
        ]
    ),

    dbc.Row(
        [footer], className="mt-5"
    )
], fluid=True)

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run(debug=False)
