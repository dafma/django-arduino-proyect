from django.db import models
from django.contrib.auth.models import User


class DispositivosManager(models.Manager):
    def as_choices(self):
        for dispositivo in self.all():
            yield (dispositivo.pk, unicode(dispositivo))

class Dispositivos(models.Model):
    objects = DispositivosManager()
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



class UsosDisp(models.Model):
    tiempo_encendido = models.DateTimeField(verbose_name="tiempo de encendido", null=True, blank=True)
    tiempo_apagado = models.DateTimeField(verbose_name="tiempo de apagado", null=True, blank=True)
    Usuario = models.ForeignKey(User)
    dispositivo = models.ForeignKey(Dispositivos)

    class Meta:
        verbose_name_plural = 'Usos de dispositivos'
        verbose_name = 'Usos de dispositivo'

    def __unicode__(self):
        return u'%s - %s' %(self.dispositivo, self.Usuario)
