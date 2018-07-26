import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
el = list(data["ELEV"])

def color_producer(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000<= elevation < 3000:
		return 'orange'
	else:
		return 'red'

map_1 = folium.Map(location=[28.69, 77.51], zoom_start=6)  # can add :tiles="Mapbox Bright"

for i,j,nm,el in zip(lat,lon,name,el):
	folium.Marker([i, j],
              popup= folium.Popup(str(nm),parse_html=True),
              icon=folium.Icon(color = color_producer(el)) 
             ).add_to(map_1)

folium.GeoJson(data =open('world.json','r',encoding='utf-8-sig').read(),
style_function =lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000000 
else 'yellow' if 100000000 <= x['properties']['POP2005'] < 20000000 else 'red'}).add_to(map_1)

map_1.add_child(folium.LatLngPopup())
map_1.add_child(folium.ClickForMarker(popup='Waypoint'))
map_1.add_child(folium.LayerControl())
map_1.save("map1.html") 