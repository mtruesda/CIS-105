#
# This program will provide the amount of property tax to the user based on house value
# 2/11/2020
# @Myron Truesdale
# Problem 2
#

# Introductory piece
print('Problem 2 - Carroll County Property Taxes')
print('This program will provide the amount of property tax to the user based on house value')

# Assignment

# Sets fixed variables
Carroll_property_tax_rate = 1.018
Amount_per = 100

# Asks the user for their property value
Prop_value = input('What is your assessed property value (in dollars, do not use dollar sign)? ')

# Maths - sets the string for the value to an int, then it finds out how
# many sets of one hundred are in the value, and then multiplies it by the rate.
Property_tax_amount = int(Prop_value)
Property_tax_amount = Property_tax_amount/Amount_per
Property_tax_amount = Property_tax_amount*Carroll_property_tax_rate

#rounds it out two decimal places and adds a comma
Property_tax_amount = format(Property_tax_amount, ',.2f')

# returns the wanted amount
print('The tax amount is $' + str(Property_tax_amount))
