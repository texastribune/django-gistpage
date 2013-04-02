from django.views.generic import TemplateView


class Page(TemplateView):
    template_name = "index.html"
