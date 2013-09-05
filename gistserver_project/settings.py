# Django settings for gistserver project.
import os


def project_dir(*paths):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *paths)


DEBUG = True

ALLOWED_HOSTS = ['*']

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = project_dir('..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = project_dir('static_root')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    project_dir('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lolimasekrit'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

ROOT_URLCONF = __name__

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    project_dir('templates'),
    os.path.abspath('.'),
]

ADDITIONAL_TEMPLATE_DIR = os.environ.get('ADDITIONAL_TEMPLATE_DIR', '')
if ADDITIONAL_TEMPLATE_DIR:
    TEMPLATE_DIRS.append(ADDITIONAL_TEMPLATE_DIR)

INSTALLED_APPS = [
    'django.contrib.staticfiles',

    # helpers
    'abstract_templates',
]

# TODO clean up this file
from django.conf.urls import patterns, url
from django.views.static import serve

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Page.as_view()),
    url(r'^app.css$', views.Glob.as_view(pattern="*.css")),
    url(r'^app.js$', views.Glob.as_view(pattern="*.js")),

    # Use Django to serve static media even when DEBUG=False
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': STATIC_ROOT,
    }),
)

try:
    from .local_settings import *
except ImportError:
    pass
