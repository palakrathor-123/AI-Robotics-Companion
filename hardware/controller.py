from services.ai_services import get_ai_response
from services.speech_services import speech_to_text, text_to_speech

user_input = speech_to_text()

response = get_ai_response(user_input)

text_to_speech(response)

print(response)