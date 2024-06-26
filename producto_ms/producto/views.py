from django.shortcuts import render
from .logic.logic import getProdcutos , getProducto ,createProduct
# Create your views here.
from rest_framework.decorators import api_view
from .forms import ProductoForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


@api_view(["GET", "POST"])
def ProductosList(request): 
    productos= getProdcutos()
    print(productos, "PRODUCTOS")
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
    return render(request, 'producto/createProducto.html', context) 

@api_view(["GET", "POST"])
def ProductoUpdate(request,id): 
    producto= getProducto(id)
    if request.method == 'POST':
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            createProduct(form) 
            return HttpResponseRedirect(reverse("ProductoList"))
        else:
            print(form.errors) 
    else: 

        form= ProductoForm(instance=ProductoForm)
    context={
            'form': form,
    }    
    return render(request,'producto/updateProducto.html',context) 
  
