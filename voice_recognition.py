import speech_recognition as sr
import os
from gtts import gTTS
import pygame
import time
import openai

openai.api_key = "OPENAI_API_KEY"

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise for 1 second
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("Recognizing...")
    print("You said:", text)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can choose other models like "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "Reply like a voice assistant. Keep it brief."},
            {"role": "user", "content": text},
        ]
    )
    ans = response.choices[0].message.content
    print(ans)

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print("Error with the Google API; {0}".format(e)) # This message is now slightly inaccurate
except openai.APIError as e:
    print(f"Error with the OpenAI API: {e}")

language = "en"
tts = gTTS(text=ans, lang=language, slow=False)
tts.save("output.mp3")

# Try to initialize pygame mixer safely
try:
    pygame.mixer.init()
    mixer_initialized = True
except pygame.error as e:
    print(f"Failed to initialize mixer: {e}")
    mixer_initialized = False

if mixer_initialized:
    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        os.remove("output.mp3")
        print("File removed successfully.")

    except Exception as e:
        print(f"Error during playback or file removal: {e}")
else:
    print("Skipping audio playback due to mixer initialization failure.")
