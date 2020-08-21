from colorama import Fore
from welcome import welcome_msg
import pyttsx3
import os
from help_module import helping
import random

import  welcome
welcome.opening()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(text):
	engine.say(text)
	engine.runAndWait()

os.system("cls")

name = "enter the command: "
thankyoumessages = ["For You Sir Always"]
msg = welcome_msg()
print(Fore.GREEN + msg + Fore.RESET)
speak(msg)

while(True):
    x = input(Fore.RED + name + Fore.RESET)

    if len(x) <= 0:
        print(Fore.CYAN + "Please Enter a command" + Fore.RESET)
        speak("Please Enter a command")

    if "bye" in x or "quit" in x or "cya" in x or "exit" in x:
        print(Fore.CYAN + "Bye! sir" + Fore.RESET)
        speak("Bye!! See You Soon")
        exit()

    if "Made you" in x or "You" in x or "made" in  x:
       ## print(Fore.CYAN + "Sparsh Kishore kumar made me " + Fore.RESET)
        speak("Sparsh Kishore kumar made me")

    if "linuxworld" in x:
       ## print(Fore.CYAN + "i want to thank vimal daga sir and linux world informatics " + Fore.RESET)
        speak("i want to thank vimal daga sir and linux world informatics ")

    if "help" in x:
        helping()
        speak("I can help you with above things")
        
    if "love" in x:

        speak("I love you too sir.")

    elif "thank" in x or "thanks" in x:
        p = random.choice(thankyoumessages)
        print(Fore.CYAN + p + Fore.RESET)
        speak(p)


    elif ( "run" in x or "execute" in x or "open" in x ) and "chrome" in x:
        print(Fore.CYAN + "Opening Chrome" + Fore.RESET)
        speak("Opening Chrome")
        os.system("chrome")

    elif ( "run" in x or "execute" in x or "open" in x ) and ( "code" in x or "vs code" in x or "vscode" in x ):
        print(Fore.CYAN + "Opening VS Code" + Fore.RESET)
        speak("Opening VS Code")
        os.system("code")

    elif ("run" in x or "execute" in x or "open" in x ) and ( "editor" in x or "notepad" in x or "text" in x ):
        print(Fore.CYAN + "Opening Notepad" + Fore.RESET)
        speak("Opening Notepad")
        os.system("notepad")


    
    

