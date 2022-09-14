from gtts import gTTS
import os
n=input("what u want to speak")

mytext=n

language='en-in'

output=gTTS(text=mytext,lang=language)

output.save("output.mp3")

os.system("start output.mp3")
