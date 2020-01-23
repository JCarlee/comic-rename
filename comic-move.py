import tkinter as tk
from tkinter import filedialog
import os
import shutil

a = tk.Tk()
a.withdraw()

# --------- CHANGE DESTINATION PATHS ---------
# Where files will move
# xmen = r"C:\Users\jcarlee\Desktop\z"
# placeholder = r"C:\Users\john.carlee\Desktop\ComicMove\CHANGE_ME"

xmen = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Dawn of X"
avengers = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Avengers"
spiderman = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Spider Man"
cosmic = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Cosmic"
other_marvel = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Other Marvel"
events = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Events"
starwars = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_StarWars"
reviewdelete = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/__ReviewDelete"

# --------- DEFINE LISTS ---------
# Use only lower case values
list_x = ["dead man logan", "x-men", "wolverine", "x-force", "new mutants", "fallen angels", "marauders", "excalibur",
          "house of x", "powers of x"]  # Search terms to move into _Dawn of X
list_av = ["strikeforce", "jane foster", "doctor strange", "hawkeye", "thor", "star", "avenger", "hulk", "black widow",
           "champions", "fantastic four", "captain america", "ms. marvel", "captain marvel", "iron man", "loki", "black panther", "ironheart", "invisible woman", "future foundation"]
list_sp = ["carnage", "venom", "spider", "black cat", "mary jane", "morbius"]
list_co = ["galaxy", "annihilation", "nova", "silver surfer", "quill", "yondu", "thanos", "eternals"]
list_othrm = ["punisher", "moon knight", "invaders", "daredevil", "conan", "runaways", "ghost rider", "doctor doom",
              "alpha flight", "agents of atlas"]
list_event = ["contagion", "absolute carnage", "annihilation", "ravencroft", "the end", "marvels x", "2099",
              "history of the marvel universe", "marvel team-up", "marvel comics present", "zombies"]
list_starwars = ["star wars"]
list_review = ["aero", "squirrel girl", "sword master", "tarot", "gwenpool", "marvel preview"]

# Prompt user to select starting folder
comic_folder = filedialog.askdirectory()
filenames = []

# Main loop
for root, dirs, files in os.walk(comic_folder):
    for file in files:
        if file not in filenames:
            filenames.append(file)
        elif file in filenames:
            gone = os.path.join(root, file)
            os.remove(gone)
            print("{0} deleted.".format(gone))
            break
        if any(x in file.lower() for x in list_x):  # If any values in list_x are in filename, execute next line
            m = os.path.join(root, file)
            shutil.move(m, xmen)
            print("{0} moved to {1}.".format(m, xmen))
        elif any(x in file.lower() for x in list_ph):  # SAMPLE TEST USING LIST (list_ph)
            shutil.move(os.path.join(root, file), placeholder)
            print

for root, dirs, files in os.walk(comic_folder):
    for file in files:
        if file not in filenames:
            filenames.append(file)
        elif file in filenames:
            gone = os.path.join(root, file)
            os.remove(gone)
            print("{0} deleted.".format(gone))
            break
        if any(x in file.lower() for x in list_x):  # If any values in list_x are in filename, execute next line
            shutil.move(os.path.join(root, file), xmen)
        if any(x in file.lower() for x in list_av):
            shutil.move(os.path.join(root, file), avengers)
        if any(x in file.lower() for x in list_sp):
            shutil.move(os.path.join(root, file), spiderman)
        if any(x in file.lower() for x in list_co):
            shutil.move(os.path.join(root, file), cosmic)
        if any(x in file.lower() for x in list_othrm):
            shutil.move(os.path.join(root, file), other_marvel)
        if any(x in file.lower() for x in list_event):
            shutil.move(os.path.join(root, file), events)
        if any(x in file.lower() for x in list_starwars):
            shutil.move(os.path.join(root, file), starwars)
        if any(x in file.lower() for x in list_review):
            shutil.move(os.path.join(root, file), reviewdelete)
