#
# This project will create books that can be utilized in a class system
# @MyronTruesdale
# 5/9/2020
# Lab 8 - Problem 2 
# 

### TO BE USED WITH ClassTwo.py ###
import ClassTwo

# intro
def intro():
    print('This project will create books that can be utilized in a class system\n')

def main():
    # intro
    intro()
    # Book object creations
    book1 = ClassTwo.Book()
    book2 = ClassTwo.Book()
    book3 = ClassTwo.Book()
    book4 = ClassTwo.Book()

    shelf = []

    # setting up book 1
    book1.set_title('Starting Out with Python, Student Value Edition (4th Edition)')
    book1.set_author('Tony Gaddis')
    book1.set_price(69.32)
    book1.set_rating(4.6)
    shelf.append(book1)
    
    # setting up book 2
    book2.set_title("Murach's Java Programming (5th Edition)")
    book2.set_author('Joel Murach')
    book2.set_price(46.49)
    book2.set_rating(4.6)
    shelf.append(book2)

    # setting up book 3
    book3.set_title("Ruby Programming (Introduction to Programming)")
    book3.set_author('Jerry Lee Ford')
    book3.set_price(154.95)
    book3.set_rating(2)
    shelf.append(book3)

    # setting up book 4
    book4.set_title('iOS 13 Programming for Beginners: Get started with building iOS apps with Swift 5 and Xcode 11, 4th Edition')
    book4.set_author('Ahmad Sahar')
    book4.set_price(39.99)
    book4.set_rating(4.3)
    shelf.append(book4)
    
    # printing the books
    for book in shelf:
        print(book)
        print('\n')

main()
