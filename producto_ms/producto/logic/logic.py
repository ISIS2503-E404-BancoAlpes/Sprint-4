from ..models import Producto
from django.shortcuts import get_object_or_404
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
import datetime


def getProdcutos():
    client = MongoClient(settings.MONGO_CLI)
    print(client)
    db = client.productos_db
    productos= [] 
    productos_collection = db['prodcuto']
    print(productos_collection, "Colection")
    productos_db = productos_collection.find({})
    print(productos_db, "Producto db")
    productos += [ Producto.from_mongo(producto) for producto in productos_db ]
    client.close()
    return productos

def getProducto(id):
    client = MongoClient(settings.MONGO_CLI)
    db = client.productos_db
    productos_collection = db['prodcuto']
    producto = productos_collection.find_one({'id':ObjectId(id)})
    client.close() 
    return producto 

def createProduct(form):
    client = MongoClient(settings.MONGO_CLI)
    db = client.productos_db
    producto = transForm(form)

    productos_collection = db['producto'] 
    print(productos_collection)
    print(producto)
    producto.id = productos_collection.insert_one(
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

    producto = Producto()
    nombre,tier,tipo,fecha= form.fields
    producto.nombre = nombre
    producto.tipo = tipo
    producto.tier = tier
    producto.fecha = fecha 
    return producto
