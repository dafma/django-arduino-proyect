from django.conf.urls import patterns, url
from sugerencias import views



urlpatterns=patterns('',
   url(r'^$', views.sugerenciasList, name='Listado_sugerencias'),
   url(r'^new$', views.sugerenciasCreate, name='Crear_sugerencias'),
   url(r'^edit/(?P<pk>\d+)$', views.sugerenciasUpdate, name='Editar_sugerencias'),
)	