from os import error
import os
import random
import googlemaps
from datetime import datetime
import json
from map.Taxi_class import Taxi
gmaps = googlemaps.Client(key='AIzaSyAuqDZE6TtnDFhqfMKsvYn7aNG8X0fqJig')
pos_inicio = [[40.445906,-3.703979],[40.369674, -3.716095], [40.370124, -3.738196], [40.406415, -3.669671],[40.437997, -3.690703], [40.473435, -3.677528]]
request_route_pending = 0


saved_searchs = {}
taxis = {}



def get_coord(search): 
    data = gmaps.geocode(address=search, region = "es")   #Se cobra 0.005€ por petición. Minimizar uso de llamadas.     
    return data[0]['geometry']["location"]

    #  if not os.path.exists('places.json'):
    #      with open('places.json', 'w') as f: f.write("[{}]")

    #  with open('places.json', 'r') as json_places:
    #      data = json.load(json_places)        

    #  if search in data:                
    #      return data[search]

    #  with open('places.json', 'w') as json_places: 
    #     data = gmaps.geocode(address=search, region = "es")   #Se cobra 0.005€ por petición. Minimizar uso de llamadas.             
    #     saved_searchs[search] = data[0]['geometry']["location"]
    #     json.dump(saved_searchs, json_places)
        
    #  return saved_searchs[search]

#For debbug
#taxis = {0:Taxi(id=0, dest='Intercambiador de Plaza castilla',pos_dest=get_coord('Intercambiador de Plaza castilla') , pos_actual= [40.445906,-3.703979]), 1:Taxi(id=1, dest='Estación Getafe Central, Getafe', pos_dest=get_coord('Estación Getafe Central, Getafe'), pos_actual=[40.369674, -3.616095])}

def add_taxi_rand(id, destino):    
    if id in taxis: print("Ese taxi ya está añadido!")
    taxis[id]=Taxi(id = id,dest= destino, pos_dest=get_coord(destino), pos_actual=random.choice(pos_inicio))
    
def add_taxi(id, origen, destino):
     
    if id in taxis: 
        print("Ese taxi ya está añadido!")
    pos_origen = get_coord(origen)  
    if len(destino)<2: pos_destino=pos_origen
    else: pos_destino=get_coord(destino)
    taxis[id]=Taxi(id = id,dest= destino, pos_dest=pos_destino, pos_actual=pos_origen)
    

def get_taxis():
    return taxis




def request_route(taxi_id, dest):
    global request_route_pending
    taxis[taxi_id]['destino']=dest
    request_route_pending += 1

def assign_route(taxi_id, path):
    global request_route_pending
    taxis[taxi_id]['path']=path    
    request_route_pending -= 1


def request_route_pending():
    return request_route_pending > 0

def new_routes():
    i = 0
    routes = []
    #if request_pending: return []
    for taxi_id in taxis:
        if taxis[taxi_id]['destino'] != False:
            routes[i]=(taxis[taxi_id]["pos_actual"], taxis[taxi_id]["dest"])
            i+=1
    return routes

   

def get_rand_place():
    with open('map/latlng.json') as json_file:
        data = json.load(json_file)
        num = random.randint(0, len(data['places'])-1)
        latlng = (data['places'][num]['lat'], data['places'][num]['lng'])
        #print(latlng)
    return latlng


