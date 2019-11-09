from tikapp import TikaApp

def getTextFile():
	# get the Tika Object
	tika_client = TikaApp(file_jar="/home/cmput274/Documents/sylRead/tika-app-1.22.jar")

	# read the pdf
	with open("course_outline.pdf") as fin:
		content = tika_client.extract_all_content(objectInput = fin)
		# write the pdf to a text file
		with open("test.txt", "w") as fout:
			fout.write(content)


if __name__ == "__main__":
	getTextFile()
