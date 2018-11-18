# 'Calendar Program'

### I. Initiative

'Calendar Program' is a utility program set inside a command line interface (without a GUI) that can read, write and edit any entries in a calendar, located inside a text file within the same directory.

### II. Epics and User Stories

##### Epics

 - The program must provide the user with the option to view all existing calendar entries, add new calendar entries, and edit any entry that exists within the text file.
 - The program should be able to interact with a text file located in the same directory.
 - The user must be able to view all calendar entries 
 - The user must be able to add any calendar entry to the list
 - The program must provide the user with the choice to edit any existing calendar entry of their choice
 - The user must be able to edit any existing entry

##### Non-Functional Requirements

 - If the user provides the program with an invalid input, they are requested to try again
 - If the computer re-asks the user a question, it is presented on a separate line away from the previous question, to reduce screen clutter
 - ASCII text is used in the text file and presented in the calendar program to look more appealing and easier to read

##### User Stories

 - "As a user, I would want to chose an option between reading, writing and editing existing entries"
 - "As a user, I would want the program to interact with a text file called 'calendar' located in the same directory"
 - "As a user, I would want to be able to read all of the calendar entries"
 - "As a user, I would want to have the calendar entries presented to me in a readable and clear format"
 - "As a user, I would want to add any entry to the calendar"
 - "As a user, I would want to edit any existing entry I chose"
 - "As a user, I would like to be asked again if I type in a wrong choice or edit an entry that does not exist"
 - "As a user, I would like the program to limit the output to only the current month/year etc."
 - "As a user, I would like the program to use a form of time function to print events at the correct time"

##### How We Addressed The Requirements

A plan was devised so that all the functional requirements would be completed with the highest priority, followed by the non-functional requirements.

### III. Genre

A GUI-less, command line utility program

### IV. Technical Details

##### Platform

The program was coded in the Python IDLE Shell. It was useful for fixing problems in the code, by providing   easy-to-read feedback on which line(s) were problematic.

##### Programming Language/Environment

Python IDLE 3.7

##### Programming Challenges

There were several programing challenges that were faced during the implementation of the code. The main challenge was getting started, due to the fact that there were so few restrictions placed on the task. Another challenge was getting the program to interact with the text file the way it needed to, without any errors or formatting issues involved. Another challenge was letting the program edit the text file the way it needed to.
 
##### Constructing And Implementing My Code

To overcome the main challenge, giving the user the option to chose between writing, reading and editing the text file was the starting point (using if statements). Then, the different functional requirements were built onto that part, followed by the non-functional requirements. After the user was given a choice, a while loop was placed on top of that to re-ask the question if the user enters an incorrect input. Then, each 'choice' was built on, starting with the reading of the file, then the appending to the file, followed by the editing of the file.

##### Algorithms

The first algorithm present in the program is responsible for the user's choice between viewing, adding and editing existing calendar entries. It uses a while loop and an if statement to lead the user to what they wish to do.
Another algorithm in the program is responsible for file management. Each user choice leads to a file being opened for reading/writing/appending using the `f.read()` , `f.write()` and `f.seek()` functions.
 
##### Coding Standards 
The following coding standards were adhered to when completing the code:

-   Using camelCase for variable and function names
-   The variable names and cases are consistent
-   The code is readable
-   The spacing, indentation, comments and brackets are consistent

### V. Research

The only research conducted was for finding out how to efficiently seek any line in a text file. This was done by using the `linecache` module built into Python. 

This module was discovered in the official Python documentation found online: https://docs.python.org/3.7/library/linecache.html

### VI. Project Management

##### Burndown Chart

![](https://i.imgur.com/sasXhWB.jpg)

Chart showing the completion of user stories over time

##### User Stories Tracking Chart (Which Stories Have Been Completed)

![](https://i.imgur.com/9vpVP0p.jpg)

##### Flowchart

![enter image description here](https://i.imgur.com/l7wfmDO.jpg)

##### Functions

 - "Open calendar.txt for reading": Using an in-built command to tell Python to open the calendar text file for reading which is located in the same directory. `f = open("calendar.txt", "r")` 
 - "Open calendar.txt for reading and writing": Does the same as explained above, but also allows python to overwrite any existing information located in the file itself. `f = open("calendar.txt", "r+")`
 - "Open calendar.txt for appending": Uses the 'a' to tell Python to only add to the text file. (Nothing gets overwritten). `f = open("calendar.txt", "a")`
 - "Read the contents of calendar.txt": Tells Python to read everything contained in the text file. `calendarContents = f.read()`
 - "close calendar.txt": Closes the calendar after it has been opened. This must be done to prevent the files from staying open after the program is closed, which can lead to memory leaks etc. `f.close()
 - "Write down the entry number, year, month, day and entry into the text file in fitting format": Once the user inputs have been received, they will written down into the text file using `f.write()`
 - "Write over the old line with the new line containing the new information in the fitting format": Also uses the same function `f.write()` , but first, the program needs to go to the line that needs to be edited by using a for loop to convert the text file into a list (shown below): 
`for i in range(lineNumber):    readLine = f.readline()    lengthofLine = len (readLine)`

### VII. Evaluation

I have managed to complete all of the functional requirements and get this program to work properly without any issues or errors. Almost all of it was completed without any outside assistance whatsoever. This is the reason why the code is made up from many basic ideas. There is definitely another way to implement all of the functional requirements more efficiently, however that would require a lot more time for me to pull off.
After beginning with giving the user 4 options, I began to work a lot faster and more efficiently, because that is what became the basic structure of the code. 

Some non-functional requirements were also implemented. The user is prompted to enter their input again if their first input didn't properly chose an option -  this seemed necessary to input, as it is often the case where the user can miss-type their option or misunderstand the question that they are being prompted with. Another non-functional requirement featured in the program is the presentation of the prompts in the command-line. ASCII text was used in occasions to de-clutter the screen and make the program more user friendly.

Python was used because it has not been used in any other project before, and also it appeared to be the most fitting language to use, as the syntax was very basic, and also fixing errors was easy due to the feedback that the Python shell provided me with.

