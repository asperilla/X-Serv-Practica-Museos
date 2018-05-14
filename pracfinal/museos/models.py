from django.db import models

# Create your models here.

class Museo(models.Model):
	Nombre = models.TextField(default="")
	Descripcion = models.TextField(default="")
	Accesibilidad = models.IntegerField(default="0")
	Barrio = models.TextField(default="")
	Distrito = models.TextField(default="")
	Telefono = models.TextField(default="")
	Fax = models.TextField(default="")
	Email = models.TextField(default="")
	Direccion = models.TextField(default="")
	CodigoPostal = models.IntegerField(default="0")
	Enlace = models.TextField(default="")

	def __str__(self):
		return self.Nombre

