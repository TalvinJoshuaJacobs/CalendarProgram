userChoice = input ("Welcome! \n \nPlease chose an option by entering the number that corresponds to your choice: \n 1 View all calendar entries \n 2 Write new entries into the calendar \n 3 Edit existing entries \n 4 Exit the program \n \nChoice: ")

while userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4':
    print ("\nSorry, I didn't quite get that ")
    userChoice = input ("Choice: ")
    
if userChoice == ("1"):
    print ("")
    print ("You have chosen to view all calendar entries")
    print ("--------------------------------------------")
    print ("")

    f = open("calendar.txt", "r")
    calendarContents = f.read()
    
    print (calendarContents)
    print ("")
    f.close()

elif userChoice == ("2"):
    print ("")
    print ("You have chosen to write new entries into the calendar")
    print ("------------------------------------------------------")
    print ("")

    f = open("calendar.txt", "a")

    newEntryID = input ("Please enter a new entry ID ")
    f.write("\n")
    f.write(newEntryID)
    
    newYear = input ("Please enter the Year ")
    f.write("         ")
    f.write(newYear)
    
    newMonth = input ("Please enter the Month ")
    f.write("-")
    f.write(newMonth)

    newDay = input ("Please enter the Day ")
    f.write("-")
    f.write(newDay)

    print ("\n")
    newEvent = input ("What event would you like to add? ")
    print ("")
    f.write("     ")
    f.write(newEvent)
    print ("Done!")
    
    f.close()
    
elif userChoice == ("3"):
    print ("")
    print ("You have chosen to edit existing calendar entries")
    print ("-------------------------------------------------")
    print ("")

    f = open("calendar.txt", "a")
    eventEdit = input ("Please enter the position of the calendar you want to edit ")
    f.seek(eventEdit)
    madeChanges = input ("Please enter an updated version of the event")
    f.write(madeChanges)
    print ("Done!")
    f.close()
    
elif userChoice == ("4"):
    print ("This program will now close")
    print ("Thank you for using this program")
    exit()
