from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_protect

from .models import GistPage


# This view is called from GistpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
@csrf_protect
def gistpage(request, url):
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    print "hi", url
    page = get_object_or_404(GistPage, site_url__exact=url,
        # sites__id__exact=settings.SITE_ID
    )

    t = Template(page.template)
    c = RequestContext(request, dict(
        style=page.style,
        script=page.script,
    ))
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, GistPage, page.pk)
    return response
