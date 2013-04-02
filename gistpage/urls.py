from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.Page.as_view()),
    url(r'^app.js$', views.Glob.as_view(pattern="*.js")),
)
