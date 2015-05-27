from django.conf.urls import patterns, include, url
from django.contrib import admin
from yawdadmin import admin_site
from django.conf import settings
from django.contrib.auth.views import login, logout

admin.autodiscover()
admin_site._registry.update(admin.site._registry)


urlpatterns = patterns('',
    url (r'^',include('modulos.dispositivos.urls')),
    url(r'^admin/', include(admin_site.urls)),
        
    url(r'^login/$', login),
	url(r'^logout/$', logout),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
	#url(r'^sugerencias/', include('sugerencias.urls')),
        
)

"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tesis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
"""
