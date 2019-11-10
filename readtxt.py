import re 
from datetime import date

def read_file(filename):
	'''
	param: filename: the name of the file we want to read from
	return: contents: the contents of the file
	'''

	file_o = open(filename,'r')
	contents = file_o.read()
	file_o.close()

	return contents

def find_words(contents):
	'''
	param: contents: the contents of the file  
	return: dates: a list of specific words and dates
	'''

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

	dates = re.findall(r"Midterm|Final|Exam|Assignment|Quiz|Labs?|[A-Z].{2,5}.[0-9]\b", contents)

	return dates

def organize_dates(dates):
	'''
	'''
	word_list = ['Midterm','Final','Exam','Assignment','Quiz','Lab','Labs']

	organized= []

	for i in range(0,len(dates)):
		date = []
		if dates[i] in word_list:
			date.append(dates[i])
			for j in range(i+1,len(dates)):
				if dates[j] in word_list:
					break
				else:
					date.append(dates[j])

			organized.append(date)

	organized_list = []

	for lists in range(0,len(organized)):
		if len(organized[lists]) > 1:
			organized_list.append(organized[lists])

	complete_list = []

	for lists in organized_list:
		if (lists[0] == 'Lab') or (lists[0] == 'Labs'):
			complete_list = complete_list
		else:
			complete_list.append(lists)

	return complete_list

def proper_date(organized_list):
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
			if j[0].isdigit():
				form = 1
			else: 
				form = 2

			if form == 2:
				day = ''
				#this is for form 2
				if j[0:3] not in months:
					month = 'error'

				for index in range(0,len(months)):
				#find the number value for the date Ex. Jan or January is 01  
					if j[0:3] == months[index]:
						month = str(index + 1)
						if len(month) < 2:
							month = '0'+ month
				for char in j: 
					if char.isdigit():
						day += char
				if month != 'error':
					new_date_format=year + '-'+month+'-' + day
					properDate.append(new_date_format)

		properDates.append(properDate)

		properDates_updated = []
		
		for lists in properDates:
			if (len(lists) > 1):
				properDates_updated.append(lists)


	return properDates_updated


if __name__ == '__main__':
	testing = read_file('test.txt')
	words = find_words(testing)
	print('Unorgonized list: ',words)
	oro = organize_dates(words)
	print('Organized! : ',oro)
	proper = proper_date(oro)
	print('Proper Date: ',proper)