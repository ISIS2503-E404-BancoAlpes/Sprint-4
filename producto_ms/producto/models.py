import datetime
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, default= None)
    tipo = models.CharField(max_length=50, default= None)
    fecha= models.DateTimeField()
    tier = models.CharField(null=True, blank= True,max_length=50)
    def __str__(self): 
        return "%s , %s , %s ,%s"%(self.id,self.nombre,self.fecha,self.tier)


    @staticmethod
    def from_mongo(dto):
        producto = Producto()
        producto.id     =  str(dto['_id'])
        producto.nombre = dto.get('nombre', '')
        producto.tipo   = dto.get('tipo','' )
        producto.tier   = dto.get('tier', '')
        producto.fecha  = dto.get('fecha', datetime.datetime.now())
        return producto
