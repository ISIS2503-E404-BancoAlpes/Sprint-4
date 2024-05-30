from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^productos/', views.ProductosList,name="ProductoList"),
    url(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='ProductoCreate'),
    url(r'^productoUpdate/<int:producto_nombre>/$', csrf_exempt(views.ProductoUpdate), name='productoUpdate'),
]