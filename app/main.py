from fastapi import FastAPI, WebSocket
app = FastAPI()

@app.get('/')
def home() : 
    return {'message' : 'the api works'}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"{data}")
        