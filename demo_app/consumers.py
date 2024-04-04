import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.conf import settings


class OpenConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = settings.WS_OPEN_ROOM

        # Join a group
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "open_message", "message": message}
        )

    # Receive message from room group
    def open_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))


class TasksConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = settings.WS_TASKS_ROOM

        # Join a group
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "task_message", "message": message}
        )

    # Receive message from room group
    def task_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))


class PrivateConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope["url_route"]["kwargs"]["group_name"]

        # Join a group
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "private_message", "message": message}
        )

    # Receive message from room group
    def private_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
