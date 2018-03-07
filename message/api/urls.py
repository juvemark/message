from django.conf.urls import url
from message.api import api

urlpatterns = [
    # /api/v1/echo/
    url(r'^v1/echo/', api.echo_message, name='echo_message'),
]
