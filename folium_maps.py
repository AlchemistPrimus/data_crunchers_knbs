# Importing the necessary libraries
import pandas as pd
import geopandas as gpd
import fiona
import matplotlib.pyplot as plt
import folium
from folium.plugins import StripePattern

# Loading the datasets
core_healthworkforce = gpd.read_file("iaos_data/folium_maps_data/core_healthworkforce.geojson")
govt_open_late_night = gpd.read_file("iaos_data/folium_maps_data/govt_open_late_night.geojson")
govt_open_public_holidays = gpd.read_file("iaos_data/folium_maps_data/govt_open_public_holidays.geojson")
govt_open_weekends = gpd.read_file("iaos_data/folium_maps_data/govt_open_weekends.geojson")
govt_open_whole_day = gpd.read_file('iaos_data/folium_maps_data/govt_open_whole_day.geojson')
nongovt_open_late_night = gpd.read_file("iaos_data/folium_maps_data/nongovt_open_late_night.geojson")
nongovt_open_public_holidays = gpd.read_file("iaos_data/folium_maps_data/nongovt_open_public_holidays.geojson")
nongovt_open_weekends = gpd.read_file("iaos_data/folium_maps_data/nongovt_open_weekends.geojson")
nongovt_open_whole_day = gpd.read_file('iaos_data/folium_maps_data/nongovt_open_whole_day.geojson')
homes_with_fixed_internet = gpd.read_file("iaos_data/folium_maps_data/homes_fixed_with_internet.geojson")
human_waste_disposal = gpd.read_file("iaos_data/folium_maps_data/human_waste_disposal.geojson")
internet_through_mobile = gpd.read_file("iaos_data/folium_maps_data/internet_through_mobile.geojson")
internet_users = gpd.read_file("iaos_data/folium_maps_data/internet_users.geojson")
main_source_of_drinking_water = gpd.read_file("iaos_data/folium_maps_data/main_source_of_drinking_water.geojson")
place_of_birth = gpd.read_file("iaos_data/folium_maps_data/place_of_birth.geojson")

# Naming the dataframes

def map_func(geojson_data, clmn, col, nm, lgd_name):
    # Creating Kenya map object
    KEN=folium.Map(location=[0.0236,37.9062], zoom_start=5)
    
    choropleth= folium.Choropleth(
        geo_data = geojson_data,
        data=geojson_data,
        columns= ('objectid', clmn),
        key_on=('feature.properties.objectid'),
        fill_color=(col),
        fill_opacity=0.8,
        nan_fill_opacity=0.4,
        line_opacity=0.5,
        name= nm,
        show=True,
        overlay=True,
        legend_name= lgd_name,
        highlight=True,
        nan_fill_color = "black",
        reset=True
    ).add_to(KEN)
    # Add hover functionality.
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}

    # Add dark and light mode. 
    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(KEN)
    folium.TileLayer('cartodbpositron',name="light mode",control=True).add_to(KEN)

    # We add a layer controller. 
    folium.LayerControl(collapsed=False).add_to(KEN)
    
    children = list(geojson_data.drop(['objectid', 'geometry'], axis=1).columns)
    
    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(children, labels=True))

    return KEN

# Example of using the function
map_func(place_of_birth, 'Non Health Facility', 'YlGnBu', 'Place_Of_Birth', 'Women who gave Birth in a Non-Health Facility (%)')    