#installed an external module and 
# performed an operation on it

import pyttsx3 # type: ignore
engine = pyttsx3.init()
engine.say("My name is Ravleen Kaur")
engine.runAndWait()