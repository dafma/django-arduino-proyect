# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from modulos.dispositivos.models import Dispositivos, Tareas
from modulos.dispositivos.models import UsosDisp 
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#importacion de la placa arduino
from Arduino import Arduino
board = Arduino('9600') 

#importacion de paquetes necesarios para reportes pdf

#----> Canvas clase de reportlab para generar el pdf que trabaja por coordenadas
from reportlab.pdfgen import  canvas
#----> Image, Drawing son funciones de canvas
from reportlab.graphics.shapes import Image, Drawing
#----> Tipos de letras y tramaños de hoja
from reportlab.lib.pagesizes import letter, landscape, portrait, A4, A5, A3, legal
#----> getSampleStyleSheet es la clase con que le doy los estilos al texto y Paragraph es la clase que une los estilos con el string que le pases
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.colors import black
#----> Metodos de la y clases de la clase Platypus
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, Image, Spacer, Paragraph, Table, TableStyle, Frame, PageTemplate
#----> libreria para alinear el texto cuando le estes definiendo el estilo
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
#----> clase que contiene los tipos de letras
from reportlab.pdfbase.ttfonts import TTFont
#----> libreria donde obtienes las unidades de medidas
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
#----> libreria de reportlab para generar las fechas en cualquier formato copiada a lib/
import datetime
import time
from django.contrib.auth.decorators import login_required,user_passes_test, permission_required
#----> barcode es la clase para generar los codigos de barras en los reportes
from reportlab.graphics.barcode import code128, code93, createBarcodeDrawing, getCodeNames
from reportlab.graphics.barcode.code93 import *
from django.contrib.auth.models import User
from django.db import transaction, models
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase import pdfmetrics
# Variables donde defino el ancho y largo de la página usadas en la funcion cabecera
from django.db import connection #-----> connection permite conectar las funciones de sql con django
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib import messages #Sirve para mostrar el mensaje de error en la interfaz de Django
from reportlab.graphics.charts.piecharts import Pie
from django.core.context_processors import csrf
from reportlab.lib.units import inch, cm, mm
from modulos.dispositivos  import fecha

PAGE_HEIGHT=29.7*cm
PAGE_WIDTH=21*cm


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
        board.pinMode(puerto, "OUTPUT") # les paso el numero del puerto
        board.digitalWrite(puerto, is_on_arduino) # les paso el numero del puerto
        dispositivo = Dispositivos.objects.get(id=request.POST['id'])
        # ultimo_uso = UsosDisp.objects.filter(dispositivo=dispositivo).order_by('-id')[0]
        usuario = request.user
        #import pdb; pdb.set_trace() 
        if is_on == True:
            UsosDisp.objects.create(Usuario=usuario, dispositivo=dispositivo, tiempo_encendido=datetime.datetime.now(),tiempo_apagado=datetime.datetime.now())
        else:
            UsosDisp.objects.create(Usuario=usuario, dispositivo=dispositivo, tiempo_encendido=datetime.datetime.now(), tiempo_apagado=datetime.datetime.now())
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
    dispositivos = Dispositivos.objects.all()
    return render_to_response('tareas/tareas.html', locals(), context_instance=RequestContext(request))


