#
# This Program will convert given miles per hour to feet per second
# 2/11/2020
# @Myron Truesdale
# Problem 3
#

# Introductory Piece
print('Problem 3 - Miles per Hour to Feet per Second Converter')
print('This program will convert given miles per hour to feet per second')

# Fixed Variables
Conversion_amount = 1.46667

# Assignment
Given_speed = int(input('Please provide a speed in mph '))

# Math used
# This step converts the speed
Converted_speed = Given_speed*Conversion_amount
# This step rounds to the tenths place and adds a comma
Converted_speed = format(Converted_speed, ',.1f')

# Returns output
print('The conversion from ' + str(Given_speed) + ' mph to fps is ' + str(Converted_speed) + ' feet per second')
