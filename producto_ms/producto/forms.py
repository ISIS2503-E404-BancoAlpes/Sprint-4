from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta: 
        model= Producto
        fields=[
            'id',
            'nombre',
            'tier',
            'tipo', 
          
        ]
        labels= {
            'id': 'Id',
            'nombre':'nombre',
            'tier': 'Tier',
            'tipo': 'Tipo', 
     
        }