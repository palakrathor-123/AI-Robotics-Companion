import os
from dotenv import load_dotenv

# .env file ko load karne ke liye
load_dotenv()

class Settings:
    # Gemini Key
    GEMINI_API_KEY = os.getenv("AIzaSyBfIjp84Md-baydYZvUDMgrKPodkO9yuEQ")
    # ElevenLabs Key
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    # Robot IP (default de diya hai taaki error na aaye)
    ROBOT_IP = os.getenv("ROBOT_IP", "127.0.0.1")

settings = Settings()