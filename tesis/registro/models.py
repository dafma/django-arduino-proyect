from django.db import models


class Registro(models.Model):
	Nombre = models.CharField(max_length=255)
	Apellido = models.CharField(max_length=244)
	Direccion = models.CharField(max_length=255)
	Fecha_nacimiento = models.DateField(auto_now=False or None)
	status = models.BooleanField()

	def __unicode__(self):
		return self.Nombre

