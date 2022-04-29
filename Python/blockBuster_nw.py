#
# BlockBuster done right
# @MyronTruesdale
# Version 5/13/2020
#

import tkinter

class brickBroken:
    def __init__(self):
        # initializing root and frame
        self.root = tkinter.Tk()
        self.top_frame = tkinter.Frame(width = 600, height = 325)
        self.bottom_frame = tkinter.Frame(width = 600, height = 325)

        # packing the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # creating widgets
        self.titleLabel = tkinter.Label(self.top_frame, text = "BlockBuster")
        self.startButton = tkinter.Button(self.bottom_frame, text = "Start Game!",
                                          command = self.startGame)
        # packing widgets
        self.titleLabel.pack(side = "top")
        self.startButton.pack(side = "top")
        
    def startGame(self):
        print("Hi")
my_game = brickBroken()
