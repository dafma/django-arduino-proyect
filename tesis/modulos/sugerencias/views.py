from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.views.generic import TemplateView
from sugerencias.models import *


class SugerenciasForm(ModelForm):

    class Meta:
		model = Sugerencias

@login_required(login_url='/login/')
def sugerenciasList(request, template_name='sugerencias/list_sugerencias.html'):

	listsugerencias=Sugerencias.objects.all()
	data={}
	data['sugerenciaslist'] = listsugerencias
	return render(request, template_name, data)

@login_required(login_url='/login/')
def sugerenciasCreate(request, template_name='sugerencias/form_sugerencias.html'):
    form = SugerenciasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Listado_sugerencias')
    return render(request, template_name, {'form':form})

@login_required(login_url='/login/')
def sugerenciasUpdate(request, pk, template_name='sugerencias/form_sugerencias.html'):

    objsugerencias = get_object_or_404(Sugerencias, pk=pk)
    form = SugerenciasForm(request.POST or None, instance=objsugerencias)
    if form.is_valid():
        form.save()
        return redirect('Listado_sugerencias')
    return render(request, template_name, {'form':form})
"""
@login_required(login_url='/login/')
def proyecto(request, template_name='sugerencas/acer_proyecto.html'):

@login_required(login_url='/login/')
def reporte(request, template_name='sugerencias/reportes.html'):

@login_required(login_url='/login/')
def camposF(request, template_name='sugerencias/campo_fun.html'):

@login_required(login_url='/login/')
def control(request, template_name='sugerencias/control.html'):"""