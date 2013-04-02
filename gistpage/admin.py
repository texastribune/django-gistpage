import json

from django.contrib import admin
import requests

from .models import GistPage


class GistPageAdmin(admin.ModelAdmin):
    fields = (
        'gist_url',
        'site_url',
        'template',
        'style',
        'script',
        # 'sites',
    )

    def save_model(self, request, obj, form, change):
        def process(gist_files_dict):
            for filename, meta in gist_files_dict.items():
                yield meta['filename'], meta['content']

        # http://developer.github.com/v3/gists/#get-a-single-gist
        gist_id = obj.gist_url.strip('/').split('/')[-1]
        endpoint = 'https://api.github.com/gists/'
        response = requests.get('%s%s' % (endpoint, gist_id))
        if response.status_code != 200:
            # TODO validation error
            return

        # clear out old values
        obj.template = ''
        obj.style = ''
        obj.script = ''

        data = json.loads(response.content)
        files = data['files']

        for filename, content in process(files):
            if filename == 'index.html':
                obj.template = content
            extension = filename.rsplit('.', 1)[-1]
            if extension == 'css':
                obj.style += content
            if extension == 'js':
                obj.script += content

        obj.save()


admin.site.register(GistPage, GistPageAdmin)
