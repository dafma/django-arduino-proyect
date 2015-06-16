# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError #se importa ValidationError para el uso del clean
from django.db.models import Q
from modulos.dispositivos.models import Dispositivos, Tareas
from django.forms import TextInput
from django.contrib.admin import widgets 


TipoReporte = (('0','Seleccione...'),('1','dispositivos disponibles'),('2','usuarios disponibles'), ('3','usos de dispositivos por usuario'),('4','tareas programadas'))

disp = (('0','Seleccione...'),)

class TipoReporteForm(forms.Form):
    tipo = forms.ChoiceField(choices=TipoReporte, required=True, help_text='<i>Por favor, seleccione el tipo que desea descargar.</i>', label='Tipo de reporte') 
    fecha_ini = forms.CharField()
    fecha_fin = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(TipoReporteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_ini'].widget = widgets.AdminDateWidget()
        self.fields['fecha_fin'].widget = widgets.AdminTimeWidget()

    def clean_tipo(self):
        if self.cleaned_data['tipo'] == '0':
            raise forms.ValidationError("Debe seleccionar el tipo")
        return self.cleaned_data['tipo']

