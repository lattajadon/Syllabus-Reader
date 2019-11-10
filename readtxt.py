import re 

def read_file(filename):
	'''
	param: filename: the name of the file we want to read from
	return: contents: the contents of the file
	'''

	file_o = open(filename,'r')
	contents = file_o.read()
	file_o.close()

	return contents

def find_word(contents):
	'''
	param: contents:  
	return: 
	'''
	dates = re.findall("Midterm|Final|Exam|Final|Assignment|Quiz|\b[A-Z].*[0-9]\b*", contents)

	return dates

if __name__ == '__main__':
	testing = read_file('test.txt')
	words = find_word(testing)
	print(words)