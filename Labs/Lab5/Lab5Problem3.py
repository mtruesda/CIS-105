#
# This program reads the 'directory' made in the previous problem
# @MyronTruesdale
# 4/5/2020
# Lab 5 - Problem 3
#

# intro function
def intro():
    print("This program reads the 'directory' made in the previous problem")

# calls intro
intro()

def main():
    # initialize variables
    contributionTotal = 0
    contributions = 0
    contributionAverage = 0
    
    # reopens the directory for reading
    directory = open('directory.txt', 'r')
    line = directory.readline()
    
    # checks for and prints every line in the directory
    while (line != ''):
        print(line.rstrip('\n'))
        # determines if the line is a contribution line
        if(line.find('Contribution:')!=-1):
            # strips it of any additional pieces before it is turned to an int
            line = line.rstrip('\n')
            line = line.lstrip('Contribution: ')
            # increments the number of contributions
            contributions += 1
            # tries to add the number to the total
            try:
                contributionTotal += int(line)
            except ValueError as err:
                print(err)

        # finds the next line
        line = directory.readline()

    # trying to find the average
    try:
        contributionAverage = contributionTotal/contributions
        contributionAverage = format(contributionAverage, '.2f')
    except ValueError as err:
        contributionAverage = err

    print('Summary Statistics\n-------------------')

    # format the total in case
    contributionTotal = format(contributionTotal, '.2f')
    
    # contribution summary
    print('Total Contributions: $ ' + str(contributionTotal))
    print('Number of Contributors: ' + str(contributions))
    print('Average Contribution Amount: ' + str(contributionAverage))

    # if zero contribution
    if (contributionTotal == 0 and contributions > 0):
        print('\nTry selecting integers for your contribution amounts')

    # closes the directory to protect data
    directory.close()

try:
    main()
except ValueError as err:
    print(err)
