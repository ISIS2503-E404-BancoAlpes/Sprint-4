from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=50, default= None)
    tipo = models.CharField(max_length=50, default= None)
    fecha= models.DateField(auto_created=True, auto_now_add=True) 
    tier = models.CharField(null=True, blank= True)
    def __str_(self): 
        return "%s , %s , %s " 
