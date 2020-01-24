import tkinter as tk
from tkinter import filedialog
import os
import shutil

a = tk.Tk()
a.withdraw()

xmen = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Dawn of X"
avengers = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Avengers"
spiderman = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Spider Man"
cosmic = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Cosmic"
other_marvel = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Other Marvel"
events = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_Events"
starwars = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/_StarWars"
reviewdelete = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/Comics/__ReviewDelete"

dupes = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/ComicDupes"
if not os.path.exists(dupes):
    os.mkdir(dupes)

multi = r"/Users/carlosbell/Library/Mobile Documents/com~apple~CloudDocs/ComicMultiMatch"
if not os.path.exists(multi):
    os.mkdir(multi)


# --------- DEFINE LISTS ---------
# Use only lower case values
list_x = ["dead man logan", "x-men", "wolverine", "x-force", "new mutants", "fallen angels", "marauders", "excalibur",
          "house of x", "powers of x"]
list_av = ["strikeforce", "jane foster", "doctor strange", "hawkeye", "thor", "star", "avenger", "hulk", "black widow",
           "champions", "fantastic four", "captain america", "ms. marvel", "captain marvel", "iron man", "loki",
           "black panther", "ironheart", "invisible woman", "future foundation"]
list_sp = ["carnage", "venom", "spider", "black cat", "mary jane", "morbius"]
list_co = ["galaxy", "annihilation", "nova", "silver surfer", "quill", "yondu", "thanos", "eternals"]
list_othrm = ["punisher", "moon knight", "invaders", "daredevil", "conan", "runaways", "ghost rider", "doctor doom",
              "alpha flight", "agents of atlas"]
list_event = ["contagion", "absolute carnage", "annihilation", "ravencroft", "the end", "marvels x", "2099",
              "history of the marvel universe", "marvel team-up", "marvel comics present", "zombies"]
list_starwars = ["star wars"]
list_review = ["aero", "squirrel girl", "sword master", "tarot", "gwenpool", "marvel preview"]

# List of all lists
list_lists = [list_x, list_av, list_sp, list_co, list_othrm, list_event, list_starwars, list_review]


def comic_move(start, dest):
    shutil.move(start, dest)
    print("{0} moved to {1}.".format(start, dest))


# Prompt user to select starting folder
comic_folder = filedialog.askdirectory()
filenames = []

for root, dirs, files in os.walk(comic_folder):
    for file in files:
        if file not in filenames:  # If filename unique
            filenames.append(file)  # Add unique filename to filenames
        elif file in filenames:  # If filename not unique
            comic_move(os.path.join(root, file), dupes)  # Move to dupe folder
            break
        if any(x in file.lower() for x in list_x):  # If any values in list_x are in filename, execute next line
            dbl_chk = list_lists.pop(0)  # Create list of all other possible values
            if any(y in file.lower() for y in dbl_chk):  # If match any other values
                comic_move(os.path.join(root, file), multi)  # Move to multi folder
            else:
                comic_move(os.path.join(root, file), xmen)
        if any(x in file.lower() for x in list_av):
            dbl_chk = list_lists.pop(1)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), avengers)
        if any(x in file.lower() for x in list_sp):
            dbl_chk = list_lists.pop(2)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), spiderman)
        if any(x in file.lower() for x in list_co):
            dbl_chk = list_lists.pop(3)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), cosmic)
        if any(x in file.lower() for x in list_othrm):
            dbl_chk = list_lists.pop(4)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), other_marvel)
        if any(x in file.lower() for x in list_event):
            dbl_chk = list_lists.pop(5)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), events)
        if any(x in file.lower() for x in list_starwars):
            dbl_chk = list_lists.pop(6)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), starwars)
        if any(x in file.lower() for x in list_review):
            dbl_chk = list_lists.pop(7)
            if any(y in file.lower() for y in dbl_chk):
                comic_move(os.path.join(root, file), multi)
            else:
                comic_move(os.path.join(root, file), reviewdelete)
