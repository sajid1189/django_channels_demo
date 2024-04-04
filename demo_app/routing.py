# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/open-room/$", consumers.OpenConsumer.as_asgi()),
    re_path(r"ws/tasks/$", consumers.TasksConsumer.as_asgi()),
    re_path(r"ws/private/(?P<group_name>\w+)/$", consumers.PrivateConsumer.as_asgi()),
]