from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import database, models, auth
from datetime import datetime

router = APIRouter()
connections = set()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, user=Depends(auth.get_current_user), db: AsyncSession = Depends(database.get_db)):
    await websocket.accept()
    connections.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            msg = models.Message(sender_id=user.id, content=data, timestamp=datetime.utcnow())
            db.add(msg)
            await db.commit()
            for conn in connections:
                await conn.send_text(f"{user.username}: {data}")
    except:
        connections.remove(websocket)
