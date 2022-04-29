#
# The program will ask the user for the amount of protein leakage over 24 hours and then come back with a response.
# 2/21/2020
# @Myron Truesdale
# Problem 2
#

# Introductory Piece
print("This program will ask for leakage over 24 hours and diagnose a need for a doctor")

# Assignments

# Variables
protein = int(input("How much protein leakage has occurred over the last 24 hours? "))

if(protein < 30 and protein >= 0):
    print("Your protein leakage is normal and needs no additional follow-up.")
elif(protein >= 30 and protein <= 300):
    print("You may have early kidney disease and will need a follow-up with your physician.")
elif(protein > 300):
    print("You may have more advanced kidney disease and will definitely need a follow-up with your physician.")
elif(protein < 0):
    print("You entered an amount that either doesn't make sense or isn't possible.")
