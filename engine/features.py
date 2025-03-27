from playsound import playsound as ps
import eel

# Playing assiatnt sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assests\\start_sound.mp3"
    ps(music_dir)