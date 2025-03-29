import os
import webbrowser
from playsound import playsound as ps
import eel
from command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re
import sqlite3

conn = sqlite3.connect("aurora.db")
cursor = conn.cursor()

# Playing assiatnt sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assests\\start_sound.mp3"
    ps(music_dir)

def openCommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")



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