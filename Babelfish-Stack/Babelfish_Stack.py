import speech_recognition as sr
from googletrans import Translator


r = sr.Recognizer()
mic = sr.Microphone()

#harvard = sr.AudioFile('harvard.wav')
#with harvard as source:
#    audio = r.record(source)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)




try:
    print(r.recognize_google(audio))
except:
    print("Audio cannot be recognized")