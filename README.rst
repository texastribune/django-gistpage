Django-GistPage
===============

**Disclaimer:** *This is pre-alpha code. Not all the claims made in in this
document are implemented.*

This package provides two components:

1. **DjangoGistServer**: A way to develop a simple static site that uses the
   full Django templating engine.

2. **GistPage**: A way to take a page developed using DjangoGistServer that's
   been published as a GitHub gist and serve it at a url.

DjangoGistServer
----------------

Sample Usage:

Using virtualenvwrapper and vi as the editor::

    # do development inside a virtualenv because this uses a lot of libraries
    mkvirtualenv gistme
    pip install django-gistpage
    mkdir my_awesome_page
    cd my_awesome_age
    vi index.html
    vi app.js
    vi app.css
    python -m DjangoGistServer 8000 --template-dir=/a/b/c/templates/
    # your directory is now being served on port 8000

Turning your static page into a gist:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are several command line tools you can install do do this:

* TODO

You can also create a gist from GitHub, clone it locally, and push it back up.

GistPage
--------

To serve that static site in your production Django site, you would create a new
``GistPage`` object in the admin, just like a flatpage. Point it to the gist
version of the static page, and that's it.
