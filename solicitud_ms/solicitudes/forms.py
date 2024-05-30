from django import forms

from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta: 
        model= Solicitud
        fields=[
            'id',
            'fecha',
            'ciudad',
            'direccion',
            'estado',
            'tipo',
        ]
        labels= {
            'id':'Id',
            'fecha':'Fecha',
            'ciudad':'Ciudad',
            'direccion':'Direccion',
            'estado':'Estado',
            'tipo':'Tipo',
        }
