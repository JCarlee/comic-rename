import tkinter as tk
from tkinter import filedialog
import os
import re

root = tk.Tk()
root.withdraw()

# Select folder
comic_folder = filedialog.askdirectory()

comics = []
no_files = 0
for root, dirs, files in os.walk(comic_folder):
    for file in files:
        os.rename(os.path.join(root, file), os.path.join(root, re.sub(r'\)[^.]*\.', ').', file)))
