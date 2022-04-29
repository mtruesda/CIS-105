#
# This project will create a student class that will gather info on them
# @MyronTruesdale
# 5/9/2020
# Lab 8 - Problem 1
# 

### TO BE USED WITH Lab8Problem1 Module ###

# the actual student class
class Student:
    # initializes attributes
    def __init__(self):
        self.__name = ""
        self.__major = ""
        self.__credits_earned = 0
    # set functions
    def set_name(self, name):
        self.__name = name
    def set_major(self, major):
        self.__major = major
    def set_credits_earned(self, number):
        self.__credits_earned = number
    # get functions
    def get_name(self):
        return self.__name
    def get_major(self):
        return self.__major
    def get_credits_earned(self):
        return self.__credits_earned


