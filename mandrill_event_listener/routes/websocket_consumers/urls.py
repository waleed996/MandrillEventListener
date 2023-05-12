from django.urls import re_path

from mandrill_event_listener.websocket_consumers.v1.user_email_action_updates_consumer import \
    UserEmailActionUpdatesConsumer


websocket_urlpatterns = [
    re_path(r'mandrill_event_listener/ws/v1/user_email_action_updates', UserEmailActionUpdatesConsumer.as_asgi())
]
