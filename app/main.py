from fastapi import FastAPI
from api import websocket

app = FastAPI(title="AI Robotics Platform")


app.include_router(websocket.router)

@app.get("/")
def home():
    return {"message": "AI-Robotics System is Online"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)