from subprocess import call
import dash

dash.register_page(__name__) # adding path makes it the home page

#additional libararies
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np

np.random.seed(2020)

layout  = html.Div(
    [
        dcc.Graph(id = "histograms-graph"),
        dcc.Slider(
            id = "histograms-mean", min = -3, max = 3, value=0, marks = {-3:"-3", 3:"3"}
        ),
        html.P("Standard Deviation: "),
        dcc.Slider("histograms-std", min=1, max = 3, value=1, marks = {1:"1", 3:"3"}),
    ]
)

@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
)

def display_color(mean, std):
    data = np.random.normal(mean, std, size = 500)
    fig = px.histogram(data, nbins=30, range_x=([-10, 10]))
    fig.update_layout(showlegend=False)
    return fig
    