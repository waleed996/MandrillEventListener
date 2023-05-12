from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from mandrill_event_listener.components.base import MandrillEventBaseComponent
from mandrill_event_listener.constants import WebsocketGroups, MandrillEventTypes


class MandrillEmailActionUpdatesComponent(MandrillEventBaseComponent):

    def handle(self, data):
        """Handle webhook update"""

        # Save webhook event
        self.save_event(event_id=data["_id"], event_type=MandrillEventTypes.USER_EMAIL_ACTION_UPDATES, event_data=data)

        # Send updates to client in group
        MandrillEmailActionUpdatesComponent.send_user_email_action_update(message=data)

    @staticmethod
    def send_user_email_action_update(message):
        """
        Send an update to the user email action updates consumer group
        :param message: str message to be sent
        """

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            WebsocketGroups.USER_EMAIL_ACTION_UPDATES_GROUP,
            {
                'type': 'send_update',
                'update': {
                    'message': str(message)
                }
            }
        )

