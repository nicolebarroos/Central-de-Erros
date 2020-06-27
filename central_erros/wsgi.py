"""
WSGI config for central_erros project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "central_erros.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()