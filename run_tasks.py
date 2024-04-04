import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from django.conf import settings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time


def main():
    channel_layer = get_channel_layer()
    i = 1
    while True:
        submit_message = f"task {i} submitted"
        async_to_sync(channel_layer.group_send)(
            settings.WS_TASKS_ROOM,
            {
                "type": "task_message",
                "message": submit_message,
            },
        )

        time.sleep(0.5)
        exc_message = f"task {i} being executed"
        async_to_sync(channel_layer.group_send)(
            settings.WS_TASKS_ROOM,
            {
                "type": "task_message",
                "message": exc_message,
            },
        )

        time.sleep(0.5)
        f_message = f"task {i} finished"
        async_to_sync(channel_layer.group_send)(
            settings.WS_TASKS_ROOM,
            {
                "type": "task_message",
                "message": f_message,
            },
        )
        i += 1
        time.sleep(0.5)


if __name__ == "__main__":
    main()
