# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.template.loader import render_to_string

def vista_principal(request):
  return render_to_response('home/mainpage.html', context_instance=RequestContext(request))

def usos_est(request):
    query = UsosDisp.objects.all().values_list('Usuario__dispositivo_id').annotate(total=Count('dispositivo.id')).order_by('total')
    data = json.dumps(list(query), cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')

def dispositivos_est(request):
    query = Dispositivos.objects.all().values_list('dispositivo__dispositivo_nombre').annotate(total=Count('dispositivo.nombre')).order_by('total')
    data = json.dumps(list(query), cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')