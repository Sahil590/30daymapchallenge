import json
import pandas as pd
import plotly.express as px

# Load the CSV data
df = pd.read_csv("./data/vehichle_data.csv")

# Aggregate the data by local authority
df_aggregated = (
    df.groupby(["Lower tier local authorities Code", "Lower tier local authorities"])
    .sum()
    .reset_index()
)

geojson = json.load(open("./data/Counties.geojson", "r"))
print(df_aggregated.head())

# Create the choropleth map
fig = px.choropleth_map(
    df_aggregated,
    geojson=geojson,
    locations="Lower tier local authorities Code",
    featureidkey="properties.ctyua_code",
    color="Observation",
    hover_name="Lower tier local authorities",
    title="Car or Van Availability by Local Authority",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()
