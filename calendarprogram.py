# ===============================================================================
# 'Calendar Program' is a utility program set inside a command line interface
# (without a GUI) that can read, write and edit any entries in a calendar,
# located inside a text file within the same directory.
# By Talvin Jacobs (2018)
# ===============================================================================

# Importing linecache. This allows one to get any line from a Python source file,
# while attempting to optimize internally, using a cache, the common case
# where many lines are read from a single file.
import linecache

#Getting the user's choice as a number
userChoice = input ("Welcome! \n \nPlease chose an option by entering the number that corresponds to your choice: \n 1 View all calendar entries \n 2 Write new entries into the calendar \n 3 Edit existing entries \n 4 Exit the program \n \nChoice: ")

# A while loop for when the user does not enter the correct input. It will keep
# looping until the user DOES enter the required input.
while userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4': # While the user does not enter 1, 2, 3 or 4:
    print ("\nSorry, I didn't quite get that ")
    userChoice = input ("Choice: ") # Grab another input and keep looping

# If the user enters 1    
if userChoice == ("1"):
    print ("")
    print ("You have chosen to view all calendar entries")
    print ("--------------------------------------------")
    print ("")

    f = open("calendar.txt", "r") # Open the calendar for reading
    calendarContents = f.read() # Assign a variable to reading the contents of the file
    
    print (calendarContents) # Display the contents
    print ("")
    f.close() # Closing the file to complete the operation
    
# If the user enters 2
elif userChoice == ("2"):
    print ("")
    print ("You have chosen to write new entries into the calendar")
    print ("------------------------------------------------------")
    print ("")

    f = open("calendar.txt", "a") # Open the calendar for appending
    
    # Receiving input for the new entry number
    newEntryID = input ("Please enter a new entry number ")
    f.write("\n")
    f.write(newEntryID) # Writing it to the file

    # Receiving input for the new year
    newYear = input ("Please enter the Year ")
    f.write("         ")
    f.write(newYear) # Writing it to the file
    
    # Receiving input for the new month
    newMonth = input ("Please enter the Month ")
    f.write("-")
    f.write(newMonth) # Writing it to the file

    # Receiving input for the new day
    newDay = input ("Please enter the Day ")
    f.write("-")
    f.write(newDay) # Writing it to the file

    # Receiving input for the new event
    print ("\n")
    newEvent = input ("What event would you like to add? ")
    print ("")
    f.write("     ")
    f.write(newEvent) # Writing it to the file
    
    print ("Done!")
    print ("")
    print ("Goodbye!")
    f.close() # Closing the file to complete the operation

    
# If the user enters 3   
elif userChoice == ("3"):
    print ("")
    print ("You have chosen to edit existing calendar entries")
    print ("-------------------------------------------------")
    print ("")

    # Grab the user input for the Event number they wish to edit
    eventEdit = input ("Please enter the Entry ID that corresponds to the event you with to edit ")
    eventeditString = str(eventEdit) # Convert it into a string and place it in a variable for printing
    eventeditInteger = int(eventEdit) # Convert it into an integer and place it in another variable for calculation

    # If the entered number DOES appear in the calendar's text file:
    if eventEdit in open ("calendar.txt").read():
        print ("")
        print ("This entry does exist") # Tell the user it exists
        print ("You have chosen to edit the entry number" , eventeditString) # Confirm the entry they wish to edit
        print ("")
        print ("This is the entry you wish to edit:")

        lineNumber = eventeditInteger + 2 # Get the location number of the line that contains the entry chosen

        f = open ("calendar.txt" , "r+") # Open the calendar's text file for reading and writing
        print (linecache.getline("calendar.txt" , lineNumber , module_globals=None)) # Display the line-to-edit itself
        print ("")

        neweditedYear = input ("Please enter a new year for this entry ") # Get a new input for the year
        neweditedMonth = input ("Please enter a new month for this entry ") # Get a new input for the Month
        neweditedDay = input ("Please enter a new day for this entry ") # Get a new input for the Day
        neweditedEvent = input ("Please enter a new event for this entry ") # Get a new input for an event

        # A for loop, whose purpose is to split the text file into a list and work out the length of each line by looping through the entire list
        for i in range(lineNumber):
            readLine = f.readline()
            lengthofLine = len (readLine)

        # Tell the program to go backwards and reach the point where the editing begins
        f.seek(f.tell() -lengthofLine)

        f.write("         ")
        f.write(neweditedYear) # The new year is written
        f.write("-")
        f.write(neweditedMonth) # The new month is written
        f.write("-")
        f.write(neweditedDay) # The new day is written
        f.write("     ")
        f.write(neweditedEvent) # The new event is written
        f.write("\n")

        print("")
        print("Done!")

        f.close() # Closing the file to complete the operation 

    # Otherwise (If the user has NOT entered the entry ID of an existing entry)    
    else:
        print ("This entry does NOT exist")
        print ("The program will now exit")
        exit() # The program will end

# If the user enters 4    
elif userChoice == ("4"):
    print ("This program will now close")
    print ("Thank you for using this program")
    exit() # The program will end
