from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync  # 异步转同步


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()  # 服务器允许客户端创建连接

        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)

    def websocket_receive(self, message):
        # self.send(text)  # 服务端向（当前）前端回消息

        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_send)(group, {'type': 'xx.oo', 'message': message})

    def xx_oo(self, message):
        text = message['message']['text']
        self.send(text)  # 服务端向（组内每个）前端回消息

    def websocket_disconnect(self, message):
        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        raise StopConsumer()
