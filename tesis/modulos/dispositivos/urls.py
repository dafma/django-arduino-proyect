# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    #url(r'^$', 'modulos.dispositivos.views.resumen', name='resumen'),
    url(r'^$', 'modulos.dispositivos.views.estadisticas', name='estadisticas'),
    url(r'^estadisticas/dispositivos$', 'modulos.dispositivos.views.estadisticasDisp'),
    url(r'^estadisticas/usuarios$', 'modulos.dispositivos.views.estadisticasUsu'),
    url(r'^reportes/$', 'modulos.dispositivos.views.reportes_pdf', name='reportes'),
    url(r'^disponibles/$', 'modulos.dispositivos.views.disponibles'),
    url(r'^usuarios/$', 'modulos.dispositivos.views.usuarios'),
    url(r'^usos/$', 'modulos.dispositivos.views.ListadoUsos'),
    #url(r'^reportepdf/(\d+)/', 'modulos.dispositivos.views.reportes_pdf'),
    url(r'^configuraciones/$', 'modulos.dispositivos.views.configuraciones', name='configuraciones'),
    url(r'^dispositivos/$', 'modulos.dispositivos.views.dispositivos', name='dispositivos'),
    url(r'^dispositivos/update/$', 'modulos.dispositivos.views.dispositivos', name='actualizar_dispositivo'),
    url(r'^tareas/$', 'modulos.dispositivos.views.tareas', name='tareas'),
    url(r'^tareas/list/$', 'modulos.dispositivos.views.ver_tareas'),
    url(r'^tareas/create/$', 'modulos.dispositivos.views.guardar_tarea'),
    url(r'^tareas/update/$', 'modulos.dispositivos.views.actualizar_tarea'),
    url(r'^tareas/delete/$', 'modulos.dispositivos.views.eliminar_tarea'),
    )
