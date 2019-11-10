import re 
from datetime import date

def read_file(filename):
	'''
	param: filename: the name of the file we want to read from
	return: contents: the contents of the file
	'''

	file_o = open(filename, 'r', encoding='utf-8')
	contents = file_o.read()
	file_o.close()

	return contents

def find_words(contents):
	'''
	param: contents: the contents of the file in a list 
	return: dates: a list of specific words and dates
			course: the course name as a string in a list
	'''

	#locates required content
	contents = re.sub(r"[Jj]anuary", "Jan", contents)
	contents = re.sub(r"[Ff]ebruary", "Feb", contents)
	contents = re.sub(r"[Mm]arch", "Mar", contents)
	contents = re.sub(r"[Aa]pril", "Apr", contents)
	contents = re.sub(r"[Mm]ay", "May", contents)
	contents = re.sub(r"[Jj]une", "Jun", contents)
	contents = re.sub(r"[Jj]uly", "Jul", contents)
	contents = re.sub(r"[Aa]ugust", "Aug", contents)
	contents = re.sub(r"[Ss]eptember", "Sep", contents)
	contents = re.sub(r"[Oo]ctober", "Oct", contents)
	contents = re.sub(r"[Nn]ovember", "Nov", contents)
	contents = re.sub(r"[Dd]ecember", "Dec", contents)

	dates = re.findall(r"Midterm|Final|Exam|Assignment|Quiz|Labs?|[A-Z].{2,5}.[0-9]\b|[0-9]{1-2}.[A-Z].{2-3}?\b|[0-9]{1,2}.[A-Z][a-z]{2,5}.[0-9]{4}|[0-9]{1,2}.[0-9]{1,2}.[0-9]{4}|[0-9]{4}.[0-9]{1,2}.[0-9]{1,2}", contents)

	course = re.findall(r"[A-Z][A-Za-z\s-]{1,5}\d{3}",contents)


	if len(course) > 1:
		for i in range(len(course)-1):
			course.pop()


	return (dates,course)

def organize_dates(dates):
	'''
	param: dates: the contents of a file as a list
	return: complete_list: orgonized list in lists, assigns the main words with the dates 
	'''
	word_list = ['Midterm','Final','Exam','Assignment','Quiz','Lab','Labs']

	organized= []

	for i in range(0,len(dates)):
		date = []
		if dates[i] in word_list:
			#add the main word toa seperate list
			date.append(dates[i])
			for j in range(i+1,len(dates)):
			#continue to add dates to the list until you reach another main word
				if dates[j] in word_list:
					break
				else:
					date.append(dates[j])
			# add eacj list of word anf dates to a list with the others
			organized.append(date)

	organized_list = []

	for lists in range(0,len(organized)):
	# make sure each main word has a date otherwise ignore it
		if len(organized[lists]) > 1:
			organized_list.append(organized[lists])

	complete_list = []

	for lists in organized_list:
	# ingnors any lab dates for now
		if (lists[0] == 'Lab') or (lists[0] == 'Labs'):
			complete_list = complete_list
		else:
			complete_list.append(lists)

	return complete_list

def check_duplicates(listoflists):
	'''
	param: listoflists: a list with lists in it
	return: no_duplicates: a list of lists with no duplicates in it
	'''
	no_duplicates = []
	duplicates = []

	for i in listoflists: 
		strings = ' '.join(i)
		if strings not in duplicates:
			duplicates.append(strings)

	for i in duplicates:
		add = list(i.split())

		no_duplicates.append(add)

	return no_duplicates


def proper_date(organized_list):
	'''
	param: organized_list: a list of organized lists 
	return: properDates_updated: convert the dates to the proper format for the google calender API
	'''
	today = date.today()
	year = today.strftime("%Y")

	months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month = ''  # For future use

	properDates = []

	for set_ in organized_list:
	# goes through each word and dates list in the orginized list
		word = set_.pop(0)
		properDate = [word]
		dates = set_
		for j in dates:
		#goes through each date in the dates list

			# form will keep track of what format the date is in
			if not j[0].isdigit():
				form = 1
			elif j[0].isdigit() and j[2].isdigit():
				form = 2
			elif j[0].isdigit() and not j[3].isdigit():
				form = 3
			else: 
				form = 4

			if form == 1:
				day = ''
				#this is for format 2
				if j[0:3] not in months:
					# for any words that got read in that are NOT dates
					month = 'error'

				for index in range(0,len(months)):
				#find the number value for the date Ex. Jan or January is 01  
					if j[0:3] == months[index]:
						month = str(index + 1)
						if len(month) < 2:
							month = '0'+ month
				for char in j: 
				#finds the day
					if char.isdigit():
						day += char
				if month != 'error':
					new_date_format=year + '-'+month+'-' + day
					properDate.append(new_date_format)

			elif form == 2: 
				if j[5].isdigit():
				# if the month is represented as numbers
					month = j[5]
					if j[6].isdigit(): 
						month = month +j[6]
					else: 
						month = '0'+ month
				if j[-2].isdigit():
					day = j[-1]+j[-2]
				else: 
					day = '0'+j[-1]
				new_date_format=year + '-'+month+'-' + day
				properDate.append(new_date_format)

			elif form == 3:
				for index in range(0,len(months)):
				#find the number value for the date Ex. Jan or January is 01  
					if j[5:7] == months[index]:
						month = str(index + 1)
						if len(month) < 2:
							month = '0'+ month
							month = '0'+ month
				if j[-2].isdigit():
					day = j[-1]+j[-2]
				else: 
					day = '0'+j[-1]
				new_date_format=year + '-'+month+'-' + day
				properDate.append(new_date_format)

			elif form == 4:
				if j[1].isdigit():
					day = j[0]+j[1]
						if j[4].isdigit():
							month = j[3]+j[4]
						else:
							month = '0'+j[3]
				else: 
					day = '0'+j[0]
					if j[3].isdigit():
							month = j[2]+j[3]
						else:
							month = '0'+j[2]



			new_date_format=year + '-'+month+'-' + day
			properDate.append(new_date_format)


		properDates.append(properDate)

		Dates_updated = []
		
		for lists in properDates:
		# make sure there are more then 1 items is each list otherwise ignore it
			if (len(lists) > 1):
				Dates_updated.append(lists)

		properDates_updated = check_duplicates(Dates_updated)


	return properDates_updated


if __name__ == '__main__':
	testing = read_file('test.txt')
	words, course = find_words(testing)
	print('Unorgonized list: ',words)

	print('course: ', course)
	oro = organize_dates(words)
	print('Organized! : ',oro)
	proper = proper_date(oro)
	print('Proper Date: ',proper)