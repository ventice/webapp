from channels.generic.websocket import AsyncWebsocketConsumer

class RequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        return await self.accept()
    
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def close(self, code=None):
        return await super().close(code)
    
    async def receive(self, text_data=None, bytes_data=None):
        return await self.send(text_data=''.join(reversed(text_data)))
    