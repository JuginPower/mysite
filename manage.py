#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
    print(f"environment in manage.py: {environment}")

    if environment == 'production':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_prod'
    else:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_dev'
    
    print("Django Settings Modul in manage.py:", os.environ['DJANGO_SETTINGS_MODULE'])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
