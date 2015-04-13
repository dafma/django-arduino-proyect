from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response

def vista_principal(request):
  return render_to_response('home/mainpage.html', context_instance=RequestContext(request))
