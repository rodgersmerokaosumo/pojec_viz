import dash
import dash_app as dl
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY]
)

for x in dash.page_registry.values():
    print(x)

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href = page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "page.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    class_name="mb-2"
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)