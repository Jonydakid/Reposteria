from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Persona(models.Model):
	idPersona = models.AutoField(primary_key=True)
	run = models.CharField(unique=True, max_length=10)
	nombreCompleto = models.CharField(max_length=100)
	fechaNacimiento = models.DateField()
	telefono = models.IntegerField(null=True)
	direccion = models.CharField(max_length=254)
	email = models.CharField(max_length=100)

class Producto(models.Model):
	idProducto = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	categoria=models.CharField(max_length=25)
	precio = models.IntegerField()
	stock = models.IntegerField()
	foto=models.ImageField(upload_to = "media", blank = True)
	descripcion=models.CharField(max_length = 100)

class Boleta(models.Model):
	idBoleta = models.AutoField(primary_key = True)
	persona = models.ForeignKey(Persona, on_delete = models.DO_NOTHING)
	producto = models.ForeignKey(Producto, on_delete = models.DO_NOTHING)
	nroPedido=models.IntegerField()
	fecha = models.DateField()
	fechaEntrega = models.DateField()
	estado=models.CharField(max_length=15)
	total=models.IntegerField()
