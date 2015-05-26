from django.shortcuts import render_to_response
from django.template import RequestContext

def resumen(request):
  return render_to_response('resumen/resumen.html', context_instance=RequestContext(request))


def dispositivos(request):
  return render_to_response('dispositivos/dispositivos.html', context_instance=RequestContext(request))


def tareas(request):
  return render_to_response('tareas/tareas.html', context_instance=RequestContext(request))


def estadisticas(request):
  return render_to_response('estadisticas/estadisticas.html', context_instance=RequestContext(request))


def reportes(request):
  return render_to_response('reportes/reportes.html', context_instance=RequestContext(request))


def configuraciones(request):
  return render_to_response('configuraciones/configuraciones.html', context_instance=RequestContext(request))
