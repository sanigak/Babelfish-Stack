import speech_recognition as sr
from googletrans import Translator

import pyttsx3


r = sr.Recognizer()

#NOTE: I needed to set the mic to 1, rather than default, because I was using a headset.
mic = sr.Microphone(device_index=1)

#harvard = sr.AudioFile('harvard.wav')
#with harvard as source:
#    audio = r.record(source)

print(sr.Microphone.list_microphone_names())

with mic as source:

    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)

voiceCapture = ""


try:
    voiceCapture = str(r.recognize_google(audio))
except:
    print("Audio cannot be recognized")






translator = Translator()

ans = translator.translate(voiceCapture, src='en', dest='de')

translationResult = ans.text




germanID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"


engine = pyttsx3.init()
engine.setProperty('voice', germanID)


engine.say(translationResult)
engine.runAndWait()