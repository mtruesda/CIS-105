###
#
# @MyronTruesdale
# 4/21/2021
# V1.0
#
###

# imports
import mysql.connector
import tkinter

# connecting to the server
mydb = mysql.connector.connect(
  host="DESKTOP-BJNO04E",
  user="romyn",
  password="G0n3B@n@n@s06"
)

# gui
class gui:
    # initializing gui with elements
    def __init__(self):
        
        # creating root reference
        self.root = tkinter.Tk()

        # creating elements
        self.label1 = tkinter.Label(self.root, text = "Login Page")
        self.user = tkinter.Text(self.root, width=20, height=1)
        self.pw = tkinter.Text(self.root, width=20, height=1)
        self.login = tkinter.Button(self.root,width=10,height=1,text='Login',command=self.loginButton)
        
        # pack elements
        self.label1.pack()
        self.user.pack()
        self.pw.pack()
        self.login.pack()

        # gui mainloop
        tkinter.mainloop()

    # defines loginButton action
    def loginButton(self):
        print("logging in ... ")

# creates the gui
myGui = gui()
