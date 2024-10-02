"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

environment = os.getenv('DJANGO_ENVIRONMENT', 'development')

if environment == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_prod')

else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_dev')

application = get_asgi_application()
