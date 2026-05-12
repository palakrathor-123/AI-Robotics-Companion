# AI-Robotics-Companion

## Overview
AI Robotics Companion is an intelligent AI-powered assistant project designed to interact with users through voice and text communication. The system uses Artificial Intelligence, Speech Recognition, Text-to-Speech, and automation features to create a smart robotic companion experience.

## Features
### Voice Recognition
* Converts user speech into text
* Understands voice commands
* Real-time interaction support
   
## AI Chat System
* Generates intelligent responses using AI models
* Supports conversational interaction
* Context-aware communication
  
## Text-to-Speech
* Converts AI responses into voice
* Provides human-like audio interaction
  
##  User-Friendly Dashboard
* Interactive Streamlit UI
* Easy navigation and controls
* Clean and responsive design
* 
## Automation Support
* Handles basic assistant tasks
* Can be extended for smart automation
  
## Technologies Used
### Frontend
* Streamlit
### Backend
* Python
### AI & ML Libraries
*  ollama
* SpeechRecognition
* Pyttsx3
* Whisper AI
### Additional Libraries
* OS
* Time
* Dotenv
* PyAudio
  
## Project Structure
ai-robotics-platform/
│
├── app/                        
│   ├── api/                   
│   │   ├── __init__.py
│   │   └── websocket.py        
│   │
│   ├── services/             
│   │   ├── __init__.py
│   │   ├── ai_service.py       
│   │   ├── speech_service.py   
│   │   └── robot_service.py    
│   │
│   ├── core/                   
│   │   ├── __init__.py
│   │   └── engine.py           
│   │
│   ├── config.py
│   └── main.py                
│
├── hardware/                   
│   └── controller.py          
│
├── data/                       
│   └── audio/               
│
├── .env                       
├── .gitignore                  
├── requirements.
└── README.md                   

## Installation
### Step 1: Clone Repository
Bash
git clone <repository-link>
cd AI-Robotics-Companion

### Step 2: Create Virtual Environment
Bash
python -m venv venv

### Step 3: Activate Virtual Environment
Windows
Bash
venv\Scripts\activate

### Step 4: Install Dependencies
Bash
pip install -r requirements.txt

### Environment Variables
Create a .env file and add your Gemini API Key.

### Environment
ollama

### Running the Project
Bash
streamlit run app/ui_dashboard.py

## How It Works
* Speech is converted into text
* AI model processes the request
* AI generates a response
* Response is converted into speech
* Output is displayed on dashboard
  
## Future Improvements
* Face Recognition
* Emotion Detection
* Smart Home Integration
* Multi-language Support
* Real-Time Robotics Control
  
## Advantages
* Interactive AI communication
* Easy to use interface
* Real-time response system
* Modular and scalable architecture

  ## Dashboard Overview
  <img width="1330" height="489" alt="Image" src="https://github.com/user-attachments/assets/653fae68-3f91-417f-9efd-472cb9c9aa76" />

<img width="761" height="555" alt="Image" src="https://github.com/user-attachments/assets/b147adaa-e4f1-4b15-be96-325e90da61bd" />
  
## Author
### Palak Rathore
