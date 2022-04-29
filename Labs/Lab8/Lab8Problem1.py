#
# This project will create a student class that will gather info on them
# @MyronTruesdale
# 5/9/2020
# Lab 8 - Problem 1
#

# import the module (USE WITH MODULE NAMED Class)
import Class

# intro function
def intro():
    print("This project will create a student class that will gather info on them")

def main():
    intro()
    # creates object
    student1 = Class.Student()
    # sets the objects attributes
    student1.set_name(input("What is the students name? "))
    student1.set_major(input("What is their major? "))
    student1.set_credits_earned(input("How many credits do they have? "))
    # gets their attributes for display\
    print('Name: ' + student1.get_name() + '\tMajor: ' + student1.get_major() + '\t\tNumber of Credits: ' + student1.get_credits_earned())
    
main()
    
