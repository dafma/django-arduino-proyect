from django.conf.urls import patterns, url


urlpatterns = patterns(

    '',
    url(r'^$', 'modulos.dispositivos.views.resumen', name='resumen'),
    url(r'^dispositivos/$', 'modulos.dispositivos.views.dispositivos', name='dispositivos'),
    url(r'^tareas/$', 'modulos.dispositivos.views.tareas', name='tareas'),
    url(r'^estadisticas/$', 'modulos.dispositivos.views.estadisticas', name='estadisticas'),
    url(r'^reportes/$', 'modulos.dispositivos.views.reportes', name='reportes'),
    url(r'^configuraciones/$', 'modulos.dispositivos.views.configuraciones', name='configuraciones'),


)