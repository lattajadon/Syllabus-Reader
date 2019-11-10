Hack ED Beta 2019 Project: Syllabus-Reader

CREATORS: Dennea Maccallum, Jadon Latta, Steven Jiao

This program will use Python 3 to read a directory of syllabi PDFs and combine all the due dates onto Google Calander.

TO RUN:
	1. Create a clone of our repository by runnning the following code in 		the command line: 
	git clone https://github.com/lattajadon/Syllabus-Reader.git

	2. Download the Tika wrapper: https://pypi.org/project/tika-app/. 
	After the pip install, make sure the tika-app-python folder is in the 		same directory as the rest of the files.

	3. Download the Apache Tika 1.22 file from: https://tika.apache.org/download.html by selecting the tika-app-1.22.jar mirror for download. Make sure 	this .jar file is in your working directory.

	3. Making sure the credentials.json file is in the working directory, 		run the following code in the terminal:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

	4. Now, in the working directory, run the following on the terminal:
	python3 FolderSelectAndRead.py

	5. Choose which folder your PDF syllabi are in, and select it! Allow a 		couple seconds of processing to occur while the program parses your 		file. 

Python Scripts:
	* FolderChooser.py: By utilizing tkinter and filedialog, will pop up a 		UI for the user to choose which folder to read from, and the program 		will return the folder path chosen for later usage. 
	
	* sylRead.py: Through the modules os and Tikapp, will take the folder 		path chosen from FolderChooser.py, parse through the PDFs into .txt 		files.
	
	* ReadText.py: The actual parser of the .txt files! Will read through 		a .txt file, and using the regex module will search for class name, key 	words (midterm, exam, assignments, etc), their corresponding dates of 		the key words, and returning the organized date-format with the key 		words. 

	* GoogleAPI_Test.py: Creates and adds events to Google Calender with 		the correct dates, the course name with what the event is. It also adds 	a email reminder set to 2 days prior to the event date. 

	* FolderSelectAndRead.py: The main script running all the python files 		and functions to read through .txt files created from the PDF-formatted 	syllabi, parse it for its information, subsequently delete the .txt 		file after parsing, and add it to the google calender. 

Additional Files:
	* credentials.json: A credentials file in order to allow for the usage 		of Google Calender's API.












