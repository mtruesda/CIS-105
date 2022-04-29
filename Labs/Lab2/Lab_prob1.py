#
# This program asks the user for the Maryland House District number and returns a name for the representative
# 2/21/2020
# @Myron Truesdale
# Problem 1
#

# Introductory Piece
print("This program will print a representatives name that corresponds to the District number")

# Assignment

# Variables

first = "Andy Harris"
second = "Dutch Ruppersberger"
third = "John Sarbanes"
fourth = "Anthony G. Brown"
fifth = "Steny Hoyer"
sixth = "David Trone"
seventh = "Currently Vacant - Elijah Cummings - Died in October 2019"
eighth = "Jamie Raskin"

selectedPosition = int(input("Select a district number and we will return a name: "))

if(selectedPosition == 1):
    print(first)
elif(selectedPosition == 2):
    print(second)
elif(selectedPosition == 3):
    print(third)
elif(selectedPosition == 4):
    print(fourth)
elif(selectedPosition == 5):
    print(fifth)
elif(selectedPosition == 6):
    print(sixth)
elif(selectedPosition == 7):
    print(seventh)
elif(selectedPosition == 8):
    print(eighth)
else:
    print("You've selected a number that is outside of the list of districts")
