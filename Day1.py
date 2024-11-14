import dash
import dash_leaflet as dl
from dash import html, dcc
import pandas as pd
from lat_lon_parser import parse

custom_icon = dict(
    iconUrl="https://leafletjs.com/examples/custom-icons/leaf-green.png",
    iconSize=[20, 50],
    iconAnchor=[22, 94],
    popupAnchor=[-3, -76],
)

df = pd.read_csv(
    "Local_Nature_Reserves_England_6224075941597999982.csv",
    usecols=(
        "LNR_NAME",
        "LONGITUDE",
        "LATITUDE",
    ),
)
# Inspect the data to ensure it has the necessary columns for latitude and longitude
df["longitude"] = df["LONGITUDE"].apply(parse)
df["latitude"] = df["LATITUDE"].apply(parse)
df.drop(columns=["LONGITUDE", "LATITUDE"], inplace=True)
df["size"] = 1

app = dash.Dash(__name__)


latitudes = df["latitude"].tolist()
longitudes = df["longitude"].tolist()
names = df["LNR_NAME"].tolist()


markers = [
    dl.Marker(
        position=[lat, lon],
        icon=custom_icon,
        children=[dl.Popup(html.Div([html.H1(name)]))],
    )
    for lat, lon, name in zip(latitudes, longitudes, names)
]

app.layout = html.Div(
    [
        dl.Map(
            center=[56, 10],
            zoom=4,
            children=[dl.TileLayer(), dl.LayerGroup(id="layer", children=markers)],
            style={"width": "1000px", "height": "500px"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
