from glob import iglob
from operator import concat
import mimetypes

from django.http import HttpResponse
from django.views.generic import View


class Glob(View):
    """
    Concats and serves all files found by globbing `self.pattern`.

    TODO raise helpful error if no `pattern`.
    WISHLIST handle large numbers of large files better?
    """
    pattern = None  # make sure to pass this into your as_view()

    def get(self, request, **kwargs):
        def contents(filename_list):
            for filename in filename_list:
                with open(filename, "r") as f:
                    yield f.read()
        files = iglob(self.pattern)
        return HttpResponse(reduce(concat, contents(files)),
            content_type=mimetypes.guess_type(self.pattern)[0],
            # content_type='text/plain',
        )
