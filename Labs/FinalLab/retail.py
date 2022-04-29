# Programming Exercise 10-5
# Give your name here so you can get credit for
# the take-home portion of the final exam!

# MYRON TRUESDALE FINAL - will use ### to mark mistakes

class RetailItem:
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price
        
    def set_description(self, description):
        self.__description = description

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    ### the functions down are tabbed an extra time which will cause issues
    def get_description(self):
        return self.__description
            
    def get_inventory(self):
        return self.__inventory
            
    def get_price(self):
        return self.__price

    def __str__(self):
        ### had to concatenate the get_price function to string
        result = 'Description: ' + self.get_description() + '\n' + \
                    'Units in inventory: ' + str(self.get_inventory()) + \
                    '\nPrice: $' + str(self.get_price())
        return result


