print ("Welcome!")
print ("")
print ("Please chose an option by entering the number that corresponds to your choice:")
print ("1 View all calendar entries")
print ("2 Write new entries into the calendar")
print ("3 Edit existing entries")
print ("4 Exit the program")
print ("")
userChoice = input ("Choice: ")

while userChoice == "1" or "2" or "3" or "4" :
    
    if userChoice == ("1"):
        print ("")
        print ("You have chosen to view all calendar entries")
        break
    
    elif userChoice == ("2"):
        print ("")
        print ("You have chosen to write new entries into the calendar")
        break

    elif userChoice == ("3"):
        print ("")
        print ("You have chosen to edit existing calendar entries")
        break

    elif userChoice == ("4"):
        print ("This program will now close")
        print ("Thank you for using this program")
        exit()
        break

    else:
        print ("Sorry, I didn't understand that. Please enter in your input again")
        print ("")
        break


    
