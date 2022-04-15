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
    
    Specify pandas data, geopandas data, column and how to join i.e side(left or right(default value)) to join the two datasets as parameter. Returns geojson dataframe"""
    kenya_gdf=read_map(geopandas_shape)
    kenya_pd=pd.DataFrame(kenya_gdf)
    pandas_=load_data(pandas_)
    appended_d=pd.merge(pandas_,kenya_pd,left_index=True,right_index=True)

    #joined_data=kenya_gdf.geometry.append(pandas_.squeeze())
    joined_data=gpd.GeoDataFrame(appended_d,crs="EPSG:4326")

    return joined_data
    
    
#generating maps
def generate_map(pandas_data,geopandas_shape,name_,column_lst,coordinates_lst,fields_,aliases_,lgnd_name,fill_clr="Blues"):
    """Returns the map to display the visualization.
    
    parameters
    pandas data and geopandas shape file
    column_n: name of the column to join them with.
    name_:name of the map to generate
    column_lst: column data to include in the map
    cordinates_lst: list of the coordinates(must be two items)
    fields_ and aliases_ are entered as per folium.features.GeojsonTooltip
    lgnd_name: takes the legend name
    fill_clr: takes the color of the fill, can be list but set to RdYIGn by default.
    """
    if not (isinstance(coordinates_lst,list) and isinstance(fields_,list) and isinstance(aliases_,list)):
        return "column_lst,fields_,aliases_, cordinates(list that must contain only two items of int or float types), i.e arguments 4th, 5th, 6th and 7th should be lists"
    #pandas_transp=data_transpose(pandas_data)
    gdf=join_pandas_geopandas(pandas_data,geopandas_shape)
    coord=polygons(coordinates_lst)
    
    tooltip=folium.features.GeoJsonTooltip(fields=fields_,aliases=aliases_,labels=True,stick=False)
    map_=folium.Map(location=coord,tiles="Stamen Terrain",zoom_start=5)
    cpleth=folium.Choropleth(gdf,data=gdf,key_on=('features.properties.County'),columns=column_lst,fill_color=fill_clr,legend_name=lgnd_name,name=name_)

    cpleth.geojson.add_child(tooltip)
    cpleth.add_to(map_)
    folium.LayerControl().add_to(map_)
    
    return map_.save(name_+".html")
 
 
#=============simple tests=================   

dir=os.path.dirname("/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/open_source_data_values/")

csv_files=['County.shp','2009_County_Population.csv','2013_health_staff_per_10000.csv','2018_2019_health_staff_per_10000.csv','2019_County_Population.csv','list_of_community_health_units.csv','list_of_hospitals_and_number_of_beds.csv','list_of_pharmacies.csv','number_of_hospital_beds.csv']

def file_finder(dir,csv_files):
    for i in csv_files:
        loc=os.path.join(dir,i)
        d=load_data(loc)
        return d.head(5)
    
#print(file_finder(dir,csv_files))
gdf=join_pandas_geopandas(os.path.join(dir,csv_files[4]),os.path.join(dir,csv_files[0]))
#gdf=read_map(os.path.join(dir,csv_files[0]))
print(gdf.head(5))

print(generate_map(os.path.join(dir,csv_files[2]),os.path.join(dir,csv_files[0]),"Core Health",['County','Total'],[0.0236,37.9062],['County','Total'],['County','Total'],"County Population"))
