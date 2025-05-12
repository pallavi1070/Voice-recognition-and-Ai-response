INTRODUCTION

This is a Voice Recognition and AI Response Project developed using Python. The project acts as an interactive voice assistant that listens to the user's speech, converts it to text, generates an intelligent response using OpenAI's API, and provides an audio response using Google Text-to-Speech (gTTS).

FEATURES

  - Real-time voice recognition using Google Speech API.

  - AI-powered response generation using OpenAI's GPT-3.5.

  - Text-to-Speech conversion using Google Text-to-Speech (gTTS).

  - Audio playback using Pygame.

  - Error handling for speech recognition, OpenAI API, and audio playback.

HOW IT WORKS

  - The application captures user speech through the microphone.

  - Converts the speech to text using Google Speech Recognition API.

  - The text is sent to OpenAI’s API to generate a response.

  - The generated response is converted into speech using gTTS.

  - The response audio is played back to the user using Pygame.

PREREQUISITES

  - Python installed on your system.

  - An OpenAI API key.

  - Required Python libraries: SpeechRecognition, gTTS, pygame, and openai.

INSTALLATION

  - Clone the repository:

        git clone https://github.com/your-username/voice-recognition-ai.git
        cd voice-recognition-ai

  - Install the required libraries:

  - pip install SpeechRecognition gTTS pygame openai

  - Set your OpenAI API key in the script:

  - openai.api_key = "your-openai-api-key"

  - Usage

RUN THE SCRIPTS :

  - python your_script_name.py

  - Speak when prompted, and the assistant will respond with a voice reply.

ERROR HANDLING

  - If the audio is not recognized, it will display an error message.

  - If there is an issue with the OpenAI API, an error message will be shown.

  - If audio playback fails, it will skip the audio response without crashing.


ACKNOWLEDGEMENTS:

  - Google Speech Recognition for voice-to-text.

  - OpenAI for AI-based text generation.

  - gTTS for text-to-speech conversion.

  - Pygame for audio playback.

CONTRIBUTING

  - Contributions are welcome! Feel free to open an issue or submit a pull request.


