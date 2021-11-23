from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from map.geocoding import get_coord, get_rand_place, new_routes, assign_route, get_taxis, add_taxi
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from map.Taxi_class import Taxi

 #desp = 0.00003768 #aprox 60km/h si se llama a ala función cada 1/4s       

desp = 2**-16
def map_index(request):

        #------------------------------------------
    #For simulation purposes
    add_taxi(0, destino='Intercambiador de Plaza castilla')
    add_taxi(1, destino='Estación Getafe Central, Getafe')    
    #add_taxi(2, destino='Facultad de Medicina Complutense de Madrid')    
    #------------------------------------------



    template = loader.get_template('map_index.html')
    context = {
        'name_to_add': 'FUNCIONA!!!',
        'API_KEY_MAPS':'AIzaSyAuqDZE6TtnDFhqfMKsvYn7aNG8X0fqJig',
    }
    return HttpResponse(template.render(context, request))


def check_taxis(request):       
   taxis = get_taxis()  
   data={}
   ocupado = 'si'
   for id in taxis:
        #if abs(taxis[id].pos[0] - taxis[id].pos_dest['lat']) < 0.00001 and abs(taxis[id].pos[1] - taxis[id].pos_dest['lng']) < 0.0000001: ocupado = 'si'
        #else:        
        taxis[id].pos[0] = taxis[id].pos['lat']+desp if (taxis[id].pos['lat'] < taxis[id].pos_dest['lat'] ) else taxis[id].pos['lat']-desp
        taxis[id].pos['lng'] = taxis[id].pos['lng']+desp if  (taxis[id].pos['lng'] < taxis[id].pos_dest['lng']) else taxis[id].pos['lng']-desp
                   
        
        data[taxis[id].id]={'id':taxis[id].id,
                    'dest':taxis[id].dest,
                    'Lat':taxis[id].pos['lat'],
                    'Lng':taxis[id].pos['lng'],
                    'ocupado': ocupado}
       
   return JsonResponse(data)



#De aquí para abajo está por implementar

@csrf_exempt 
def send_route(request): 
    #recibimos la ruta --- Revisar si se recibe y se manda la path y no otra cosa
    array = request.GET.getlist('data[]')
    for e in array:        
        assign_route(e)
        print("-------------")
        print(e)

     


    return JsonResponse({
            'status':'ok',           
        })
   
def check_new_routes(request):
    r = new_routes()
    #if r is None: return JsonResponse({})
    data = {
        'route':[{
            '1': {
                'origin': r['origin'],
                'dest': r['dest']
            }
        }]       
    }
    
    return JsonResponse(data)

