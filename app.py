
import streamlit as st
import geopandas as gpd
from indicator_engine import run_indicators
from streamlit_folium import st_folium
import folium
import os

st.set_page_config(layout="wide")
st.title("Investigation Coverage Map – CPT & MASW")

dataset_option = st.radio("Select Dataset", ["CPT (Points)", "MASW (Lines)"])

if dataset_option == "CPT (Points)":
    path = os.path.join("data", "ind_pc.shp")
    dataset_type = "CPT"
else:
    path = os.path.join("data", "ind_ln.shp")
    dataset_type = "MASW"

gdf = gpd.read_file(path)
gdf = run_indicators(gdf, dataset_type)
gdf = gdf.to_crs(epsg=4326)

# Set up the map
centroid = gdf.geometry.unary_union.centroid
m = folium.Map(location=[centroid.y, centroid.x], zoom_start=13, tiles="CartoDB positron")

folium.GeoJson(
    gdf,
    tooltip=folium.GeoJsonTooltip(fields=gdf.columns.drop("geometry").tolist()),
    name="Survey Data"
).add_to(m)

st.subheader(f"Map – {dataset_type} Coverage")
st_folium(m, width=1000, height=600)
