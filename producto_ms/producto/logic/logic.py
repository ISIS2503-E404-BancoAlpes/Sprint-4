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
    productos_collection = db['prodcuto']
    productos_db = productos_collection.find({})
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

def createProduct(data):
    client = MongoClient(settings.MONGO_CLI)
    db = client.productos_db
    producto =verifyProductData(data)

    productos_collection = db['products'] 
    producto.id = productos_collection.insert_one(
        {
            'nombre': producto.nombre,
            'tier'  : producto.tier,
            'fecha' : producto.fecha ,
            'tipo'  : producto.tipo
        }
    )
    client.close()
    return () 

def verifyProductData(data):
    if 'name' not in data:
        raise ValueError('name is required')
    
    producto = Producto()
    producto.id= data['id']
    producto.nombre = data['nombre']
    producto.tipo = data['tipo']
    producto.tier = data['tier']
    producto.fecha =  data['fecha']
    return producto
