#
# This program will get a string from the user and generate a password that selects the first letter of each
# word in the string and concatenating them.
# @MyronTruesdale
# 4/19/2020
# Lab 6 - Problem 3
#

def intro():
    print("This program will get a string from the user and generate a password that selects the first letter of each word in the string and concatenating them.")

def passwordMaker():
    # retrieves string from the user
    print("Think of a string to generate your password, longer strings with more words work better.")
    string = input("What is your string? ")

    # split the string
    wordList = string.split()
    print(wordList)

    # create empty password
    password = ""

    # loop through each word and gather the first letters
    for a in wordList:
        password += a[0]

    # returns the password to the user.
    print('Your new password is ' + password + '.')
    
intro()
passwordMaker()
