from ..models import Producto
from django.shortcuts import get_object_or_404
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
import datetime


def getProdcutos():
    client = MongoClient(settings.MONGO_CLI)
   
    db = client.productos_db
    productos= [] 
    productos_collection = db['producto']
   
    productos_db = productos_collection.find({})

    productos = []
    
    for producto in productos_db:
      productos.append( Producto.from_mongo(producto))


    client.close()
    return productos

def getProducto(id):
    client = MongoClient(settings.MONGO_CLI)
    db = client.productos_db
    productos_collection = db['producto']
    producto = productos_collection.find_one({'id':ObjectId(id)})
    client.close() 
    return producto 

def createProduct(form):
    client = MongoClient(settings.MONGO_CLI)
    db = client.productos_db
    producto = transForm(form)

    productos_collection = db['producto'] 
    
    producto.id = productos_collection.insert(
        {
            'nombre': producto.nombre,
            'tier'  : producto.tier,
            'fecha' : producto.fecha,
            'tipo'  : producto.tipo
        }
    )
    
    client.close()
    return () 

def transForm(form):

    producto = form.save(commit=False) 
    producto.fecha= datetime.datetime.now()
    return producto
