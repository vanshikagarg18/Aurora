import os
from playsound import playsound as ps
import eel
from command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re

# Playing assiatnt sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assests\\start_sound.mp3"
    ps(music_dir)

def openCommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    if query !="":
        speak("Opening " +query)
        os.system('start '+query)
    else:
        speak("Not Found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    #regular expression to capture sing name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #re.search to find match in command...... re = regular expression
    match = re.search(pattern, command,re.IGNORECASE)
    #if match found, return extracted song name else return none
    return match.group(1) if match else None