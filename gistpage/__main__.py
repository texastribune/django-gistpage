import os
import sys


if __name__ == "__main__":
    port = 8000  # TODO
    sys.path.append(os.path.abspath('.'))
    os.environ["DJANGO_SETTINGS_MODULE"] = "example_project.settings"
    from django.core.management import call_command
    call_command('runserver', addrport="0.0.0.0:%s" % port)
    # addrport
    # shutdown_message
    # use_reloader
