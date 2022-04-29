#
# This program creates a directory of contributors and other items and
# adds them to a file
# @Myron Truesdale
# 4/5/2020
# Lab 5 - Problem 2
#

def main():
    # opens the directory for work
    directory = open('directory.txt', 'w')
    
    # adds all the contributors and their information to the directory
    for i in range(contributors):
        name = input('What is the ' + str(i+1) + " contributor's name? ")
        cookie = input('What is their favorite cookie? ')
        age = input('How old are they? ')
        contribution = input('How much did they contribute? ')

        directory.write('Name: ' + name + '\n')
        directory.write('Favorite Cookie: ' + cookie + '\n')
        directory.write('Age: ' + age + '\n')
        directory.write('Contribution: ' + contribution + '\n')
        directory.write('\n')

    # closes the directory
    directory.close()

# determines the number of contributors - returns the error if it's wrong
try:
    contributors = int(input('How many contributors are there? '))
    main()
except ValueError as err:
    print(err)
