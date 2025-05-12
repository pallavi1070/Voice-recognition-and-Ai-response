# Voice Recognition and AI Response Project

## Introduction

This is a Voice Recognition and AI Response Project developed using Python. The project acts as an interactive voice assistant that listens to the user's speech, converts it to text, generates an intelligent response using OpenAI's API, and provides an audio response using Google Text-to-Speech (gTTS).

## Features

* Real-time voice recognition using Google Speech API.
* AI-powered response generation using OpenAI's GPT-3.5.
* Text-to-Speech conversion using Google Text-to-Speech (gTTS).
* Audio playback using Pygame.
* Error handling for speech recognition, OpenAI API, and audio playback.

## How It Works

1. The application captures user speech through the microphone.
2. Converts the speech to text using Google Speech Recognition API.
3. The text is sent to OpenAI’s API to generate a response.
4. The generated response is converted into speech using gTTS.
5. The response audio is played back to the user using Pygame.

## Prerequisites

* Python installed on your system.
* An OpenAI API key.
* Required Python libraries: `SpeechRecognition`, `gTTS`, `pygame`, and `openai`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/voice-recognition-ai.git
   cd voice-recognition-ai
   ```
2. Install the required libraries:

   ```bash
   pip install SpeechRecognition gTTS pygame openai
   ```
3. Set your OpenAI API key in the script:

   ```python
   openai.api_key = "your-openai-api-key"
   ```

## Usage

* Run the script:

  ```bash
  python your_script_name.py
  ```
* Speak when prompted, and the assistant will respond with a voice reply.

## Error Handling

* If the audio is not recognized, it will display an error message.
* If there is an issue with the OpenAI API, an error message will be shown.
* If audio playback fails, it will skip the audio response without crashing.

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

## Acknowledgements

* Google Speech Recognition for voice-to-text.
* OpenAI for AI-based text generation.
* gTTS for text-to-speech conversion.
* Pygame for audio playback.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.



