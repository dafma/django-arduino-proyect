from django.conf.urls import patterns, url


urlpatterns = patterns(

    '',
    url(r'^$', 'modulos.dispositivos.views.resumen', name='resumen'),
    

    url(r'^estadisticas/$', 'modulos.dispositivos.views.estadisticas', name='estadisticas'),
    url(r'^reportes/$', 'modulos.dispositivos.views.reportes', name='reportes'),
    url(r'^configuraciones/$', 'modulos.dispositivos.views.configuraciones', name='configuraciones'),

    url(r'^dispositivos/$', 'modulos.dispositivos.views.dispositivos', name='dispositivos'),
    url(r'^dispositivos/update/$', 'modulos.dispositivos.views.dispositivos', name='actualizar_dispositivo'),

    url(r'^tareas/$', 'modulos.dispositivos.views.tareas', name='tareas'),
    url(r'^tareas/list/$', 'modulos.dispositivos.views.ver_tareas'),
    url(r'^tareas/create/$', 'modulos.dispositivos.views.guardar_tarea'),
    url(r'^tareas/update/$', 'modulos.dispositivos.views.actualizar_tarea'),
    url(r'^tareas/delete/$', 'modulos.dispositivos.views.eliminar_tarea'),


)