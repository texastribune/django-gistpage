Django-GistPage
===============

**Disclaimer:** *This is pre-alpha code. Not all the claims made in in this
document are implemented.*

This package provides two components:

1. **DjangoGistServer**: A way to develop a simple static site that uses the
   full Django templating engine, including extending some Django project's base
   templates.

2. **GistPage**: A way to take a page developed using DjangoGistServer that's
   been published as a GitHub gist and serve it at a url in some Django project.

Your static page should be in a directory that looks like this::

    index.html
    app.css
    app.js

If you use a template base that supports DjangoGistServer, you don't have to
worry about including css and js. If your base doesn't support DjangoGistServer,
add these two lines somewhere inside index.html::

    <link href="app.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="app.js"></script>

**Magic Warning:** If you have multiple css and js files, they will be
concatenated into app.css and app.js. You may have guessed at this point that it
doesn't matter what your files are named. TODO add docs on how to deal with
including third-party JS/CSS.

Static pages are published as gists. Which are great because you get history and
can package multiple files together. A sample gist is available at:

    https://gist.github.com/crccheck/93a8a020f6789d373a6c

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
