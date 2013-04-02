from optparse import OptionParser

import os
import sys


DEFAULT_PORT = 8000

if __name__ == "__main__":
    usage = "usage: python -m DjangoGistServer [options] [port]"
    parser = OptionParser(usage=usage)
    # parser.add_option()
    (options, args) = parser.parse_args()
    port = DEFAULT_PORT
    if args:
        port = args[0]
    sys.path.append(os.path.abspath('.'))
    os.environ["DJANGO_SETTINGS_MODULE"] = "gistserver_project.settings"
    from django.core.management import call_command
    call_command('runserver', addrport="0.0.0.0:%s" % port)
    # addrport
    # shutdown_message
    # use_reloader
