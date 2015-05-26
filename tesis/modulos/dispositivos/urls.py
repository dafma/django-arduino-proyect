from django.conf.urls import patterns, url


urlpatterns = patterns(

    '',
    url(r'^$', 'modulos.dispositivos.views.resumen', name='resumen'),

)