import asyncio
import websockets

clients = []

async def register(websocket):
    clients.append(websocket)
    print("Client connected")

async def unregister(websocket):
    clients.remove(websocket)
    print("Client  disconnected")

async def handle_client(websocket):
    # Выполните регистрацию клиента с уникальным client_id.
    
    await register(websocket)

    try:
        async for message in websocket:
            websocket.send("hi server")
            # Здесь можно обрабатывать входящие сообщения от клиента, если необходимо.
            print(f"Received message from client {message}")

            # Пример отправки ответного сообщения обратно клиенту.
            
            
            for client in clients:
                if client is not  websocket:
                    await client.send(message)
                
                    
    except websockets.ConnectionClosed:
        
        await unregister(websocket)
        

start_server = websockets.serve(handle_client, "localhost", 8765)
print("Server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
