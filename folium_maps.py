# Importing the necessary libraries
import pandas as pd
import geopandas as gpd
import fiona
import matplotlib.pyplot as plt
import folium
import os
from folium.plugins import StripePattern

dir=os.path.dirname("/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/open_source_data_values/folium_maps_data/")

# Loading the datasets
core_healthworkforce = gpd.read_file(os.path.join(dir,"core_healthworkforce.geojson"))
govt_open_late_night = gpd.read_file(os.path.join(dir,"govt_open_late_night.geojson"))
govt_open_public_holidays = gpd.read_file(os.path.join(dir,"govt_open_public_holidays.geojson"))
govt_open_weekends = gpd.read_file(os.path.join(dir,"govt_open_weekends.geojson"))
govt_open_whole_day = gpd.read_file(os.path.join(dir,'govt_open_whole_day.geojson'))
nongovt_open_late_night = gpd.read_file(os.path.join(dir,"nongovt_open_late_night.geojson"))
nongovt_open_public_holidays = gpd.read_file(os.path.join(dir,"nongovt_open_public_holidays.geojson"))
nongovt_open_weekends = gpd.read_file(os.path.join(dir,"nongovt_open_weekends.geojson"))
nongovt_open_whole_day = gpd.read_file(os.path.join(dir,'nongovt_open_whole_day.geojson'))
homes_with_fixed_internet = gpd.read_file(os.path.join(dir,"homes_fixed_with_internet.geojson"))
human_waste_disposal = gpd.read_file(os.path.join(dir,"human_waste_disposal.geojson"))
internet_through_mobile = gpd.read_file(os.path.join(dir,"internet_through_mobile.geojson"))
internet_users = gpd.read_file(os.path.join(dir,"internet_users.geojson"))

main_source_of_drinking_water = gpd.read_file(os.path.join(dir,"main_source_of_drinking_water.geojson"))
place_of_birth = gpd.read_file(os.path.join(dir,"place_of_birth.geojson"))

# Naming the dataframes

core_healthworkforce.name = 'core_healthworkforce'
govt_open_late_night.name = 'govt_open_late_night'
govt_open_public_holidays.name = 'govt_open_public_holidays'
govt_open_weekends.name = 'govt_open_weekends'
govt_open_whole_day.name = 'govt_open_whole_day'
nongovt_open_late_night.name = 'nongovt_open_late_night'
nongovt_open_public_holidays.name = 'nongovt_open_public_holidays'
nongovt_open_weekends.name = 'nongovt_open_weekends'
nongovt_open_whole_day.name = 'nongovt_open_whole_day'
homes_with_fixed_internet.name = 'homes_with_fixed_internet'
human_waste_disposal.name = 'human_waste_disposal'
internet_through_mobile.name = 'internet_through_mobile'
internet_users.name = 'internet_users'
main_source_of_drinking_water.name = 'main_source_of_drinking_water'
place_of_birth.name = 'place_of_birth'

# The mapping function

def mapping_func(geojson_data):

    #creating Kenya map object
    KEN=folium.Map(location=[0.0236,37.9062], zoom_start=7)
    
    if geojson_data.name == 'core_healthworkforce':
        clmn = ('objectid','\% change')
        col = 'Greys'
        nm = 'Healthworkforce'
        lgd_name = ('Core Healthworkforce')
    elif geojson_data.name == 'govt_open_late_night':
        clmn = ('objectid','No')
        col = 'Purples'
        nm = 'Govt_Open_Late_Night'
        lgd_name = ('Government Hospitals Open Late Night')
    elif geojson_data.name == 'govt_open_public_holidays':
        clmn = ('objectid','No')
        col = 'Blues'
        nm = 'Govt_Open_Public_Holidays'
        lgd_name = ('Government Hospitals Open on Public Holidays')
    elif geojson_data.name == 'govt_open_weekends':
        clmn = ('objectid','No')
        col = 'Greens'
        nm = 'Govt_Open_Weekends'
        lgd_name = ('Government Hospitals Open on Weekends')
    elif geojson_data.name == 'govt_open_whole_day':
        clmn = ('objectid','No')
        col = 'Oranges'
        nm = 'Govt_Open_Whole_Day'
        lgd_name = ('Government Hospitals Open Whole Day')
    elif geojson_data.name == 'nongovt_open_late_night':
        clmn = ('objectid','No')
        col = 'Reds'
        nm = 'Nongovt_Open_Late_Night'
        lgd_name = ('Non-Governmental Hospitals Open Late Night')
    elif geojson_data.name == 'nongovt_open_public_holidays':
        clmn = ('objectid','No')
        col = 'YlOrBr'
        nm = 'Nongovt_Open_Public_Holidays'
        lgd_name = ('Non-Governmental Hospitals Open on Public Holidays')
    elif geojson_data.name == 'nongovt_open_weekends':
        clmn = ('objectid','No')
        col = 'YlOrRd'
        nm = 'Nongovt_Open_Weekends'
        lgd_name = ('Non-Governmental Hospitals Open on Weekends')
    elif geojson_data.name == 'nongovt_open_whole_day':
        clmn = ('objectid','No')
        col = 'OrRd'
        nm = 'Nongovt_Open_Whole_Day'
        lgd_name = ('Non-Governmental Hospitals Open Whole Day')
    elif geojson_data.name == 'homes_with_fixed_internet':
        clmn = ('objectid','No')
        col = 'PuRd'
        nm = 'Fixed_Internet'
        lgd_name = ('Households with Fixed Internet at Home')
    elif geojson_data.name == 'human_waste_disposal':
        clmn = ('objectid','Improper')
        col = 'RdPu'
        nm = 'Human_Waste_Disposal'
        lgd_name = ('Households Modes of Human Waste Disposal')
    elif geojson_data.name == 'internet_through_mobile':
        clmn = ('objectid','No')
        col = 'BuPu'
        nm = 'Internet_Through_Mobile'
        lgd_name = ('Households that Accessed Internet Through Mobile')
    elif geojson_data.name == 'internet_users':
        clmn = ('objectid','No')
        col = 'GnBu'
        nm = 'Internet_Users'
        lgd_name = ('Persons that Accessed Internet in the Last Three Months')
    elif geojson_data.name == 'main_source_of_drinking_water':
        clmn = ('objectid','Unsafe')
        col = 'PuBu'
        nm = 'Drinking_Water'
        lgd_name = ('Households Main Source of Drinking Water')
    else:
        clmn = ('objectid','Non Health Facility')
        col = 'YlGnBu'
        nm = 'Place_Of_Birth'
        lgd_name = ('Women who gave Birth in a Non-Health Facility')
        
    choropleth= folium.Choropleth(
        geo_data = geojson_data,
        data=geojson_data,
        columns= clmn,
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

    return KEN.save('app/templates/maps_templates/'+nm+'.html')

#lst=['core_healthworkforce.geojson','govt_open_late_night.geojson','govt_open_public_holidays.geojson','govt_open_weekends.geojson','govt_open_whole_day.geojson','homes_fixed_with_internet.geojson','human_waste_disposal.geojson','internet_through_mobile.geojson','internet_users.geojson','main_source_of_drinking_water.geojson','nongovt_open_late_night.geojson','non_govt_open_public_holidays.geojson','nongovt_open_weekends.geojson','non_govt_open_whole_day.geojson','place_of_birth.geojson']

loc=os.path.join(dir,'core_healthworkforce.geojson')

file_=gpd.read_file(loc)  
mapping_func(file_)
