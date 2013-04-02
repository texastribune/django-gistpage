from glob import iglob
from operator import concat
import mimetypes

from django.http import HttpResponse
from django.views.generic import TemplateView, View


class Page(TemplateView):
    template_name = "index.html"


class Glob(View):
    pattern = None  # make sure to pass this into your as_view()

    def get(self, request, **kwargs):
        def contents(filename_list):
            for filename in filename_list:
                with open(filename, "r") as f:
                    yield f.read()
        files = iglob(self.pattern)
        return HttpResponse(reduce(concat, contents(files)),
            content_type=mimetypes.guess_type(self.pattern),
            # content_type='text/plain',
        )
