"""This file is necessary for generating interactive maps using folium library."""
import sys
sys.path.insert(0,'/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/')
import os
from data_processing import polygons, read_map, load_data, data_transpose
import folium
import pandas as pd
import geopandas as gpd


#kenyan coordinates
#coordinates=[0.0236,37.9062]
#kc_latitude=coordinates[0]
#kc_longitude=coordinates[1]

def coordinates(latt=0.0236,long_it=37.9062):
    coordinates=latt,long_it
    return list(coordinates)

def map(lat,longit):
    KEN=folium.Map([lat,longit],zoom_start=5,tiles="Stamen Terrain")
    KEN.save('app/templates/my_map')
    
map(coordinates()[0],coordinates()[1])

print(coordinates()[0])



#Joining the two datasets from different sources
def join_pandas_geopandas(pandas_,geopandas_shape,on_=None,how_='right'):
    """Here we will link geopandas geodataframe with pandas data. 
    
    Specify pandas data, geopandas data, column and how to join i.e side(left or right(default value)) to join the two datasets as parameter. Returns geopandas dataframe"""
    kenya_gdf=read_map(geopandas_shape)
    kenya_pd=pd.DataFrame(kenya_gdf)
    pandas_=load_data(pandas_)
    appended_d=pd.merge(pandas_,kenya_pd,left_index=True,right_index=True)

    #joined_data=kenya_gdf.geometry.append(pandas_.squeeze())
    joined_data=gpd.GeoDataFrame(appended_d,crs="EPSG:4326")

    return joined_data
    
    
#generating maps
def generate_map(geojson_data,column_,clr,name_,lgnd_name):
    KEN=folium.Map(location=[0.0236,37.9062],zoom_start=6,tiles='Stamen Terrain')
    cpleth=folium.Choropleth(geo_data=geojson_data,data=geojson_data,columns=column_,key_on=('feature.properties.objectid'),fill_color=(clr),fill_opacity=0.8,nan_fill_opacity=0.4,line_opacity=0.5,name=name_,show=True,overlay=True,legend_name=lgnd_name,highlight=True,nan_fill_color='black',reset=True).add_to(KEN)
    
    #Hovering functionality
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}
    
    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(KEN)
    folium.TileLayer('cartodbpositron',name="light mode",control=True).add_to(KEN)

    # We add a layer controller. 
    folium.LayerControl(collapsed=False).add_to(KEN)
    
    children = list(geojson_data.drop(['objectid', 'geometry'], axis=1).columns)
    
    cpleth.geojson.add_child(folium.features.GeoJsonTooltip(children, labels=True))
    
    return KEN.save('app/templates/maps_templates/'+name_+'.html')
#=============simple tests=================   

dir=os.path.dirname("/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/open_source_data_values/folium_maps_data/")

#lst=['place_of_birth.geojson','core_healthworkforce.geojson','main_source_of_drinking_water.geojson']
loc_=read_map(os.path.join(dir,'main_source_of_drinking_water.geojson'))

generate_map(loc_,('objectid','Unsafe'),'PuBu','Drinking_Water',('Households Main Source of Drinking Water.'))