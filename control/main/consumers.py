import json

from channels.generic.websocket import WebsocketConsumer
#reminder: configure channel layer
        
class MainConsumer(WebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.workspace = ''
        
    def connect(self):
        self.accept()
        self.workspace = self.scope['url_route']['kwargs']['type']
        self.send(text_data=json.dumps({"message": self.workspace}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": self.workspace}))