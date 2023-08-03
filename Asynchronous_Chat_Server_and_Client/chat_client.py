import asyncio
import websockets

async def handle_message():
    uri = "ws://localhost:8765"
    

    async with websockets.connect(uri) as websocket:
        
        

        print("Enter 'exit' to exit")
        
        while True:
            
          
            message = input("Enter message - ")
            if message == "exit":
                break
            
            
            await websocket.send(message)
            
            response = await websocket.recv()
            if response != "":
                print(f"Received response: {response}")
            else:
                print()

asyncio.get_event_loop().run_until_complete(handle_message())

