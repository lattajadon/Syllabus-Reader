from tkinter import filedialog
from tkinter import *
folderPath = ''

def browse_button():
    filename = filedialog.askdirectory()
    global folderPath
    folderPath = filename
    print(folderPath)
    root.destroy()
    return folderPath

def choose_directory():
    root = Tk()
    v = StringVar()
    button2 = Button(root, text="Select Target Folder", command=browse_button).grid(row=2, column=3)

    mainloop()