#
# This program will take in daily spending for each day of the week and use the list
# to create a bunch of math.
# @MyronTruesdale
# 4/18/20
# Lab 6 - Problem 1
#

def intro():
    print("This program will take in daily spending for each day of the week and use the list to create a bunch of math.")

def dailySpend():
    # variables
    daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    dailySpending = []
    lowest = 100000
    highest = 0
    total = 0
    average = 0

    # for finding the full list of days $
    for a in daysOfWeek:
        spend = int(input("How much did you spend on " + a + "? "))
        dailySpending.append(spend)

    # minimum and maximum
    lowest = min(dailySpending)
    highest = max(dailySpending)

    # calculating the total
    for a in dailySpending:
        total += a

    # calculating the average
    average = total/(len(dailySpending))

    # formats the values
    total = format(total, ".2f")
    average = format(average, ".2f")
    lowest = format(lowest, ".2f")
    highest = format(highest, ".2f")
    
    # prints the values to the output
    print("The minimum is $" + str(lowest))
    print("The maximum is $" + str(highest))
    print("The total for the week is $" + str(total))
    print("The average of the weekly spend is $" + str(average))
    
intro()
dailySpend()

