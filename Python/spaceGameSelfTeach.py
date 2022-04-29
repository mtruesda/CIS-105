# import
import tkinter
import tkinter.messagebox

# gui Class
class spaceGame:
    def __init__(self):
        # creates the root
        self.root = tkinter.Tk()

        # forms title screen
        self.initial()
        
        # runs tkinter loop
        tkinter.mainloop()

    def initial(self):
        self.title = tkinter.Label(self.root,text="SPACE GAME")
        self.startButton = tkinter.Button(self.root,text="START GAME",command=self.gameStarted)
        self.title.pack()
        self.startButton.pack()

    #def titleScreen():
        #self.title.config(self.root,state="normal")
        #self.startButton.config(self.root,state="normal")
        #space for image

        #self.title.pack()
        #self.startButton.pack()
        
    #def gameStarted(self):
        #self.title.config(self.root,state="disabled")
        #self.title.config(self.root,state="hidden")
        #space for image

        #self.title.pack()
        #self.startButton.pack()
        

game = spaceGame()
