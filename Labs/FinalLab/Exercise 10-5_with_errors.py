# Programming Exercise 10-5
# This file and the other file called retail.py are the solutions
# to problem 10-5 in the textbook. However, these files contain errors.
# 1. Read the problem in the textbook. 
# 2. Fix the mistakes in the code. There are 5 mistakes to find. 4 points each. 
# 3. Put a comment next to the corrected code using the # symbol to say what was
# wrong.
# 4. Save both corrected files with your full name as comments
# at the beginning of each file and submit to Blackboard.

# MYRON TRUESDALE FINAL - will use ### to mark mistakes

### imported incorrectly. Don't add the .py
import retail

def main():
    # Intro message
    intro()
    
    # Create three instances of RetailItem.
    item1 = retail.RetailItem('Jacket', 12, 59.95)
    item2 = retail.RetailItem('Designer Jeans', 40, 34.95)

    ### parts called out of order
    item3 = retail.RetailItem('Shirt', 20, 24.95)

    ### not sure if this counts as a mistake but you can use \n for line changes
    # Display information.
    print ('Retail Item 1: ')
    print (item1 + '\n')

    print ('Retail Item 2:')
    print (item2 + '\n')
    
    print ('Retail Item 3:')
    print (item3 + '\n')

def intro():
    print('This program will demonstrate the use of classes to create a Retail Item')
    ### there was no starting quotation in this print statement
    print('object to save information.')
    
# Call the main function.
main()

