import folium
import pandas
import json
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

benes = open("world.json", "r", encoding = "utf-8-sig")
john = json.load(benes)

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2000:
        return "blue"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [38.5, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "volcanoes")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe),
    icon = folium.Icon(color = color_producer(el))))

fgp = folium.FeatureGroup(name = "population")

fgp.add_child(folium.GeoJson(data = john, style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000<= x["properties"]["POP2005"] < 20000000 else "red"}))
benes.close()
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map4.HTML")
