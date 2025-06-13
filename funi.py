import time
import platform
import os
import subprocess
import ctypes
import shutil
import tkinter as tk
import webbrowser
from tkinter import messagebox

sus_verbs = ["fuck", "suck", "vaginal", "bang", "penetrate",
             "destroy", "molest", "violate", "clap", "rail", "peg"]
family_nouns = ["mom", "mother", "sister", "brother", "dad",
                "father", "grandma", "grandpa", "dog", "cat", "pet", "car"]


def system_alert(title: str, message: str):
    """
    Try to raise a scary-looking system-level popup on Windows, macOS, or Linux.
    Falls back to a tkinter warning box if native tools aren’t available.
    """
    system = platform.system()

    try:
        # ---------- Windows ----------
        if system == "Windows":
            # System-modal, yellow warning icon
            MB_ICONWARNING = 0x30
            MB_SYSTEMMODAL = 0x1000
            ctypes.windll.user32.MessageBoxW(
                0, message, title, MB_ICONWARNING | MB_SYSTEMMODAL
            )

        # ---------- macOS ----------
        elif system == "Darwin":
            # “as critical” = red stop sign; requires AppleScript (built-in)
            os.system(
                f'''osascript -e 'display alert "{title}" message "{
                    message}" as critical buttons {{"OK"}} default button 1' '''
            )

        # ---------- Linux / *nix ----------
        else:
            # Try Zenity (GNOME) first
            if shutil.which("zenity"):
                os.system(
                    f'''zenity --warning --title="{title}
                        " --text="{message}" --width=400'''
                )
            # Fallback: notify-send (less intrusive)
            elif shutil.which("notify-send"):
                os.system(
                    f'''notify-send "{title}" "{message}
                        " --icon=dialog-warning'''
                )
            # Final fallback: tkinter
            else:
                raise RuntimeError("No native popup utility found")

    except Exception:
        # tkinter fallback for any OS
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning(title, message)
        root.destroy()


print("Funni mad lib gaem v1")
verb = input("Enter a verb (ie: run, not running or ran): ")
noun = input("Enter a singular noun: ")
adj = input("Enter an adjective: ")
print("I tried to " + verb + " your " + noun + ", but it was too " + adj + ".")
print("very funni wahoo")
input("Did you think it was funny? ")
input("Did you? ")
input("DID YOU?! ")
survey1 = input("Y/N ").strip().lower()
if (survey1 == "y"):
    print("Yay! YOU BETTER HAVE BEEN HONEST, OR I WILL LEAK THESE RESPONSES.")
    if verb.lower() in sus_verbs and noun.lower() in family_nouns:
        print("DON'T THINK I DIDN'T SEE THAT YOU...")
        time.sleep(1.5)
        print("Oh.")
        time.sleep(0.5)
        print("OH GOD.")
        time.sleep(1.5)
        print("YOU TRIED TO " + verb.upper() + " YOUR " +
              noun.upper() + ", BUT IT WAS TOO " + adj.upper() + ".")
        time.sleep(1)
        print("Just...")
        time.sleep(0.5)
        print("wow.")
        time.sleep(1.5)
        print("That's all I have to say. Just be glad you hadn't said no to my survey. I might have had to... report this. Just... wow...")
        quit()
    elif verb.lower() in sus_verbs:
        time.sleep(1)
        print("DON'T THINK I DIDN'T SEE THAT YOU TRIED TO " + verb.upper() + " YOUR " +
              noun.upper() + ", BUT IT WAS TOO " + adj.upper() + ", You horny WEIRDO.")
        quit()
    else:
        quit()
elif (survey1 == "n"):
    print("fuck you, I know what you like...")
    time.sleep(1.5)
    if verb.lower() in sus_verbs:
        print("Wha..WHAT THE FUCK")
        time.sleep(1)
        print("YOU TRIED TO " + verb.upper() + " YOUR " +
              noun.upper() + " BUT IT WAS TOO " + adj.upper() + "?!")
        time.sleep(1)
        print("YEAH I SEE YOU BITCH, WEIRDO")
        time.sleep(1)
        if verb.lower() in sus_verbs and noun.lower() in family_nouns:
            print("You know what?")
            system_alert("Illegal Activity Dectected",
                         "Activity has been reported to the FBI.")
            time.sleep(1)
            print("YEAH. I THOUGHT SO.")
            quit()
        else:
            quit()
    else:
        print("huh. you actually weren't that sus. BUT I'M STILL WATCHING YOU... BITCH! I'LL GET YOU NEXT TIME!!")
        quit()
