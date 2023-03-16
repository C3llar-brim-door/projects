import requests
from bs4 import BeautifulSoup
import pandas



l = []

schroop = BeautifulSoup(c, "html.parser")

page_nr = schroop.find_all("a", {"class": "Page"})[-1].text

base_url = f"https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10, 10):
    r = requests.get(base_url + f"{page}.html")
    c = r.content
    soop = BeautifulSoup(c, "html.parser")
    charvas = soop.find_all("div", {"class": "propertyRow"})
    charvas[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ", "")
    for item in charvas:
        d={}
        d["Price"] = item.find("h4", {"class", "propPrice"}).text.replace("\n", "").replace(" ", "")
        d["Address"] = item.find_all("span", {"class", "propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span", {"class", "propAddressCollapse"})[1].text
        except:
            d["Locality"] = "no info"
        try:
            d["Beds"] = item.find("span", {"class", "infoBed"}).text
        except:
            d["Beds"] = "no info"
        try:
            d["Area"] = item.find("span", {"class", "infoSqFt"}).text
        except:
            d["Area"] = "no info"
        try:
            d["Full Baths"] = item.find("span", {"class", "infoValueFullBath"}).text
        except:
            d["Full Baths"] = "no info"
        try:
            d["Half Baths"] = item.find("span", {"class", "infoHalfBath"}).text
        except:
            d["Half Baths"] = "no info"
        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)

df = pandas.DataFrame(l)
df.to_csv("Web_data.csv")
