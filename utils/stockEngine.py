from gateways.kraken import KrakenGateway


async def price_listener(price_callback):
    gateway = KrakenGateway()
    await gateway.connect()
    await gateway.subscribe(pairs=["ETH/USD"], subscription_type="ticker")
    await gateway.listen(price_callback=price_callback)
