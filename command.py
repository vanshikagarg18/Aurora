import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    print(voices)

    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False  # Keep energy threshold fixed
    r.energy_threshold = 400  

    with sr.Microphone() as source:
        print('Listening....')
        '''r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)'''
        r.adjust_for_ambient_noise(source, duration=1.0) 
        r.pause_threshold = 1.2
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        speak(query)
        return query.lower()
    except Exception as e:
        print("Could not recognize speech.")
        return ""
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return "I didn't catch that."
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return "Speech service is unavailable."
    
    
        


