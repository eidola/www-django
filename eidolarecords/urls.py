from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eidolarecords.views.home', name='home'),
    # url(r'^eidolarecords/', include('eidolarecords.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^releases/',include('releases.urls', namespace="releases")),
    url(r'^artists/',include('artists.urls', namespace="artists")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

