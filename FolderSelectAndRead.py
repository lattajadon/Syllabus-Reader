from os import getcwd, listdir, remove
from os.path import splitext
import sylRead
import FolderChooser
import readtxt
from GoogleAPI_test import add_events

main_directory = getcwd()
FolderChooser.button_root()
user_directory = FolderChooser.browse_button()

sylRead.getPdfList(user_directory, main_directory)

docslist = listdir(user_directory)
for doc in docslist:
    if splitext(doc)[1] == ".txt":
        textfile = (user_directory + "/" + doc)
        txtcontents = readtxt.read_file(textfile)
        dates = readtxt.find_words(txtcontents)
        print(dates) # Debugging Only
        organized_dates = readtxt.organize_dates(dates)
        print(organized_dates) # Debugging Only
        proper_dates = readtxt.proper_date(organized_dates)
        print(proper_dates) # Debugging Only
        #add_events(proper_dates)
        remove(textfile)

