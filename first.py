import pyjokes
import pyttsx3
import os

joke= pyjokes.get_joke()
engine = pyttsx3.init()
engine.say("Today programming joke is: "+joke)
print(joke)
engine.runAndWait()
di='/Python'
content =os.listdir(di)
for item in content:
    print(item)