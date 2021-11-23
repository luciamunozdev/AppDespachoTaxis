from django.contrib import admin
from .models import Taxi
from django_object_actions import DjangoObjectActions
from django.template import loader
from django.http import HttpResponse
from map.geocoding import get_coord, get_rand_place, new_routes, assign_route, get_taxis, add_taxi




@admin.action(description='See in the map')
def see_in_map(modeladmin, request, queryset):	
	template = loader.get_template('map_index.html')	
	context = {
				'name_to_add': '',
				'API_KEY_MAPS':'AIzaSyAuqDZE6TtnDFhqfMKsvYn7aNG8X0fqJig',
			}
		
	for e in queryset.values():		
		add_taxi(id=e['id'], origen=e['ubicacion_actual'] , destino =e['destino'])
		
	return HttpResponse(template.render(context, request))



# Register your models here.
class adminTaxis(admin.ModelAdmin):
	list_display = ("matricula", "estado_taxi", "conductor","destino", "ubicacion_actual")
	search_fields = ("conductor", "matricula","estado_taxi")
	actions = [see_in_map]


	

admin.site.register(Taxi, adminTaxis)



#configurar titulo panel
admin.site.site_header='Administracion de Despacho de Taxis'
admin.site.site_title = 'Administracion de Despacho de Taxis'
admin.site.index_title = 'Panel de gestión'


# class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def publish_this(self, request, obj):     
#     	change_actions = ('publish_this', )


