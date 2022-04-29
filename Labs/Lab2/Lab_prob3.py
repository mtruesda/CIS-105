#
# This program will ask a user for coordinate points and then display them on a graph, giving them information on quadrant and whether it is the origin or on an axis.
# 2/21/2020
# @Myron Truesdale
# Problem 3
#

# Introductory Piece
print("This program will ask a user for coordinate points and then display them on a graph, giving them information on quadrant and whether it is the origin or on an axis.")

# Assignment
xCoeff = int(input("What x-value would you like? "))
yCoeff = int(input("What y-value would you like? "))

print("Your coordinate point is (" + str(xCoeff) + ", " + str(yCoeff) + ").")

if(xCoeff == 0 and yCoeff == 0):
    print("Your point is about the origin")
elif(xCoeff == 0 and not(yCoeff == 0)):
    print("Your point is on the y-axis")
elif(not(xCoeff == 0) and yCoeff == 0):
    print("Your point is on the x-axis")
elif(xCoeff > 0 and yCoeff > 0):
    print("Your point is in quadrant 1")
elif(xCoeff < 0 and yCoeff > 0):
    print("Your point is in quadrant 2")
elif(xCoeff < 0 and yCoeff < 0):
    print("Your point is in quadrant 3")
elif(xCoeff > 0 and yCoeff < 0):
    print("Your point is in quadrant 4")
