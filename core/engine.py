from services.ai_services import get_ai_response
from services.speech_services import text_to_speech
from services.robot_service import send_robot_command # Is line ko dhyan se check karein

def process_interaction(user_input):
    # 1. AI se jawab lein
    ai_text = get_ai_response(user_input)
    
    # 2. Awaaz (Audio) generate karein
    audio_file = text_to_speech(ai_text)

    # 3. Robot Command Add karein (Jo missing tha)
    try:
        # AI text ke basis par robot ko command bhejein
        # Example: Agar AI "moving forward" bol raha hai toh robot move karega
        send_robot_command(ai_text) 
    except Exception as e:
        print(f"Robot Command failed: {e}")

    # Dashboard ko dono cheezein return karein taaki wo display kar sake
    return ai_text, audio_file