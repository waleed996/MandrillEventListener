from django.urls import path

from mandrill_event_listener.views.v1.webhooks.mandrill_email_action_updates_controller import UserEmailActionUpdatesViewSet

urlpatterns = [
    path('user_email_action_updates', UserEmailActionUpdatesViewSet.as_view({'post': 'post'}))
]
