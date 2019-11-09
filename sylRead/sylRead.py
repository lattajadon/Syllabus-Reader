from tikapp import TikaApp
from os import listdir, getcwd
from os.path import isdir, join

def getPdfList():
	myPath = getcwd()
	for item in listdir(myPath):
		if isdir(join(myPath, item)) and item != "tika-app-python":
			newPath = join(myPath, item)

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
