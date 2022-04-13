import geopandas
import folium
import matplotlib


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