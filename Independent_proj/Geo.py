
import pandas as pd
from geopy.geocoders import Nominatim

class FelGeo:

    def __init__(self):
        self.geolocator = Nominatim(timeout=10, user_agent= "myGeolocator")
    def encode(self, file):
        df =pd.read_csv(file)
        df["gcode"] = [self.geolocator.geocode(a) for a in df["Address"]]
        df["lat"] = [g.latitude for g in df["gcode"]]
        df['long'] = [g.longitude for g in df["gcode"]]
        df.to_csv("geocodedfile.csv", index = True)
