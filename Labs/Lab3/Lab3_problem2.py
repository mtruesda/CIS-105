#
# 2/25/2020
# @Myron Truesdale
# Problem 3
# This program will take the average bowling score of your three bowling scores while keeping them between set parameters
#

print("This program will take the average bowling score of your three bowling scores while keeping them between set parameters")

total = 0

for i in range(3):
    score = int(input("Enter your " + str(i+1) + " score. "))
    while(score < 0 or score > 300):
        print('You entered an invalid score')
        score = int(input('Enter a valid score '))
    total += score

print('Your average score is ' + str(total/3))
