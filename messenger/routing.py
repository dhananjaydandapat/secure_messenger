## game/routing.py
from django.conf.urls import url
from consumer import SecureMessengerConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', SecureMessengerConsumer.as_asgi()),
]