# app/ui_dashboard.py

import sys
import os
import time

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import streamlit as st

from services.ai_services import get_ai_response

from services.speech_services import (
    speech_to_text,
    text_to_speech
)

from streamlit_mic_recorder import mic_recorder


# --------------------------------
# PAGE TITLE
# --------------------------------
st.title("🤖 AI Robotics Companion")


# --------------------------------
# MIC BUTTON
# --------------------------------
audio = mic_recorder(
    start_prompt="🎤 Click to Speak",
    stop_prompt="⏹️ Stop Recording",
    key='mic'
)


# --------------------------------
# VOICE INPUT LOGIC
# --------------------------------
if audio:

    st.audio(audio['bytes'])

    start_time = time.time()

    with st.spinner("Robot is Listening & Thinking..."):

        # --------------------------------
        # SPEECH TO TEXT
        # --------------------------------
        user_query = speech_to_text(audio['bytes'])

        st.write(f"🧑 You Said: {user_query}")

        # --------------------------------
        # AI RESPONSE
        # --------------------------------
        ai_response = get_ai_response(user_query)

        # --------------------------------
        # TEXT TO SPEECH
        # --------------------------------
        audio_file = text_to_speech(ai_response)

        latency = round(time.time() - start_time, 2)

        # --------------------------------
        # DISPLAY RESPONSE
        # --------------------------------
        st.write(f"🤖 Robot: {ai_response}")

        # --------------------------------
        # PLAY ROBOT VOICE
        # --------------------------------
        st.audio(audio_file, autoplay=True)

        # --------------------------------
        # PRAVEEN SIR LATENCY LOGIC
        # --------------------------------
        st.metric(
            label="Latency",
            value=f"{latency} sec"
        )


# --------------------------------
# TEXT CHAT INPUT
# --------------------------------
user_text = st.chat_input("Ask something to the Robot...")


if user_text:

    start_time = time.time()

    with st.spinner("Robot is Thinking..."):

        ai_response = get_ai_response(user_text)

        audio_file = text_to_speech(ai_response)

        latency = round(time.time() - start_time, 2)

        st.write(f"🧑 You: {user_text}")

        st.write(f"🤖 Robot: {ai_response}")

        st.audio(audio_file, autoplay=True)

        st.metric(
            label="Latency",
            value=f"{latency} sec"
        )