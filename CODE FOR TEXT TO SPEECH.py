import pyttsx3
text_speech=pyttsx3.init()
    
answer=input("enter to speak")
text_speech.say(answer)
text_speech.runAndWait()

#OR

import pyttsx3
engine=pyttsx3.Engine()
engine.say("aman")
engine.runAndWait()
