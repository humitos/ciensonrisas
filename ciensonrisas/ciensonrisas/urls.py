from django.conf.urls import patterns, include, url

from django.views.generic import ListView
from django.views.generic import TemplateView

from website.models import Place
from website.views import PlaceDetailView
from website.views import SmileDetailView
from website.views import IndexTemplateView
from website.views import MessageCreate
from website.views import smile_detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciensonrisas.views.home', name='home'),
    # url(r'^ciensonrisas/', include('ciensonrisas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', IndexTemplateView.as_view(template_name='index.html'),
        name='home'),
    url(r'^miralas$', ListView.as_view(model=Place), name='places'),
    url(r'^miralas/(?P<slug>[a-z0-9-_]+)$', PlaceDetailView.as_view(),
        name='place_detail'),
    url(r'^miralas/(?P<place_slug>[a-z0-9-_]+)/(?P<number>\d+)$', smile_detail,
        name='smile_detail'),
    url(r'^contact$', MessageCreate.as_view(),
        name='contact_form'),
    url(r'^contact/thanks$', TemplateView.as_view(template_name='thanks.html'),
        name='contact_thanks'),


    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain"))
)


from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^user-media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
