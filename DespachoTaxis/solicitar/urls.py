from django.urls import path, include
from . import views

urlpatterns = [

    path('solicitar-taxi', views.solicitar, name="solicitar"),

]