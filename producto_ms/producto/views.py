from django.shortcuts import render
from .logic.logic import getProdcutos , getProducto , deleteProduct, createProduct
# Create your views here.
from rest_framework.decorators import api_view
from .forms import ProductoForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


@api_view(["GET", "POST"])
def ProductosList(request): 
    productos= getProdcutos()
    context= {"productoList": productos }
    return render(request,'producto/productos.html',context)


@api_view(["GET", "POST"])
def ProductoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            createProduct(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created producto')
            return HttpResponseRedirect(reverse('ProductoCreate'))
        else:
            print(form.errors)
    else:
       
       form =ProductoForm()

    context = {
        'form': form,
    }
    return render(request, 'prodcuto/createProducto.html', context) 

def ProductoUpdate(request,producto_id): 
    producto= getProducto(request,producto_id)
    if request.method == 'POST':
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            createProduct(form) 
            return HttpResponseRedirect(reverse("solicitudesList"))
        else:
            print(form.errors) 
    else: 

        form= ProductoForm(instance=ProductoForm)
    context={
            'form': form,
    }    
    return render(request,'producto/updateProducto.html',context) 
  
