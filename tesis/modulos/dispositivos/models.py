from django.db import models

class Dispositivos(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    watts = models.PositiveIntegerField()
    puerto = models.PositiveIntegerField()
    is_on = models.BooleanField(default=False) # para almacenar el estado en que se encuentra el dispositivo, encendido o apagado
    status = models.BooleanField(default=True) # para deshabilitar un dispositivo

    def __unicode__(self):
        return self.nombre


class Tareas(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField(verbose_name="inicio")
    end = models.DateTimeField(verbose_name="fin")
    allDay = models.BooleanField(default=False,verbose_name="todo el dia?")  
    status = models.CharField(max_length=100)
    dispositivo = models.ForeignKey(Dispositivos)

    def __unicode__(self):
        return self.title