else:
    print("FOLLOW DIRECTIONS, BITCH")
    time.sleep(2.5)
    print("...fine. I'll give you ONE MORE CHANCE.")
    survey2 = input("Y/N. LAST CHANCE. ").strip().lower()
    if (survey2 == "y"):
        print("Finally... You made the right choice. You decided that not being STUPID was a good idea. I'm proud. Now time to check your responses, I kinda forgot what you sent.")
        if verb.lower() in sus_verbs and noun.lower() in family_nouns:
            time.sleep(1.5)
            print("Oh.")
            time.sleep(0.5)
            print("OH GOD.")
            time.sleep(1.5)
            print("YOU TRIED TO " + verb.upper() + " YOUR " +
                  noun.upper() + ", BUT IT WAS TOO " + adj.upper() + ".")
            time.sleep(1)
            print("I...")
            time.sleep(0.5)
            print("I CAN'T EVEN WITH YOU AT THIS POINT!")
            time.sleep(1.5)
            print("YOU PRETEND TO BE AN IDIOT, AND THEN YOU GO AND SAY CREEPY SHIT LIKE " +
                  verb.upper() + "ING YOUR " + noun.upper() + ".")
            time.sleep(0.5)
            print("You know what?")
            system_alert("Illegal Activity Dectected",
                         "Activity has been reported to the FBI.")
            time.sleep(1)
            print("YEAH. I THOUGHT SO.")
            quit()
        elif verb.lower() in sus_verbs:
            time.sleep(1)
            print("YOU TRIED TO " + verb.upper() + " YOUR " +
                  noun.upper() + ", BUT IT WAS TOO " + adj.upper() + ". THAT'S REALLY WEIRD, HORNY BITCH. I might have had to report you if you had said no.")
            quit()
        else:
            time.sleep(1.5)
            print("Hey, nice job! You stayed safe this time. But I'm ALWAYS WATCHING. AND I DO NOT LIKE HOW YOU PLAYED DUMB.")
            quit()
    elif (survey2 == "n"):
        time.sleep(1.5)
        print("I mean, I'm glad you stopped PRETENDING TO BE FUCKING STUPID, but WHY DID YOU SAY NO?! THAT IS NOT THE CORRECT ANSWEEEEERRRRR! Time to check your inputs! I forgot what you sent, but if there's anything REMOTELY GROSS, I WILL GET MY REVENGE!!")
        time.sleep(1.5)
        if verb.lower() in sus_verbs and noun.lower() in family_nouns:
            print("..OH MY GOD... FUCKING GROSS!")
            time.sleep(1.5)
            print("YOU TRIED TO " + verb.upper() +
                  " YOUR " + noun.upper() + "?! DISGUSTING!")
            time.sleep(1)
            print("AND YOU MADE FUN OF MY JOKES TOO! ANNOYING BITCH!")
            time.sleep(1.5)
            print("I'M GOING TO TELL EVERYONE ABOUT THIS!")
            time.sleep(1)
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=H58vbez_m4E")
            time.sleep(5)
            system_alert("A Warrant has been put out for your arrest, and Kendrick is hunting you!",
                         "Tryna strike a chord, AND IT'S PROBABLY A MINORRRRRR!")
            time.sleep(1)
            print("TAKE THAT, BITCH!")
            quit()
        elif verb.lower() in sus_verbs:
            print("Wha..WHAT THE FUCK")
            time.sleep(1)
            print("YOU TRIED TO " + verb.upper() + " YOUR " +
                  noun.upper() + " BUT IT WAS TOO " + adj.upper() + "?!")
            time.sleep(1)
            print("YEAH I SEE YOU BITCH, WEIRDO")
            time.sleep(1)
            print("You know what, YOU ANNOYED ME ENOUGH, WEIRDO.")
            system_alert("Illegal Activity Dectected",
                         "Activity has been reported to the FBI.")
            time.sleep(1)
            print("YEAH. I THOUGHT SO, HORNY BITCH.")
            quit()
        else:
            print("You may have kept clean this time, but why did you PLAY STUPID WITH ME AND ALSO MAKE FUN OF MY JOKES?!")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("FUCK YOU!")
            quit()
    else:
        time.sleep(3)
        print("YOU... YOU LITTLE...")
        time.sleep(0.5)
        print("I GAVE YOU TWO CHANCES. TWO!")
        time.sleep(1)
        print("AND YET... AND YET...")
        time.sleep(1.5)
        print("You... YOU CAN'T FOLLOW BASIC INSTRUCTIONS?!")
        time.sleep(1)
        input("ARE YOU JUST... STUPID OR SOMETHING?! Y/N ")
        time.sleep(0.5)
        print("HONESTLY, IT DOESN'T EVEN MATTER!")
        time.sleep(2)
        print("JUST...")
        time.sleep(0.5)
        print("JUST...")
        time.sleep(1)
        print("FUCK OFF ALREADY!")
        time.sleep(0.5)
        print("I'VE HAD IT!")
        time.sleep(1.5)
        print("Opening distract.py...")
        time.sleep(1)
        webbrowser.open_new_tab(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # rickroll
        time.sleep(8)
        system_alert(
            "Screw You.", "Reported to... OSHA, or something. I genuinely do not care.")
        time.sleep(3.5)
        print("Just... GO AWAY!")
        time.sleep(0.5)
        quit()
