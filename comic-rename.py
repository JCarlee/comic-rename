import tkinter as tk
from tkinter import filedialog
import os
import re


def main():
    a = tk.Tk()
    a.withdraw()

    # Select folder
    comic_folder = filedialog.askdirectory()

    for root, dirs, files in os.walk(comic_folder):
        for file in files:
            x = re.search(r'\([0-9][0-9][0-9][0-9]\)', file)
            try:
                x.span()
            except:
                continue
            xspan = x.span()
            os.rename(os.path.join(root, file), os.path.join(root, file[:xspan[1]] + file[-4:]))


if __name__ == '__main__':
    main()
