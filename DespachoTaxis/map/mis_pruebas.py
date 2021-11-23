import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAuqDZE6TtnDFhqfMKsvYn7aNG8X0fqJig')
import json

saved_searchs = {}
def get_coord(search): 

    with open('places.json', 'r') as json_places:
        data = json.load(json_places)        

    if search in data:                
        return data[search]

    with open('places.json', 'w') as json_places: 
        data = gmaps.geocode(address=search, region = "es")   #Se cobra 0.005€ por petición. Minimizar uso de llamadas.
        print(",,,,,,")        
        saved_searchs[search] = data[0]['geometry']["location"]
        json.dump(saved_searchs, json_places)
    return saved_searchs[search]

