#Module for Lab #10, problem #1 problem by Rob Brown. 
#Class Information already exists with name, address, age, and phone_number
#attributes. It also contains all setters/getters for those attributes.

### TO BE USED WITH Lab8Problem3 ###

class Directory:
    #Directory class will create an object that stores name,
    #address, age, and phone number. 
    def __init__(self, name, address, age, phone_number):
        self.__name=name
        self.__address = address
        self.__age=age
        self.__phone_number=phone_number

    #Mutators/Setters
    def set_name(self, name):
        self.__name=name
    def set_address(self, address):
        self.__address=address
    def set_age(self, age):
        self.__age=age
    def set_phone_number(self, phone_number):
        self.__phone_number=phone_number

    #Accessors/Getters
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone_number(self):
        return self.__phone_number

    #Other methods for the Directory class
    def __str__(self):
        return "Name: " + self.__name +\
               "\nAddress: " + self.__address +\
               "\nAge: " + str(self.__age) +\
               "\nTelephone: " + self.__phone_number +\
               "\n"

class Student(Directory):
    def __init__(self, name, address, age, phone_number, major, credits_earned):
        Directory.__init__(self,name,address,age,phone_number)
        self.__major = major
        self.__credits_earned = credits_earned
    def set_major(self, major):
        self.__major = major
    def set_credits_earned(self, credits_earned):
        self.__credits_earned = credits_earned

    def get_major(self):
        return self.__major
    def get_credits_earned(self):
        return self.__credits_earned

    def __str__(self):
        return (Directory(self.get_name(), self.get_address(), self.get_age(),
                          self.get_phone_number()).__str__() +
        "Major: " + self.__major + "\nCredits Earned:" + self.__credits_earned)
    

















        
        
    





    
