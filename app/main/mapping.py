"""This file is necessary for generating interactive maps using folium library."""
import sys
sys.path.insert(0,'/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/')
from data_processing import polygons, read_map, load_data
import folium


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
def join_pandas_geopandas(pandas_,geopandas_shape):
    """Here we will link geopandas geodataframe with pandas data"""
    gdf=read_map(geopandas_shape)
    pandas_=load_data(pandas_)
    pass

#generating maps
def generate_map(pandas_data,geopandas_shape,name_,column_lst,cordinates_lst,fields_,aliases_,lgnd_name,fill_clr="RdYIGn",):
    if not (isinstance(column_lst,list) and isinstance(coordinates,list) and isinstance(fields_,list) and isinstance(aliases_,list)):
        return "column_lst,fields_,aliases_, cordinates(list that must contain only two items of int or float types), i.e arguments 4th, 5th, 6th and 7th should be lists"
    gdf=join_pandas_geopandas(pandas_data,geopandas_shape)
    coord=polygons(cordinates_lst)
    
    tooltip=folium.features.GeoJsonTooltip(fields=fields_,aliases=aliases_,labels=True,stick=False)
    map_=folium.Map(location=coord,tiles="Stamen Terrain",zoom_start=5)
    cpleth=folium.Choloropleth(gdf,data=gdf,key_on=('features.properties.objectid'),columns=column_lst,fill_color=fill_clr,legend_name=lgnd_name,name=name_)

    cpleth.geojson.add_child(tooltip)
    cpleth.add_to(map_)
    folium.LayerControl().add_to(map_)
    
    map_.save(name_+".html")