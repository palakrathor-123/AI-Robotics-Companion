from fastapi import APIRouter, WebSocket
from core.engine import process_interaction

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # process
        result = process_interaction(data)
        # send reply 
        await websocket.send_json(result)