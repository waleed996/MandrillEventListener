from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from mandrill_event_listener.constants import WebsocketGroups


class UserEmailActionUpdatesConsumer(WebsocketConsumer):

    def connect(self):
        """Accept incoming connection from client"""

        # Add client to the user email action updates group
        async_to_sync(self.channel_layer.group_add)(
            WebsocketGroups.USER_EMAIL_ACTION_UPDATES_GROUP,
            self.channel_name
        )

        self.accept()

    def send_update(self, event):
        """Send data to connected clients"""
        message = event['update']['message']
        self.send(message)

