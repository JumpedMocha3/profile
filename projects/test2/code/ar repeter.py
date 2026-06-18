import speech_recognition as sr
from gtts import gTTS
import pygame
import os

def recognize_arabic_speech():
    """Capture Arabic speech from microphone and convert to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("تكلم بالعربية الآن...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="ar-AR")
            print(f"قلت: {text}")
            return text
        except sr.UnknownValueError:
            print("لم أستطع فهم ما قلت")
            return None
        except sr.RequestError:
            print("حدث خطأ في الاتصال بالإنترنت")
            return None

def speak_arabic(text):
    """Convert Arabic text to speech and play it"""
    tts = gTTS(text=text, lang="ar")
    tts.save("response.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Clean up
    pygame.mixer.quit()
    os.remove("response.mp3")

# Main program
if __name__ == "__main__":
    while True:
        # Listen for Arabic speech
        arabic_text = recognize_arabic_speech()
        
        if arabic_text:
            # Repeat what was said
            print("سأكرر ما قلته...")
            speak_arabic(arabic_text)
        
        # Ask to continue
        cont = input("هل تريد الاستمرار؟ (y/n): ").lower()
        if cont != 'y':
            break