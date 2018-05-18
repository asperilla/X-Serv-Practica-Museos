from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Museo(models.Model):
	Nombre = models.TextField(default="")
	Descripcion = models.TextField(default="")
	Accesibilidad = models.IntegerField(default="0")
	Barrio = models.TextField(default="")
	Distrito = models.TextField(default="")
	Telefono = models.TextField(default="")
	Email = models.TextField(default="")
	Direccion = models.TextField(default="")
	CodigoPostal = models.IntegerField(default="0")
	Enlace = models.TextField(default="")
	NumeroComentarios = models.IntegerField(default="0")

	def __str__(self):
		return self.Nombre

class Comentario(models.Model):
	Usuario = models.ForeignKey(User)		
	Comment = models.TextField(default="")
	MuseoComentado = models.ForeignKey('Museo')

	def __str__(self):
		return str(self.MuseoComentado)
