from django.http import Http404
from django.conf import settings

from .views import gistpage


class GistpageFallbackMiddleware(object):
    def process_response(self, request, response):
        print "test"
        if response.status_code != 404:
            # No need to check for a flatpage for non-404 responses.
            return response
        try:
            return gistpage(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
