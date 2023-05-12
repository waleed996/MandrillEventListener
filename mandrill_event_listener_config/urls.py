from django.urls import path, include

from mandrill_event_listener.views.v1.index_controller import index

urlpatterns = [
    path('', index, name='index'),
    path('mandrill_event_listener/api/v1/', include('mandrill_event_listener.routes.webhooks.urls'))
]
