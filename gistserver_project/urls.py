from django.conf import settings
from django.conf.urls import patterns, url
from django.views.static import serve

from . import views


urlpatterns = patterns('',
    url(r'^$', views.Page.as_view()),
    url(r'^app.css$', views.Glob.as_view(pattern="*.css")),
    url(r'^app.js$', views.Glob.as_view(pattern="*.js")),

    # Use Django to serve static media even when DEBUG=False
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
)
