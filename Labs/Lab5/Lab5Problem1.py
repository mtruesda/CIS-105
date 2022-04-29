# 
# This program uses recursion to print numbers
# from the Lucas series.
# @Myron Truesdale
# 4/5/2020
# Lab 5 - Problem 1
#

def intro():
    print("This program uses recursion to print numbers from the Lucas series.")

# main function calls lucas function, loop, and inquires input
def main():
    amount = int(input('How many sequences would you like? '))

    for number in range(amount):
        print(lucas(number))
    
# The lucas function returns the nth number
# in the Lucas series.
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# Call the main function.
intro()
main()

