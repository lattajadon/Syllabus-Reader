from os import getcwd
import sylRead
import FolderChooser

main_directory = getcwd()
FolderChooser.button_root()
user_directory = FolderChooser.browse_button()

print(main_directory)
print(user_directory)

sylRead.getPdfList(user_directory, main_directory)


