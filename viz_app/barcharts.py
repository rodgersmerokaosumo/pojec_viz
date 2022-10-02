from subprocess import call
import dash

dash.register_page(__name__) # adding path makes it the home page

#additional libararies
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [
        dcc.Dropdown(
            id = "dropdown",
            value = days[0]
            clearable = False,
            style = {"width":"50%"}
        ),
        dcc.Graph(id = "bar-chart"),
    ]
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x = "sex", y = "totalbill", color="smoker", barmode="group", template="simple_white")
    return fig

