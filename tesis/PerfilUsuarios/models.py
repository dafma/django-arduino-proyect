from django.db import models

class Nuevo_Usuario(models.Model):
	Nombre = models.CharField(max_length=255)
	Apellido = models.CharField(max_length=255)
	Direccion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.Nombre
    	
	class Meta:
	    db_table='perfil_usuarios'
	
	