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
   
    
    await register(websocket)

    try:
        async for message in websocket:
            websocket.send("hi server")
            
            print(f"Received message from client {message}")

            
            
            for client in clients:
                if client is not  websocket:
                    await client.send(message)
                
                    
    except websockets.ConnectionClosed:
        
        await unregister(websocket)
        

start_server = websockets.serve(handle_client, "localhost", 8765)
print("Server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
