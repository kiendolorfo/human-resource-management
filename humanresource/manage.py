#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanresource.settings')
    try:
        """ import the execute_from_command_line function from the django.core.management module. """
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        """ If it fails to import, it raises an ImportError message. """
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) 
        """ execute_from_command_line() function with the system arguments passed to the script. """
        from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
