from tkinter import filedialog
from tkinter import *

folderPath = ''

def browse_button():
    filename = filedialog.askdirectory()
    global folderPath
    folderPath = filename
    return folderPath

def button_root():
    root = Tk()
    v = StringVar()
    button2 = Button(root, text="Select Target Folder", command=browse_button).grid(row=2, column=3)

if __name__ == "__main__":
    button_root()
    print(browse_button())
