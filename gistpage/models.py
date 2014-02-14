# from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models


class GistPage(models.Model):
    """Similar to a Flatpage, but backed by a Github.com gist."""
    #
    gist_url = models.URLField()
    template = models.TextField(null=True, blank=True)
    style = models.TextField(null=True, blank=True)
    script = models.TextField(null=True, blank=True)

    # integration fields
    site_url = models.CharField(max_length=200, null=True, blank=True,
        help_text="The url for this page on the site. e.g.: /test/page/")
    sites = models.ManyToManyField(Site,
        # default=settings.SITE_ID
    )

    # lead_art
    # headline
    # summary
