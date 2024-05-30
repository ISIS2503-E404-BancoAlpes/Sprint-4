from django.db import models

# Create your models here.
class Solicitud(models.Model):
    id= models.IntegerField(primary_key = True)
    fecha= models.DateField()   #Fecha de creación 
    ciudad= models.CharField(max_length=50, default= None)
    direccion= models.CharField(max_length=50, default= None)
    estado= models.CharField(max_length=50, default= None)
    tipo= models.CharField(max_length=50, default= None)
    def __str__(self):
        return '%s , %s, %s, %s, %s, %s'%(self.id, self.fecha, self.ciudad, self.direccion, self.estado, self.tipo)