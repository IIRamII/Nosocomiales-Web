import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
], )
server = app.server

# Sección de hyperlinks para cada pagina
leNav = dbc.Nav([
    dbc.NavItem(dbc.NavLink("Inicio", href="/")),
    dbc.NavItem(dbc.NavLink("Casos por Clínica", href="/casos-clinica")),
    dbc.NavItem(dbc.NavLink("Resistencias", href="/resistencias")),
    dbc.NavItem(dbc.NavLink("Datos Demográficos", href="/datos-demograficos")),
    dbc.NavItem(dbc.NavLink("Casos por Estado", href="/casos-estado"))
], pills=True, navbar=True
)

# Barra superior de navegación. Logo + leNav
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
                    dbc.NavbarBrand("UIMO Stats", className="ms-3", href="/")
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
                    html.A(className="bi bi-github", style={"font-size": "2rem", "color": "white"},
                           href="https://github.com/IIRamII/Nosocomiales-Web/tree/main")
                ], width="auto"
            ),
            dbc.Col(
                [
                    html.A(className="bi bi-linkedin", style={"font-size": "2rem", "color": "white"})
                ], width="auto"
            ),
            dbc.Col(
                [
                    html.A(className="bi bi-instagram", style={"font-size": "2rem", "color": "white"},
                           href="https://www.instagram.com/dr.micobrio/")
                ], width="auto"
            ),
        ], justify="evenly")
    ], style={"display": "block"}),
    color="primary",
    dark=True
)

app.layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            leNavbar
        ])
    ], className="mx-0 gx-0"),

    dbc.Row([
        dbc.Col([
            dash.page_container
        ], width=12)
    ], className="mx-0 gx-0"),

    dbc.Row([
        dbc.Col([
            footer
        ])
    ], className="mt-5 mx-0 gx-0")
], fluid=True, className="px-0")


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
