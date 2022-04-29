import math
import random

cows = 0

class cow():
    def __init__(self):
        global cows
        cows += 1
        self.number = cows
        self.name = input("What is new cow name? ")
        self.size = random.randint(1,20)

firstCow = cow()
secondCow = cow()

print(firstCow.number)
print(secondCow.number)
