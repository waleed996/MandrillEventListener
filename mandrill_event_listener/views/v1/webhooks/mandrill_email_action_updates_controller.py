import json
from urllib.parse import unquote_plus

from common.libs.response import api_response
from mandrill_event_listener.components.mandrill_email_action_updates_component import MandrillEmailActionUpdatesComponent
from mandrill_event_listener.views import PublicMandrillEventListenerViewSet


class UserEmailActionUpdatesViewSet(PublicMandrillEventListenerViewSet):

    def post(self, request):
        """Webhook api to receive user email action updates from mandrill"""

        # Decode mandrill request body and load in a dict
        request_data = json.loads(unquote_plus(request.body.decode('utf-8')).split("mandrill_events=")[-1])

        # Log received request data, logging can also be done in dispatch method at base view level
        print(request_data)

        try:
            # Handle events, multiple events can be sent in one call
            for event in request_data:
                MandrillEmailActionUpdatesComponent().handle(data=event)

        # Catch any specific custom defined exceptions etc
        except Exception as error:
            # Perform any error handling
            # db_session.rollback() ... etc
            return api_response(data={"status": "FAILURE"})

        return api_response(data={"status": "SUCCESS"})