def guardar_tarea(request):
    tarea = Tareas.objects.create(
        title = request.POST['title'],
        start = request.POST['inicio'],
        end = request.POST['fin'],
        dispositivo_id = request.POST['dispositivo']

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


from modulos.dispositivos.forms import TipoReporteForm
def reportes_pdf(request):
    if request.method == 'POST':
        import ipdb;ipdb.set_trace()
        form = TipoReporteForm(request.POST)
        if form.is_valid():
            tipo = request.POST['tipo']
            if tipo == '1':
                return HttpResponseRedirect("/disponibles/")

    else:
        form = TipoReporteForm()
    return render(request, 'reportes/reportes.html', {'form':form})

# --------------------> Reportes
class NumeroDePagina(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        fechas = datetime.datetime.today()
        self.setFont("Helvetica-Bold", 6)
        self.drawRightString(129*mm, 6*mm,
            u"A.C.C.E.M.A     %02d/%02d/%d   %02d:%02d:%02d    Página %d de %d" % (fechas.day,fechas.month,fechas.year, fechas.hour, fechas.minute, fechas.second, self._pageNumber, page_count))

def disponibles(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=dispositivos_registrados.pdf; pagesize=A4;'

    #elementos es la lista donde almaceno todos lo que voy a incluir al documento pdf
    elementos = []
    doc = SimpleDocTemplate(response, topMargin=100, bottomMargin=100)
    style = getSampleStyleSheet()
    style2 = getSampleStyleSheet()
    styleFecha = getSampleStyleSheet()

    fechas = datetime.datetime.today()
    mes = fecha.NormalDate().monthName()
    dia = fecha.NormalDate().dayOfWeekName()

    txtFecha = '%s, %s DE %s DE %s'%(dia.upper(), fechas.day, mes.upper(), fechas.year)
    styleF = styleFecha['Normal']
    styleF.fontSize = 7
    styleF.fontName = 'Helvetica'
    styleF.alignment = TA_RIGHT
    fechaV = Paragraph(txtFecha, styleF)
    elementos.append(fechaV)
    elementos.append(Spacer(1,5))

    txtTitulo = u'DISPOSITIVOS DISPONIBLES PARA EL CONTROL ELECTRICO'
    titulo = style['Heading1']
    titulo.fontSize = 9
    titulo.fontName = 'Helvetica-Bold'
    titulo.alignment = TA_CENTER
    tituloV = Paragraph(txtTitulo, titulo)
    elementos.append(tituloV)

    x = [
    #('BOX', (0,0), (4,0), 0.60, colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('GRID', (0,0), (-1,-1), 0.80, colors.black),
    ('ALIGN', (2,1), (2,1), 'CENTER'),
    ('BACKGROUND', (0,0), (6,0), colors.beige),
    ]

    tabla = []
    tabla.append([u'Nombre del Dispositivo', u'Tipo', u'Puerto de conexión', u'watts', u'esta encendido?'])
    dispositivos = Dispositivos.objects.all()
    num = 0 # Variable acumulador para enumerar la lista
    for i in dispositivos:
        tabla.append([
            u'%s'%(str(i.nombre).upper(),),
            u'%s'%(i.tipo),
            '%s'%(i.puerto),
            '%s'%(i.watts),
            '%d' %(i.is_on),
            ])
        num = num + 1


    t1 = Table(tabla, colWidths=('','', '', '', '',))
    t1.setStyle(TableStyle(x))
    elementos.append(t1)

    #doc.pagesize = landscape(A4) #Para poner la Hoja horizontal
    doc.build(elementos, canvasmaker=NumeroDePagina )
    return response

def usuarios(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=usuarios_registrados.pdf; pagesize=A4;'

    #elementos es la lista donde almaceno todos lo que voy a incluir al documento pdf
    elementos = []
    doc = SimpleDocTemplate(response, topMargin=100, bottomMargin=100)
    style = getSampleStyleSheet()
    style2 = getSampleStyleSheet()
    styleFecha = getSampleStyleSheet()

    fechas = datetime.datetime.today()
    mes = fecha.NormalDate().monthName()
    dia = fecha.NormalDate().dayOfWeekName()

    txtFecha = '%s, %s DE %s DE %s'%(dia.upper(), fechas.day, mes.upper(), fechas.year)
    styleF = styleFecha['Normal']
    styleF.fontSize = 7
    styleF.fontName = 'Helvetica'
    styleF.alignment = TA_RIGHT
    fechaV = Paragraph(txtFecha, styleF)
    elementos.append(fechaV)
    elementos.append(Spacer(1,5))

    txtTitulo = u'USUARIOS REGISTRADOS EN EL SISTEMA'
    titulo = style['Heading1']
    titulo.fontSize = 9
    titulo.fontName = 'Helvetica-Bold'
    titulo.alignment = TA_CENTER
    tituloV = Paragraph(txtTitulo, titulo)
    elementos.append(tituloV)

    x = [
    #('BOX', (0,0), (4,0), 0.60, colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('GRID', (0,0), (-1,-1), 0.80, colors.black),
    ('ALIGN', (2,1), (2,1), 'CENTER'),
    ('BACKGROUND', (0,0), (6,0), colors.beige),
    ]

    tabla = []
    tabla.append([u'Nombre de usuario', u'Dirección de correo electrónico', u'Nombres', u'Apellidos', 'Fecha de ingreso'])
    usuarios = User.objects.all()
    num = 0 # Variable acumulador para enumerar la lista
    for i in usuarios:
        tabla.append([
            u'%s'%(str(i.username).upper(),),
            u'%s'%(i.email),
            '%s'%(i.first_name),
            '%s'%(i.last_name),
            '%s' %(i.date_joined),
            ])
        num = num + 1


    t1 = Table(tabla, colWidths=('','', '', '', '',))
    t1.setStyle(TableStyle(x))
    elementos.append(t1)

    #doc.pagesize = landscape(A4) #Para poner la Hoja horizontal
    doc.build(elementos, canvasmaker=NumeroDePagina )
    return response


def ListadoUsos(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=num_aprobados_reprobados.pdf; pagesize=A4;'

    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response)
    styleSheet = getSampleStyleSheet()
    #---> Estilo Titulo
    el_titulo = styleSheet['Heading1']
    el_titulo.alignment = TA_CENTER
    el_titulo.spaceBefore = 15
    el_titulo.fontSize = 12
    el_titulo.fontName = 'Helvetica'


    txtInfo = u'<br />A.C.C.E.M.A:'
    # Estilo txtInfo
    info = styleSheet['Normal']
    info.fontSize = 12
    info.alignment = TA_LEFT
    info.fontName = 'Helvetica'
    infoV = Paragraph(txtInfo, info)

    #-->Estilo tabla
    x = [
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('GRID', (0,0), (-1,-1), 0.80, colors.black),
    ('FONT', (0,0), (-1,-1), "Helvetica", 10),
    ('FONT', (0,0), (1,0), "Helvetica-Bold", 12),
    ]
    tabla = []

    #--> Titulo de la constancia
    elementos.append(Spacer(1,5))
    Titulo = Paragraph('<b>Estadisticas de usos</b>', el_titulo)
    elementos.append(Titulo)
    elementos.append(Spacer(1,5))

    #--> Añadiendo la Informción antes del cuadro
    elementos.append(infoV)
    elementos.append(Spacer(1,10))

    usuarios = User.objects.all()
    usos = UsosDisp.objects.all()


    tabla.append([' CANTIDAD DE USUARIOS', u'NÚMERO DE USOS'])
    tabla.append(['%s'%(usuarios.__len__()), u'%s'%(usos.__len__())])

    t1 = Table(tabla, colWidths=('', ''))
    t1.setStyle(TableStyle(x))
    elementos.append(t1)

    #--> Calculando los porcentajes
    total = usos.__len__()
    
    #--> Frame del gráfico
    frame = Drawing(350,200)
    torta = Pie()
    torta.x = 125
    torta.y = 35
    torta.width = 120
    torta.height = 120

    torta.labels = []
    contador = 0 
    for i in usuarios:
        #import ipdb;ipdb.set_trace()
        uso_actual = usos.filter(Usuario=i).count()
        porcen_usuario = (float(uso_actual) * 100) / total

        torta.labels.append('%3.2f%% %s'%(porcen_usuario, i.username))
        torta.data.append(porcen_usuario)

    #--> Estilos del gráfico
    torta.slices.labelRadius = 1
    torta.sideLabels = 1
    torta.slices.fontSize = 8
    torta.slices.fontName = 'Helvetica-Bold'
    torta.slices.strokeWidth = 2
    torta.slices.popout = 10

    frame.add(torta)
    elementos.append(frame)
    doc.build(elementos, canvasmaker=NumeroDePagina )
    return response
