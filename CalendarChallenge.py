"""
Jasmyne Roberts @ GenCyber

6 July 2016

Calendar Challenge: Makes a calendar of a year, labeling months and days
and using lists and functions. Will also ask what weekday the year starts
on and if it is a leap year

Example month:
~~~~~~~~~~January~~~~~~~~~~
Sun Mon Tue Wed Thu Fri Sat 
  1   2   3   4   5   6   7 
  8   9  10  11  12  13  14 
 15  16  17  18  19  20  21 
 22  23  24  25  26  27  28 
 29  30  31 

"""

def calendar(jan1, isLeapYear):

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    weekdays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    
    for m in range(len(months)):
        
        # How many days are in a certain month
        if m == 3 or m == 5 or m == 8 or m == 10:
            days = 30
        elif m == 1:
            if isLeapYear == 1:
                days = 29
            else:
                days = 28
        else:
            days = 31
            
        squigglespace = int(27 - len(months[m])) # determines space for squiggles
        squiggle = int(squigglespace / 2) * "~" # half a string of squiggles
        otherdays = days % 7 # number of days in a non-seven-day week
        dayn = 1 # counts days

        # Prints centered month framed by squiggles at top of each month
        if len(squiggle * 2 + months[m]) < 27:
            print(squiggle + months[m] + squiggle + "~")
        else:
            print(squiggle + months[m] + squiggle)
            
        # Prints weekdays below month
        for x in range(len(weekdays)):
            print(weekdays[x], end=" ")
            
        print()
        
        # Prints day numbers for weeks
        for y in range(int((days - otherdays) / 7)):
            for z in range(7):
                if len(str(dayn)) == 1:
                    print("  " + str(dayn), end=" ")
                else:
                    print(" " + str(dayn), end=" ")
                dayn += 1
            print()
        for a in range(otherdays):
            print(" " + str(dayn), end=" ")
            dayn += 1
            
        print()
        
def begin():
    print()
    print("~"*16 + "Welcome to the Calendar Generator" + "~"*16)
    wd = int(input("What weekday (in numbers) does January 1st fall on? "))
    if wd > 6 or wd < 0:
        wd = int(input("Type a number from 0 to 6. Ex: 0 for Sunday, and 6 for Saturday: "))
    while wd > 6 or wd < 0:
        wd = int(input("This is not a number from 0 to 6. Please try again: "))
        
    ly = int(input("Is it a leap year? Type 1 for yes and 0 for no: "))
    while ly > 1 or ly < 0:
        ly = int(input("Invalid number. Please try again: "))
    print()
    calendar(wd, ly)
    
begin()
