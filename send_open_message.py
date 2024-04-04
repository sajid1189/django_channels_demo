import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from django.conf import settings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def main():
    channel_layer = get_channel_layer()

    while True:
        print("Type your message: \n")
        message = input()
        async_to_sync(channel_layer.group_send)(
            settings.WS_OPEN_ROOM,
            {
                "type": "open_message",
                "message": message,
            },
        )
        print("Message sent. ")


if __name__ == "__main__":
    main()
