from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('gistpage.urls')),

    # Use Django to serve static media even when DEBUG=False
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
)
