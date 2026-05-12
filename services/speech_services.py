# services/speech_services.py

import pyttsx3
import whisper
import tempfile

# Text To Speech Engine
engine = pyttsx3.init()

# Whisper Model
model = whisper.load_model("base")


# -------------------------------
# Speech To Text
# -------------------------------
def speech_to_text(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:

        temp_audio.write(audio_bytes)

        temp_audio_path = temp_audio.name

    result = model.transcribe(temp_audio_path)

    return result["text"]


# -------------------------------
# Text To Speech
# -------------------------------
def text_to_speech(text):

    output_file = "response.mp3"

    engine.save_to_file(text, output_file)

    engine.runAndWait()

    return output_file