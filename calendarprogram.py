userChoice = input ("Welcome! \n \nPlease chose an option by entering the number that corresponds to your choice: \n 1 View all calendar entries \n 2 Write new entries into the calendar \n 3 Edit existing entries \n 4 Exit the program \n \nChoice: ")

while userChoice != ("1" or "2" or "3" or "4"):
    userChoice = input ("\nChoice: ")
    break
    
if userChoice == ("1"):
    print ("")
    print ("You have chosen to view all calendar entries")

elif userChoice == ("2"):
    print ("")
    print ("You have chosen to write new entries into the calendar")

elif userChoice == ("3"):
    print ("")
    print ("You have chosen to edit existing calendar entries")
    
elif userChoice == ("4"):
    print ("This program will now close")
    print ("Thank you for using this program")
    exit()
    
else:
    userChoice = input ("\n Sorry, I did not get that")

         
