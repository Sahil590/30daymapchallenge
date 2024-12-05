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

# Load the GeoJSON data
geojson = json.load(open("./data/Counties.geojson", "r"))

# Extract all region codes from the GeoJSON file
all_regions = [
    feature["properties"]["ctyua_code"][0] for feature in geojson["features"]
]

# Create a DataFrame with all regions and a default value
all_regions_df = pd.DataFrame(
    {
        "Lower tier local authorities Code": all_regions,
        "Observation": 0,  # Default value for missing regions
    }
)


# Merge the aggregated data with the all regions DataFrame
df_merged = pd.merge(
    all_regions_df, df_aggregated, on="Lower tier local authorities Code", how="left"
)

df_merged["Observation"] = df_merged["Observation_y"].fillna(df_merged["Observation_x"])
df_merged = df_merged.drop(columns=["Observation_x", "Observation_y"])

df_merged.to_csv("./data/test.csv", index=False)
# Create the choropleth map
fig = px.choropleth_map(
    df_merged,
    geojson=geojson,
    locations="Lower tier local authorities Code",
    featureidkey="properties.ctyua_code",
    color="Observation",
    hover_name="Lower tier local authorities",
    title="Car or Van Availability by Local Authority",
    center={"lat": 54.5, "lon": -4},
    color_continuous_scale="GnBu",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()
