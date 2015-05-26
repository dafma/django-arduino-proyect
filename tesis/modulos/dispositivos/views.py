from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from modulos.dispositivos.models import Dispositivos



def resumen(request):
    return render_to_response('resumen/resumen.html', context_instance=RequestContext(request))


def dispositivos(request):
    if request.method == 'POST':

        # hago el import desde aqui, ya que sera la unica funcion en utilizar esta libreria
        from Arduino import Arduino
        board = Arduino('9600') #plugged in via USB, serial com at rate 9600
        
        
        is_on = True
        is_on_arduino = 'HIGH'

        if request.POST['is_on'] == 'false':
            is_on = False
            is_on_arduino = 'LOW'

        dispositivo = Dispositivos.objects.filter(id=int(request.POST['id'])).update(is_on=is_on)
        puerto = Dispositivos.objects.get(id=dispositivo).puerto
        board.pinMode(puerto, "OUTPUT")
        board.digitalWrite(puerto, is_on_arduino)

        #import ipdb; ipdb.set_trace()

        return HttpResponse("{'success':true}")


    dispositivos = Dispositivos.objects.filter(status=True)
    return render_to_response('dispositivos/dispositivos.html', locals(), context_instance=RequestContext(request))


def tareas(request):
    return render_to_response('tareas/tareas.html', context_instance=RequestContext(request))


def estadisticas(request):
    return render_to_response('estadisticas/estadisticas.html', context_instance=RequestContext(request))


def reportes(request):
    return render_to_response('reportes/reportes.html', context_instance=RequestContext(request))


def configuraciones(request):
    return render_to_response('configuraciones/configuraciones.html', context_instance=RequestContext(request))
