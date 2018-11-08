print ("Welcome!")
userChoice1 = input("Would you like to view the entire entry list? ")
if userChoice1 == ("Yes"):
    f = open('calendar.txt', 'r')
    print(f.name)
    f.close()
else:
    exit()
