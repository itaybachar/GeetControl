import asyncio
import websockets
import socket

#Get machine info on network
hostname = socket.gethostname()

ip = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # doesn't even have to be reachable
    s.connect(('1.255.255.255', 1))
    ip = s.getsockname()[0]
except:
    ip = ''
finally:
    s.close()

# create handler for each connection
 
async def handler(websocket, path):
    while True:
        data = await websocket.recv()
        print(data)
        if(data == "CLOSE"):
            reply = f"Closing server..."
            await websocket.send(reply)
            return
        elif(data=="GET_INFO"):
            reply  = f"{hostname}|{ip}"
            await websocket.send(reply)
            return
        else:
            reply = f"Data recieved as:  {data}!"
            await websocket.send(reply)
 
start_server = websockets.serve(handler, "0.0.0.0", 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()