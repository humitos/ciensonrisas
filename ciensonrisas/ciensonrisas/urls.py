from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.views.generic import ListView

from website.models import Place

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciensonrisas.views.home', name='home'),
    # url(r'^ciensonrisas/', include('ciensonrisas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^miralas$', ListView.as_view(model=Place), name='miralas'),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^user-media/(?P<path>.*)$', 'serve'),
    )
