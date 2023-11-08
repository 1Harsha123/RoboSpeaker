# import os

# print("This robospeaker is created by Harsha, Thanks for using this.")
# x = input("please enter what you want to speak: ")
# command = f"say{x}"
# os.system(command)


import pyttsx3
import os

print("This robospeaker is created by Harsha,Thanks for using this.")
while(True):
    x=(input("Enter text:"))
    if x=="quite":
        engine=pyttsx3.init()
        engine.say("Okay,Goodbye")
        engine.runAndWait()
        break
    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()