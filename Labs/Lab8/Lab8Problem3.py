#
# Will create a subclass of directory in provided module.
# @MyronTruesdale
# 5/9/2020
# Lab 8 - Problem 
# 

### TO BE USED WITH chp11_lab_defEdit ###

# import
import chp11_lab_defEdit

def intro():
    print('Will create a subclass of directory in provided module.')

def main():
    student1 = chp11_lab_defEdit.Student(input("What is the student's name? "),
                                         input("What is their address? "),
                                         input("How old are they? "),
                                         input("What is their phone number? "),
                                         input("What is their major? "),
                                         input("How many credits do they have? "))
    print(student1)

main()

