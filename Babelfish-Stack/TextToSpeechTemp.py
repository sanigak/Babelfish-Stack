import pyttsx3


germanID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"


engine = pyttsx3.init()
engine.setProperty('voice', germanID)


engine.say("guten tag")
engine.runAndWait()