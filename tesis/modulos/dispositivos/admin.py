from django.contrib import admin
from modulos.dispositivos.models import Dispositivos
from modulos.dispositivos.models import Tareas

# Register your models here.
admin.site.register(Dispositivos)
admin.site.register(Tareas)
