#
# 2/25/2020
# @Myron Truesdale
# Problem 3
# This will ask for the number of weeks and take number of hours per day programming and then create a weekly average along with total hours
#

print('This will ask for the number of weeks and take number of hours per day programming and then create a weekly average along with total hours')

weekHours = []
hours = 0
weeks = int(input('How many weeks is your course? '))

for i in range(weeks):
    hours = 0
    print('Week ' + str(i+1))
    for i in range(7):
        print('Day ' + str(i+1))
        hours += int(input('How many hours did you put in today? '))
        print(hours)
    weekHours.append(hours)

hours = 0
for i in weekHours:
    hours += i

print('Total hours was ' + str(hours) + ' hours')

hours = hours/weeks
hours = format(hours, ".1f")

print('Average was ' + str(hours) + ' hours per week')
