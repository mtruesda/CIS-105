#
# first real GUI experience
# @MyronTruesdale
# Version 5/13/2020
# Self teaching tkinter
# 

import tkinter

# line by line approach
#def main():
    # create the main window wdget
 #   main_window = tkinter.Tk()
    

    # enter the main loop
  #  tkinter.mainloop()

# call the main
#main()

# object-oriented approach
class myGUI:
    def __init__(self):
        # creating the winow
        self.root = tkinter.Tk()
        #self.frame = tkinter.Frame(width = 500, height = 500)
        
        # create a functioning button
        # self.button = tkinter.Button(self.root, text="Hello World", command = self.message)
        # self.button.pack()

        # testing two labels
        self.label1 = tkinter.Label(self.root, text = "Hello World")
        self.label2 = tkinter.Label(self.root, text = "World says hello")

        # packing the labels
        #self.frame.pack()
        self.label1.pack()
        self.label2.pack()
        
        
        tkinter.mainloop()
        
    def message(self):
        print("Hellooooo")

# initialize class
my_gui = myGUI()

## pack() is a method for finding a spot on screen ##
