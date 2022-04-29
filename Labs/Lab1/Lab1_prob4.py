#
# This program's purpose is to convert currency from U.S. dollars to Euros
# 2/11/2020
# @Myron Truesdale
# Problem 4
#

# Introductory Piece
print('Problem 4 - Currency Converter for Euro')
print('The purpose of this program is to convert currency from U.S. dollars to Euros.')

# Fixed Variables
rate = .91 #as of 9/3/2019
rate = float(rate)

# User prompt
dollars = int(input('How many U.S. dollars would you like to convert to Euros? '))
dollars = round(dollars, 2)

# Math
converted = dollars*rate

# Formatting - this felt unnecessary, but whenever I tried to format earlier it kept on returning an error that didn't make sense
dollars = format(dollars, ',.2f')
converted = format(converted, ',.2f')

# Returns the output
print('$' + str(dollars) + ' is equivalent to \u20ac35' + str(converted))
