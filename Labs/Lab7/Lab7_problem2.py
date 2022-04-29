#
# This program will enter values from two documents into two sets, creates a third set that contains orioles
# from both sets, and finally a fourth set that contains all orioles mentioned.
# @MyronTruesdale
# Version 5/3/2020
# Lab 7 - Problem 2
#

# intro function
def intro():
    print('This program will enter values from two documents into two sets, creates a third set that contains orioles from both sets, and finally a fourth set that contains all orioles mentioned.')

# main function
def main():
    # creates all the sets
    orioles2018Set = set()
    orioles2019Set = set()
    oriolesSharedSet = set()
    oriolesTotalSet = set()

    # completing the first set
    orioles2018 = open('Orioles_2018.txt', 'r')

    for line in orioles2018:
        rstripped = line.rstrip('\n')
        orioles2018Set.add(rstripped)

    orioles2018.close()
    print(str(len(orioles2018Set)) + " players in 2018")

    # completes the second
    orioles2019 = open('Orioles_2019.txt', 'r')

    for line in orioles2019:
        rstripped = line.rstrip('\n')
        orioles2019Set.add(rstripped)

    orioles2019.close()
    print(str(len(orioles2019Set)) + ' players in 2019')

    # third set completion
    oriolesSharedSet = orioles2018Set.intersection(orioles2019Set)
    print(str(len(oriolesSharedSet)) + ' players on both rosters')
    
    # fourth set completion
    oriolesTotalSet = orioles2018Set.union(orioles2019Set)
    print(str(len(oriolesTotalSet)) + ' players total')
    
intro()
main()
