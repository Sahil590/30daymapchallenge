import dash
import pandas as pd
from dash import html, dcc
import plotly.graph_objects as go
from lat_lon_parser import parse

# Load and preprocess the data
df = pd.read_csv(
    "./data/Local_Nature_Reserves_England_6224075941597999982.csv",
    usecols=["LNR_NAME", "LONGITUDE", "LATITUDE"],
)
df["longitude"] = df["LONGITUDE"].apply(parse)
df["latitude"] = df["LATITUDE"].apply(parse)
df.drop(columns=["LONGITUDE", "LATITUDE"], inplace=True)

# Create the Plotly figure using go.Scattermapbox
fig = go.Figure(
    go.Scattermapbox(
        lat=df["latitude"],
        lon=df["longitude"],
        mode="markers",
        marker=go.scattermapbox.Marker(size=5, color="green"),
        text=df["LNR_NAME"],
        hoverinfo="text",
    )
)

fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        zoom=5,
        center=dict(lat=df["latitude"].mean(), lon=df["longitude"].mean()),
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    [dcc.Graph(figure=fig, style={"width": "100%", "height": "100%"})],
    style={"width": "100vw", "height": "100vh", "margin": "0", "padding": "0"},
)
if __name__ == "__main__":
    app.run_server(debug=True)
