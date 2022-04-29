#
# This project will create books that can be utilized in a class system
# @MyronTruesdale
# 5/9/2020
# Lab 8 - Problem 2 
# 

### TO BE USED WITH Lab8Problem2.py ###

# book class
class Book:
    # initial function
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__price = 0
        self.__rating = 0
    # set functions
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author = author
    def set_price(self,price):
        self.__price = price
    def set_rating(self,rating):
        if(rating>5 or rating<0):
            self.__rating = 0
        else:
            self.__rating = rating
    
    # get functions
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price
    def get_rating(self):
        return self.__rating

    # __str__
    def __str__(self):
        return ('Title: ' + self.__title + '\tAuthor: ' + self.__author +
                '\tPrice: $' + str(self.__price) + '\tRating: ' + str(self.__rating))
