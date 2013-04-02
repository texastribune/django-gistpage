from django.contrib import admin
from .models import GistPage


class GistPageAdmin(admin.ModelAdmin):
    fields = (
        'gist_url',
        'site_url',
        # 'sites',
    )

admin.site.register(GistPage, GistPageAdmin)
