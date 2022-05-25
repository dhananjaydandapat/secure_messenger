"""
ASGI config for secure_massenger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import secure_massenger.messenger.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secure_massenger.settings')
django.setup()
# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            secure_massenger.messenger.routing.websocket_urlpatterns
        )
    ),
})

