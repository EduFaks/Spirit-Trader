import websockets
from json import dumps, loads
from datetime import datetime


prices = []


class KrakenGateway:
    def __init__(self):
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect('wss://ws.kraken.com/')
        await self.receive_message()

    async def subscribe(self, pairs, subscription_type):
        if self.websocket:
            await self.websocket.send(dumps({
                "event": "subscribe",
                "pair": pairs,
                "subscription": {
                    "name": subscription_type
                }
            }))

    async def receive_message(self):
        if self.websocket:
            return await self.websocket.recv()

    async def listen(self, price_callback):
        while True:
            message = await self.receive_message()
            price = _parse_message(message)
            if not price:
                continue
            prices.append(price)
            price_callback(prices)

    async def close(self):
        if self.websocket:
            await self.websocket.close()


def _parse_message(message):
    message = loads(message)
    if not isinstance(message, list) or message[2] not in ["ticker"]:
        return

    prices_object = message[1]
    return {"ask": prices_object["a"][0], "bid": prices_object["b"][0], "time": datetime.now().timestamp()}
