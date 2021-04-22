import moviepy.editor as mp
import speech_recognition as sr
from datetime import datetime


def processVideo(path):
    clip = mp.VideoFileClip(path)
    now = datetime.now()
    myTimeStamp = now.strftime("%d%m%Y%H%M%S")
    clip.audio.write_audiofile("./assets/" + myTimeStamp + ".wav")
    filename = "./assets/" + myTimeStamp + ".wav"
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
