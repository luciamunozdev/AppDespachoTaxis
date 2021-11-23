from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_index, name='map_index'),
]