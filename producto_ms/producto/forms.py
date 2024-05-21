from django import forms

from .models import Producto

class SolicitudForm(forms.ModelForm):
    class Meta: 
        model= Producto
        fields=[

            'nombre',
            'tier',
            'tipo', 
            'fecha'
        ]
        labels= {
            'nombre':'nombre',
            'tier': 'Tier',
            'tipo': 'Tipo', 
            'fecha': 'Fecha'
        }