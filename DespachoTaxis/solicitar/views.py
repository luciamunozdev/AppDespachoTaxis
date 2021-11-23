from django.shortcuts import render
from .forms import FormularioSolicitar
from .models import viaje

# Create your views here.

def solicitar(request):

    form_solicitud = FormularioSolicitar()

    if request.method == "POST":
        form_solicitud = FormularioSolicitar(request.POST)

        if form_solicitud.is_valid():

            info_viaje = viaje()

            info_viaje.origen = form_solicitud.cleaned_data['origen']
            info_viaje.destino = form_solicitud.cleaned_data['destino']
            info_viaje.fecha = form_solicitud.cleaned_data['fecha']
            info_viaje.hora = form_solicitud.cleaned_data['hora']
            
            info_viaje.save()
    
    return render(request, "solicitud/solicitar.html",{
        'formulario':form_solicitud,
        'title': 'Solicitar Taxi'
        })
