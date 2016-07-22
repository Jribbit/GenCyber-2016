"""
Jasmyne Roberts @ GenCyber

Started: 6 July 2016
Completed: 7 July 2016

Calendar Challenge.py: Makes a calendar of a year, labeling months and days
and using lists and functions. Will also ask what weekday the year starts
on and if it is a leap year

Example month:
~~~~~~~~~February~~~~~~~~~~
Sun Mon Tue Wed Thu Fri Sat 
              1   2   3   4 
  5   6   7   8   9  10  11 
 12  13  14  15  16  17  18 
 19  20  21  22  23  24  25 
 26  27  28  29 

"""

# Function creates and prints calendar of the year
def calendar(skip, isLeapYear):

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    weekdays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    
    # Prints months
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
            
        squigglespace = int(27 - len(months[m])) # Determines space for squiggles
        squiggle = int(squigglespace / 2) * "~" # Half a string of squiggles

        dayn = 1 # Day number
        
        firstline = 7 - skip # number of days in the first week of month
        days = days - firstline # number of days minus the first week
        otherdays = days % 7 # last week of month if week is not 7 days

        # Prints centered month framed by squiggles at top of each month
        if len(squiggle * 2 + months[m]) < 27:
            print(squiggle + months[m] + squiggle + "~")
        else:
            print(squiggle + months[m] + squiggle)
            
        # Prints weekdays below month
        for x in range(len(weekdays)):
            print(weekdays[x], end=" ")

        print()

        # Prints spaces for numberless weekdays
        print("    " * skip, end="")
        
        # Prints the first week of month
        for z in range(firstline):
            print("  " + str(dayn), end=" ")
            dayn += 1
        
        print()
        
        # Prints full weeks in month
        for y in range(int((days - otherdays) / 7)):
            for z in range(7):
                if len(str(dayn)) == 1:
                    print("  " + str(dayn), end=" ")
                else:
                    print(" " + str(dayn), end=" ")
                dayn += 1
            print()
            
        # Prints last week of month if week is not 7 days
        for a in range(otherdays):
            print(" " + str(dayn), end=" ")
            dayn += 1
            
        print()
        
        # Reassigns variable "skip" for next month        
        skip = otherdays
        
# Asks user for calendar preferences and checks user input
def begin():
    print()
    print("~"*16 + "Welcome to the Calendar Generator!" + "~"*16)
    print()
    print("On what weekday does January 1st fall?")
    wd = int(input("Type a number from 0 to 6. Ex: 0 for Sunday, and 6 for Saturday: "))
    while wd > 6 or wd < 0:
        wd = int(input("This is not a number from 0 to 6. Please try again: "))
        
    ly = int(input("Is it a leap year? Type 1 for yes and 0 for no: "))
    while ly > 1 or ly < 0:
        ly = int(input("Invalid number. Please try again: "))
    print()
    calendar(wd, ly)

# Runs program    
begin()