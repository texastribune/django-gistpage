# this is usually an empty file anyways, so throw random code we need to make
# sure Django picks up here.
#
# based on Auto-create Django admin user during syncdb
#   http://djangosnippets.org/snippets/1875/

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db.models import signals


def create_testuser(app, created_models, verbosity, **kwargs):
    if not settings.DEBUG:
        return
    try:
        auth_models.User.objects.get(username='test')
    except auth_models.User.DoesNotExist:
        assert auth_models.User.objects.create_superuser(
            'admin',
            'test@example.com',
            'admin',
        )
    else:
        print 'Test user already exists.'

signals.post_syncdb.connect(create_testuser, sender=auth_models)
