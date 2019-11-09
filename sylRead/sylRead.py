from tikapp import TikaApp
from os import listdir, getcwd
from os.path import isdir, join

def getPdfList():
	'''
		getPdfList will search for a folder in the current 
		directory and go through its PDFs, converting them into
		a .txt file for parsing.
	'''
	# get the current/working directory
	myPath = getcwd()

	for item in listdir(myPath):
		# if its a folder, set that to the new path
		if isdir(join(myPath, item)) and item != "tika-app-python":
			newPath = join(myPath, item)

	#using this new path, get textfiles of the pdfs
	for pdf in listdir(newPath):
		getTextFile(join(newPath, pdf))


def getTextFile(nameOfPDF):
	'''
		getTextFile("nameOfPDF") will take the PDF and output it as a textfile
	'''
	# get the Tika Object
	tika_client = TikaApp(file_jar="/home/cmput274/Documents/Syllabus-Reader/sylRead/tika-app-1.22.jar")

	# read the pdf
	with open(nameOfPDF) as fin:
		content = tika_client.extract_all_content(objectInput = fin)
		# write the pdf to a text file
		with open(nameOfPDF + ".txt", "w") as fout:
			fout.write(content)


if __name__ == "__main__":
	getPdfList()
