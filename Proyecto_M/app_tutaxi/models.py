from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chofer(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    nacimiento=models.DateField()
    movil_a_cargo=models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    registro=models.DateField()
    movil_asignado=models.IntegerField()   
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}" 
    
class Movil(models.Model):
    patente=models.CharField(max_length=40)
    marca=models.CharField(max_length=40)
    modelo=models.DateField()
    chofer_asignado=models.IntegerField()  
    def __str__(self):
            return f"Patente: {self.patente} - Marca: {self.marca}"  
    
#************************AVATAR***************************************
class Avatar(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True, blank=True )