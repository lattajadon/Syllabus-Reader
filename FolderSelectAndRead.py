from os import getcwd
import sylRead
import FolderChooser
import readtxt

main_directory = getcwd()
FolderChooser.button_root()
user_directory = FolderChooser.browse_button()

txtfile = sylRead.getPdfList(user_directory, main_directory)
txtcontents = readtxt.read_file(txtfile)
dates = readtxt.find_words(txtcontents)
print(dates)
organized_dates = readtxt.organize_dates(dates)
print(organized_dates)
proper_dates = readtxt.proper_date(organized_dates)
print(proper_dates)


