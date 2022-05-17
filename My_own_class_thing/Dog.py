# Class dog definition

# Still not entirely sure what this is
# just something weird that I'm working on

class Dog:

    # initialization function
    def __init__(self, name):
        self.name = name
        self.size = 10*int(input("How big is your dog (out of ten)? "))
        self.mood = 0

    # feeds the dog
    def feedDog(self, food, amount):
        print("Feeding " + self.name + " " + str(amount) + " of " + food)
        self.mood += 1

    # grows the dog
    def growDog(self, amount):
        if(self.size < 100):
            self.size += amount

    # rename the dog
    def rename(self, name):
        self.name = name

    # for walking the dog
    def walkDog(self, distance):
        if(distance < self.size/10):
            self.mood += 1
        elif(distance*10 > self.size*2):
            self.mood -= 1
        else:
            self.mood += distance

    # function to be used to update the image
    def updateImage():
        return 0

    # function to be used to return the size
    def getSize(self):
        return self.size

    # setter for size
    def setSize(self, size):
        self.size = size

    # function to be used to return the name
    def getName(self):
        return self.name

    # getter for mood
    def getMood(self):
        return self.mood

# helps with parsing the strings later
commandDict = {
    "walk": 5,
    "Walk": 5,
    "feed": 5,
    "Feed": 5
    }

# Global Methods

# used to determine arguments for commands
def parseString(cmd):
    if (upToSpace(cmd) != -1):
        n = upToSpace(cmd) + 1

    substring = int(cmd[n:])
    return substring

# finds the first instance of a space
def upToSpace(string):
    n = 0
    while(True):
        if(string[n] != " "):
            n += 1
        else:
            return n
        if (n == len(string)):
            break

    return -1

# gets stuff ready
x = True
dog = Dog(input("What is your Dogs name? "))

# used to run the "shell"-like activity
while(x):
    # Status stuff
    print("Status:\nMood: " + str(dog.getMood()) + "\nSize: " + str(dog.getSize()))
    
    
    # receive user input
    command = input("What would you like to do (say help for commands)? ")

    # try catch for invalid commands
    try:
        temp = -1
        # lists commands
        if(command == "help" or command == 'Help'):
            print("Command List:\nWalk [distance]\nFeed [amount]\n")
            print("Rename [name]")
        # check for walk
        elif(("walk" in command) or ("Walk" in command)):
            print("Walking dog")
            dog.walkDog(parseString(command))
        # check for feed
        elif(("feed" in command) or ("Feed" in command)):
            print ("Feeding dog")
        elif(("rename" in command) or ("Rename" in command)):
            print ("Renaming dog")
        # check for quit
        elif(command == "quit" or command == 'quit'):
            print ("quitting ...")
            x = False
            
    except:
        print("Invalid command")

    
        
        
        
    

    
