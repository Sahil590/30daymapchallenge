import dash
import dash_leaflet as dl
from dash import html
import json

# Load GeoJSON data
with open("./data/Submarine_Cables_and_Terminals__2018_.geojson") as f:
    geojson_data = json.load(f)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dl.Map(
            center=[20, 0],
            zoom=2,
            children=[
                dl.TileLayer(),
                dl.GeoJSON(
                    data=geojson_data,
                    style={"color": "#181818", "weight": 1},
                ),
            ],
            style={"width": "100%", "height": "100vh"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
