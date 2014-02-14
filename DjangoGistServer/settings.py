# Django settings for gistserver project.
import os


def project_dir(*paths):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *paths)


DEBUG = True

ALLOWED_HOSTS = ['*']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lolimasekrit'

ROOT_URLCONF = __name__

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath('.'),
]

ADDITIONAL_TEMPLATE_DIR = os.environ.get('ADDITIONAL_TEMPLATE_DIR', '')
if ADDITIONAL_TEMPLATE_DIR:
    TEMPLATE_DIRS.append(ADDITIONAL_TEMPLATE_DIR)

INSTALLED_APPS = [
]

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^app.css$', views.Glob.as_view(pattern="*.css")),
    url(r'^app.js$', views.Glob.as_view(pattern="*.js")),
)
