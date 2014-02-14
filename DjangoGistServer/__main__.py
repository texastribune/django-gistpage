from optparse import OptionParser

import os
import sys


DEFAULT_PORT = 8000

if __name__ == "__main__":
    usage = "usage: python -m DjangoGistServer [options] [port]"
    parser = OptionParser(usage=usage)
    parser.add_option('-t', '--template-dir', dest='template_dir',
        help='Additional directory to look for templates')
    (options, args) = parser.parse_args()
    port = DEFAULT_PORT
    if args:
        port = args[0]
    if options.template_dir:
        # hacky way to pass things into settings
        os.environ['ADDITIONAL_TEMPLATE_DIR'] = options.template_dir

    sys.path.append(os.path.abspath('.'))
    os.environ["DJANGO_SETTINGS_MODULE"] = "DjangoGistServer.gistserver_project.settings"
    from django.core.management import call_command
    call_command('runserver', addrport="0.0.0.0:%s" % port)
    # addrport
    # shutdown_message
    # use_reloader
