from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from modulos.dispositivos.models import Dispositivos, Tareas
import json
from django.core.serializers.json import DjangoJSONEncoder

from Arduino import Arduino
board = Arduino('9600') 



def resumen(request):
    return render_to_response('resumen/resumen.html', context_instance=RequestContext(request))


def dispositivos(request):
    
    if request.method == 'POST': # desde aqui recibo via ajax los datos enviados desde la plantilla (revisar archivo js en modulos/dispositivos/statis/js/dispositivos.js)
        
        is_on = True # inicializo en True por si el parametro enviado llega a ser false (es decir, false = off)
        is_on_arduino = 'HIGH' # inicializo en HIGH por si el parametro enviado llega a ser false (es decir, false = off)

        if request.POST['is_on'] == 'false': # si lo que le llega es false, entonces cambio las variables
            is_on = False
            is_on_arduino = 'LOW'

        Dispositivos.objects.filter(id=int(request.POST['id'])).update(is_on=is_on) #aqui actualizo en base de datos el estado del dispositivo
        puerto = Dispositivos.objects.get(id=int(request.POST['id'])).puerto # luego hago una busqueda para saber el numero del puerto de ese dispositivo y lo almaceno en la variable puerto
        
        #import ipdb; ipdb.set_trace()
        
        board.pinMode(puerto, "OUTPUT") # les paso el numero del puerto
        board.digitalWrite(puerto, is_on_arduino) # les paso el numero del puerto

        #import ipdb; ipdb.set_trace()

        return HttpResponse("{'success':true}")


    dispositivos = Dispositivos.objects.filter(status=True)
    return render_to_response('dispositivos/dispositivos.html', locals(), context_instance=RequestContext(request))





def estadisticas(request):
    return render_to_response('estadisticas/estadisticas.html', context_instance=RequestContext(request))


def reportes(request):
    return render_to_response('reportes/reportes.html', context_instance=RequestContext(request))


def configuraciones(request):
    return render_to_response('configuraciones/configuraciones.html', context_instance=RequestContext(request))




def tareas(request):
    return render_to_response('tareas/tareas.html', context_instance=RequestContext(request))


def guardar_tarea(request):
    tarea = Tareas.objects.create(
        title = request.POST['title'],
        start = request.POST['inicio'],
        end = request.POST['fin'],
        dispositivo_id = 1

    )
    tarea.save()

    return HttpResponse("{'success':true}")


def actualizar_tarea(request):
    Tareas.objects.filter(id=request.POST['id']).update(
        title = request.POST['title'],
        start = request.POST['inicio'],
        end = request.POST['fin'],
    )

    return HttpResponse("{'success':true}")


def eliminar_tarea(request):
    Tareas.objects.filter(id=request.POST['id']).delete()

    return HttpResponse("{'success':true}")


def ver_tareas(request):
    query=Tareas.objects.all().values('status','allDay','end', 'title',  'start', 'id', 'dispositivo__nombre')
    data = json.dumps(list(query), cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')