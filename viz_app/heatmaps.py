import dash

dash.register_page(__name__, path="/") # adding path makes it the home page

#additional libararies
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.medals_wide(indexed=True)

layout = html.Div(
    [
        html.P("Medala Included: "),
        dcc.Checklist(
            id = "heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.to_list(),
        )
        dcc.Graph(id = "heatmaps-graph")
    ]
)

@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
def filter_heatmaps(cols):
    fig  = px.imshow(df[cols])
    return fig
