import linecache
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

    newEntryID = input ("Please enter a new entry number ")
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
    print ("")
    print ("Goodbye!")
    f.close()
    
elif userChoice == ("3"):
    print ("")
    print ("You have chosen to edit existing calendar entries")
    print ("-------------------------------------------------")
    print ("")

    eventEdit = input ("Please enter the Entry ID that corresponds to the event you with to edit ")
    eventeditString = str(eventEdit)
    eventeditInteger = int(eventEdit)

    if eventEdit in open ("calendar.txt").read():
        print ("")
        print ("This entry does exist")
        print ("You have chosen to edit the entry number" , eventeditString)
        print ("")
        print ("This is the entry you wish to edit:")

        lineNumber = eventeditInteger + 2

        f = open ("calendar.txt" , "r+")
        print (linecache.getline("calendar.txt" , lineNumber , module_globals=None))
        print ("")

        neweditedYear = input ("Please enter a new year for this entry ")
        neweditedMonth = input ("Please enter a new month for this entry ")
        neweditedDay = input ("Please enter a new day for this entry ")
        neweditedEvent = input ("Please enter a new event for this entry ")

        for i in range(lineNumber):
            readLine = f.readline()
            lengthofLine = len (readLine)
        # print(f.readline())

        f.seek(f.tell() -lengthofLine)

        f.write("         ")
        f.write(neweditedYear)
        f.write("-")
        f.write(neweditedMonth)
        f.write("-")
        f.write(neweditedDay)
        f.write("     ")
        f.write(neweditedEvent)
        f.write("\n")

        print("")
        print("Done!")

        f.close()
        
    else:
        print ("This entry does NOT exist")
        print ("The program will now exit")
        exit()
    
elif userChoice == ("4"):
    print ("This program will now close")
    print ("Thank you for using this program")
    exit()
