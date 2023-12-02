import asyncio
import websockets
import time

async def send_data(data):
    uri = "ws://192.168.1.25:81"  # NodeMCU'nun IP adresi ve portu

    async with websockets.connect(uri) as websocket:
        data_to_send = data
        await websocket.send(data_to_send)
        print(f"Data sent to NodeMCU: {data_to_send}")

async def main():
    counter = 0
    while True:
        await send_data("Merhaba Tubitak " + str(counter))
        counter += 1
        await asyncio.sleep(0.5)

# Asenkron kodu çalıştır
asyncio.get_event_loop().run_until_complete(main())
