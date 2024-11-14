import dash
import dash_leaflet as dl
from dash import html
import json

app = dash.Dash(__name__)

# Load the GeoJSON data
with open("Submarine_Cables_and_Terminals__2018_.geojson") as f:
    data = json.load(f)

app.layout = html.Div(
    [
        dl.Map(
            [
                dl.TileLayer(),
                dl.GeoJSON(
                    url="/Submarine_Cables_and_Terminals__2018_.geojson",
                    zoomToBounds=True,
                ),
            ],
            style={"width": "100%", "height": "600px"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
