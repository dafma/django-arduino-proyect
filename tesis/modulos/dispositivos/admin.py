from django.contrib import admin
from modulos.dispositivos.models import Dispositivos
from modulos.dispositivos.models import Tareas
from modulos.dispositivos.models import UsosDisp 
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _

# Register your models here.
from import_export import resources


class DispResource(resources.ModelResource):
    class Meta:
        model = Dispositivos



class DispositivoAdmin(ImportExportActionModelAdmin):
    list_per_page=10
    select_related=False 
    search_fields=['nombre', 'tipo',]
    list_display=('nombre','tipo','puerto', 'watts', 'is_on')
    list_filter=['is_on', 'status']
    resource_class = DispResource

    def history_view(self,request,object_id,extra_context=None):
        from django.template.response import  TemplateResponse
        from django.contrib.admin.models import LogEntry
        from django.shortcuts import get_object_or_404
        from django.contrib.admin.util import unquote
        from django.utils.encoding import force_unicode
        from django.utils.text import capfirst
        model = self.model
        opts = model._meta
        app_label = opts.app_label
        action_list = LogEntry.objects.filter(
            object_id = object_id,
            content_type__id__exact = ContentType.objects.get_for_model(model).id
        ).select_related().order_by('action_time')
        #Muestra solo el historico del usuario si no 
        if not request.user.is_superuser:
            action_list=action_list.filter(user=request.user)
        # If no history was found, see whether this object even exists.
        obj = get_object_or_404(model, pk=unquote(object_id))
        context = {
            'title': _('Change history: %s') % force_unicode(obj),
            'action_list': action_list,
            'module_name': capfirst(force_unicode(opts.verbose_name_plural)),
            'object': obj,
            'app_label': app_label,
            'opts': opts,
        }
        context.update(extra_context or {})
        return TemplateResponse(request, self.object_history_template or [
            "admin/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "admin/%s/object_history.html" % app_label,
            "admin/object_history.html"
        ], context, current_app=self.admin_site.name)
    ordering=['-id']
admin.site.register(Dispositivos, DispositivoAdmin)


class TareaResource(resources.ModelResource):
    class Meta:
        model = Tareas

class TareasAdmin(ImportExportActionModelAdmin):
    list_per_page=10
    select_related=False 
    search_fields=['title', 'dispositivo__nombre',]
    list_display=('title', 'Dispositivo',  'start', 'end', 'allDay', 'status')
    list_filter=['allDay', 'start', 'end']
    resource_class = TareaResource


    def history_view(self,request,object_id,extra_context=None):
        from django.template.response import  TemplateResponse
        from django.contrib.admin.models import LogEntry
        from django.shortcuts import get_object_or_404
        from django.contrib.admin.util import unquote
        from django.utils.encoding import force_unicode
        from django.utils.text import capfirst
        model = self.model
        opts = model._meta
        app_label = opts.app_label
        action_list = LogEntry.objects.filter(
            object_id = object_id,
            content_type__id__exact = ContentType.objects.get_for_model(model).id
        ).select_related().order_by('action_time')
        #Muestra solo el historico del usuario si no 
        if not request.user.is_superuser:
            action_list=action_list.filter(user=request.user)
        # If no history was found, see whether this object even exists.
        obj = get_object_or_404(model, pk=unquote(object_id))
        context = {
            'title': _('Change history: %s') % force_unicode(obj),
            'action_list': action_list,
            'module_name': capfirst(force_unicode(opts.verbose_name_plural)),
            'object': obj,
            'app_label': app_label,
            'opts': opts,
        }
        context.update(extra_context or {})
        return TemplateResponse(request, self.object_history_template or [
            "admin/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "admin/%s/object_history.html" % app_label,
            "admin/object_history.html"
        ], context, current_app=self.admin_site.name)
    ordering=['-id']
    def Dispositivo(self, obj):
          return ("%s" % (obj.dispositivo)).upper()
    Dispositivo.short_description = 'Dispositivo'
admin.site.register(Tareas, TareasAdmin)


class usosAdmin(admin.ModelAdmin):
    list_per_page=10
    select_related=False 
    #search_fields=['usuario', 'dispositivo']
    #list_display=('DispositivoA','Usuario')
    #list_filter=['tiempo_encendido', 'tiempo_apagado']
admin.site.register(UsosDisp, usosAdmin)
