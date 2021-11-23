from django import forms
from datetime import datetime

class FormularioSolicitar(forms.Form):

    origen = forms.CharField(label="Origen", required=True)
    destino = forms.CharField(label="Destino", required=True)
    fecha = forms.DateField(label="Fecha", required=True, initial=datetime.now)
    hora = forms.TimeField(label="Hora", required=True, initial=datetime.now)