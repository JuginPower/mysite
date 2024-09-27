"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from pathlib import Path
from django.core.asgi import get_asgi_application
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
environment = env("DJANGO_ENVIRONMENT", default="development")

if environment == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_dev')

application = get_asgi_application()
