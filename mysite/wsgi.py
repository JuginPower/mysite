"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
print(f"environment in wsgi.py: {environment}")

if environment == 'production':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_prod'

else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_dev'

print("Django Settings Modul in wsgi.py:", os.environ['DJANGO_SETTINGS_MODULE'])
application = get_wsgi_application()
