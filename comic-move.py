import tkinter as tk
from tkinter import filedialog
import os
import shutil

a = tk.Tk()
a.withdraw()

# --------- CHANGE DESTINATION PATHS ---------
# Where files will move
xmen = r"C:\Users\john.carlee\Desktop\ComicMove\_Dawn of X"
placeholder = r"C:\Users\john.carlee\Desktop\ComicMove\CHANGE_ME"

# --------- DEFINE LISTS ---------
# Use only lower case values
list_x = ["x-men", "x-force", "new mutants"]  # Search terms to move into _Dawn of X
list_ph = ["item1", "item2"]  # Example search terms to be edited

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
        if any(x in file.lower() for x in list_x):  # If any values in list_x are in filename, execute next line
            shutil.move(os.path.join(root, file), xmen)
        elif "one item" in file.lower():  # If "one item" in filename, execute next line
            shutil.move(os.path.join(root, file), placeholder)
        elif any(x in file.lower() for x in list_ph):  # SAMPLE TEST USING LIST (list_ph)
            shutil.move(os.path.join(root, file), placeholder)
