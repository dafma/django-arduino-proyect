from django.shortcuts import render_to_response
from django.template import RequestContext

def resumen(request):
  return render_to_response('resumen/mainpage.html', context_instance=RequestContext(request))
