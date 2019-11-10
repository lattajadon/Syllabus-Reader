from tikapp import TikaApp
from os import listdir, getcwd
from os.path import isdir, join

# NEED TO MAKE PATH TO .JAR FILE FOR FILE INPUTS FOR getPdfList(<chosen file directory>)
# also add a deletion feature? Or maybe later after the parser is finalized


def getPdfList(myPath, jarPath):
	'''
		getPdfList will search for a folder in the current 
		directory (or one thats specified) and go through its 
		PDFs, converting them into a .txt file for parsing.

		Takes a directory path as an argument. If none is given, it
		will look for one in its current directory
	'''

	# if no specific path is specified, look for one inside current directory
	if myPath == (None or ''):
		myPath = getcwd()
		for item in listdir(myPath):
			# if its a folder, set that to the new path
			if isdir(join(myPath, item)) and item != "tika-app-python":
				newPath = join(myPath, item)
	else:
		newPath = myPath
	# using this new path, get textfiles of the pdfs
	for pdf in listdir(newPath):
		# MANUALLY CHANGE <newPath> TO GIVE CORRECT PATH TO .JAR FILE!!
		txtfile = getTextFile(join(newPath, pdf), jarPath)

	#return txtfile


# GETTEXTFILE'S PATH IS CURRENTLY ONLY GOING TO WORK IF THE .JAR FILE IS
# IN THE SAME DIRECTORY WITH THE FOLDER OF PDFS TO READ!!
def getTextFile(nameOfPDF, jarPath):
	'''
		getTextFile("nameOfPDF", path) will take the PDF and 
		output it as a textfile. Path will be taken and used to
		specify the .jar file needed for tika.
		Note: Needs the tika-app-1.22.jar and tika-app-python files
		and folders in the same working directory
	'''
	# get the Tika Object from current directory
	tika_client = TikaApp(file_jar = join(jarPath, "tika-app-1.22.jar"))

	# read the pdf
	with open(nameOfPDF) as fin:

		# get rid of the .pdf to change to .txt for later
		if nameOfPDF[-4:] == ".pdf":
			foutName = nameOfPDF[:-4]
		else:
			# if its not .pdf, then just keep the filename
			foutName = nameOfPDF

		content = tika_client.extract_all_content(objectInput = fin)
		# write the pdf to a text file & add .txt to it
		with open(foutName + ".txt", "w", encoding='utf-8', errors='replace') as fout:
			fout.write(content)
			return foutName+".txt"



if __name__ == "__main__":
	# test it out! input a path to a directory with PDFs to parse. 
	getPdfList()
