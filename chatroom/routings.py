from django.urls import re_path, path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    # 也可以使用正则路径,这种方式用在群组通信当中
    # re_path(r'room/(?P<group>\w+)/$', ChatConsumer.as_asgi()),
    path('chat/room/<str:group>/', ChatConsumer.as_asgi()),
]
