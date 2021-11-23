"""DespachoTaxis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from map.views import send_route, check_new_routes, check_taxis, map_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('solicitar.urls')),
    path('map/', include('map.urls')),
    #mapa
    path('map/', map_index),
    path('ajax/send_route/', send_route, name='send_route'),
    path('ajax/check_new_routes/', check_new_routes, name='check_new_routes'),
    path('ajax/check_taxis/', check_taxis, name='check_new_taxis')

]
