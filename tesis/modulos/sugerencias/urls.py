from django.conf.urls import patterns, url
from sugerencias import views



urlpatterns=patterns('',
   url(r'^$', views.sugerenciasList, name='Listado_sugerencias'),
   url(r'^new$', views.sugerenciasCreate, name='Crear_sugerencias'),
   url(r'^edit/(?P<pk>\d+)$', views.sugerenciasUpdate, name='Editar_sugerencias'),
   
)	

"""
   url(r'^proyecto$', views.proyecto, name='Acerca_proyecto'),
   url(r'^reporte$', views.reporte, name='Reporte'),
   url(r'^camposfun$', views.camposF, name='Campos_fun'),
   url(r'^control$', views.control, name='Acerca_proyecto'),
"""

