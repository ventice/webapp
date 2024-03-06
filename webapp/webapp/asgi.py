"""
ASGI config for webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from connectivity import routing
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        URLRouter(routing.url_patterns)
    )
})
