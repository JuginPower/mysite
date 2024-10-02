"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
print(f"environment in asgi.py: {environment}")

if environment == 'production':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_prod'

else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_dev'

print("Django Settings Modul in asgi.py:", os.environ['DJANGO_SETTINGS_MODULE'])

application = get_asgi_application()
