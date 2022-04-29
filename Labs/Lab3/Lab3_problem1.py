#
# 2/25/2020
# @Myron Truesdale
# Problem 1
# This program will take the number of sides entered and the length for the sides entered and find perimeter
#

print("This program will take the number of sides entered and the length for the sides enteredand find perimeter")

n = int(input("How many sides do you want to have? "))

perimeter = 0
for i in range(n):
    perimeter += int(input("How long do you want the " + str(i+1) + " side? "))

print("The perimeter of your " + str(n) + "-sided polygon is " + str(perimeter))
