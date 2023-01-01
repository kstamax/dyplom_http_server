from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/main/<str:type>', consumers.MainConsumer.as_asgi()),
]