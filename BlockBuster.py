import tkinter
#import tkMessageBox

import random
import math

#creates the window
root = tkinter.Tk()


#setting initial degrees for ball direction
degrees = 0

#wins for difficulty variety
wins = 0

#initalizing tkinter variables to use them in functions
ball = 0
playerBar = 0

#creating the canvas
canvas = tkinter.Canvas(root, height=600, width=600, bg='white')
canvas.grid(row=0,column=0)

blockOne = canvas.create_rectangle(125,125,225,150, fill='grey', state='hidden')
blockTwo = canvas.create_rectangle(250,125,350,150, fill='grey', state='hidden')
blockThree = canvas.create_rectangle(375,125,475,150, fill='grey', state='hidden')
blockFour = canvas.create_rectangle(125, 85, 225, 110, fill='grey', state='hidden')
blockFive = canvas.create_rectangle(250,85, 350, 110, fill='grey', state='hidden')
blockSix = canvas.create_rectangle(375,85,475,110, fill='grey', state='hidden')

#creating block scores, while repetitive, it will allow the individual scores to be added from the blocks.
blockScore = 250

#objective hit blocks' points text
textOne = canvas.create_text(175,135, text=str(blockScore), state='hidden')
textTwo = canvas.create_text(300,135, text=str(blockScore), state='hidden')
textThree = canvas.create_text(425,135, text=str(blockScore), state='hidden')
textFour = canvas.create_text(175,100, text=str(blockScore), state='hidden')
textFive = canvas.create_text(300,100, text=str(blockScore), state='hidden')
textSix = canvas.create_text(425,100, text=str(blockScore), state='hidden')

#initializes variables
winsDisplay = 0
playerPointas = 0

#creating the items in the canvas
title = canvas.create_text(300,100, text="BLOCKBUSTER")
buttonBG = canvas.create_rectangle(270,140,330,180, fill="grey40", outline='grey60', state='normal')
buttonTXT = canvas.create_text(300, 160, text='START', state='normal')

#end screen pieces
game_over = canvas.create_text(300,100, text='GAME OVER, TRY AGAIN?', state='hidden')
points_end = canvas.create_text(300, 120, text='',state='hidden')

#game end texts
winText = canvas.create_text(300,100, text='You win! Play again?', state='hidden')

#setting up the player points piece
playerPoints = canvas.create_text(30,25,text=("Points: "+str(playerPointas)),state='hidden')
winsText = canvas.create_text(30, 40, text=("Wins: "+str(winsDisplay)), state='hidden')

#used is for testing if the blocks have already been hit
notUsed1 = True
notUsed2 = True
notUsed3 = True
notUsed4 = True
notUsed5 = True
notUsed6 = True
notUsed7 = True
notUsed8 = True
notUsed9 = True

#returns score for the blocks based off of the wins
def returnBlockScore():
    global playerPointas
    global winsDisplay
    global blockScore
    
    if winsDisplay<1:
        playerPointas = 0
    if winsDisplay<3:
        blockScore = 250
    if winsDisplay==3:
        blockScore = 500
    if winsDisplay==5:
        blockScore = 750
    if winsDisplay>=10:
        blockScore = 1000
    
    return blockScore

#does the handling of the wincount and point reset
def winCount(n):
    global wins
    global winsDisplay
    global playerPointas
    
    if n == 0:
        wins = 0
        winsDisplay = 0
        playerPointas = 0
    if n == 1:
        wins = wins + .1
        winsDisplay = winsDisplay + 1

#hides stuff so that screens can be set up
def hideStuff(number):
    canvas.itemconfig(playerBar, state='hidden')
    canvas.itemconfig(blockOne, state='hidden')
    canvas.itemconfig(blockTwo, state='hidden')
    canvas.itemconfig(blockThree, state='hidden')
    canvas.itemconfig(blockFour, state='hidden')
    canvas.itemconfig(blockFive, state='hidden')
    canvas.itemconfig(blockSix, state='hidden')
    
    canvas.itemconfig(textOne, state='hidden')
    canvas.itemconfig(textTwo, state='hidden')
    canvas.itemconfig(textThree, state='hidden')
    canvas.itemconfig(textFour, state='hidden')
    canvas.itemconfig(textFive, state='hidden')
    canvas.itemconfig(textSix, state='hidden')
    
    canvas.itemconfig(ball, state='hidden')
    
    print('screen resetted')

    #checks input to set up different screens
    if number == 1:
        #setting up "you win"
        canvas.itemconfig(winText, state='normal')
        
    if number == 2:
        #setting up game_over
        canvas.itemconfig(game_over, state='normal')
        
        
    canvas.itemconfig(buttonBG, state='normal')
    canvas.itemconfig(buttonTXT, state='normal')
    
    playerPointasText = str(playerPointas) + " points!"
    canvas.itemconfig(points_end, state='normal', text=playerPointasText)

def checkCoords():
    
    global ball
    global playerBar
    
    global playerPointas
    global wins
    
    global notUsed1
    global notUsed2
    global notUsed3
    global notUsed4
    global notUsed5
    global notUsed6
    
    px1, py1, px2, py2 = canvas.coords(playerBar)
    x1, x2, y1, y2 = canvas.coords(ball)
    
    global degrees
    
    #checks if the ball hits the walls and if so it uses math to flip its direction
    if x1<0 or x1>600:
        degrees = math.pi - degrees
    
    #for bouncing off the top of the screen
    if y2<0: 
        degrees = degrees * -1
    
    #for hitting the bottom of the screen and initiating gameover
    if y2>canvas.winfo_height():
        print("game over")
        
        canvas.delete(ball)
        
        hideStuff(2)
        winCount(0)
        
        return winsDisplay
        
    
    #for when hitting the paddle
    if y2 > 560:
        if x1>px1-4 and x1<px2+4:
            degrees = degrees * -1
            print(px2)
            
    #for hitting block1
    if y2>125 and y2<150:
        if x1>125 and x1<225:
            if notUsed1:
                print("IN THE ZONE")
                
                #helps the code decide whether the ball bounces vertically or horizontally
                if y2<130 or y2>145:
                    degrees = degrees * -1
                elif y2>130 and y2<145:
                    if x1>125 and x1<225:
                        degrees = math.pi - degrees
                
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockOne, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textOne, state='hidden')
                notUsed1 = False
                
    #for hitting block2
    if y2>125 and y2<150:
        if x1>250 and x1<350:
            if notUsed2:
                print("IN THE ZONE")
                
                #helps the code decide whether the ball bounces vertically or horizontally
                if y2<130 or y2>145:
                    degrees = degrees * -1
                elif y2>130 and y2<145:
                    if x1>250 and x1<350:
                        degrees = math.pi - degrees
                
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockTwo, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textTwo, state='hidden')
                notUsed2 = False
    
    #for hitting block3
    if y2>125 and y2<150:
        if x1>375 and x1<475:
            if notUsed3:
                print("IN THE ZONE")
                
                #helps the code decide whether the ball bounces vertically or horizontally
                if y2<130 or y2>145:
                    degrees = degrees * -1
                elif y2>130 and y2<145:
                    if x1>375 and x1<475:
                        degrees = math.pi - degrees
                
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockThree, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textThree, state='hidden')
                notUsed3 = False
        
    #for hitting block4
    if y2>85 and y2<110:
        if x1>125 and x1<225:
            if notUsed4:
                print("IN THE ZONE")
                
                #helps the code to decide whether the ball bounces vertically or horizontally
                if y2<90 or y2>105:
                    degrees = degrees * -1
                elif y2>90 and y2<105:
                    if x1>125 and x1<225:
                        degrees = math.pi - degrees
                
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockFour, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textFour, state='hidden')
                notUsed4 = False
    
    #for hitting block5
    if y2>85 and y2<110:
        if x1>255 and x1<345:
            if notUsed5:
                print("IN THE ZONE")
                
                #helps the code to decide whether the ball bounces vertically or horizontally
                if y2<90 or y2>105:
                    degrees = degrees * -1
                elif y2>90 and y2<105:
                    if x1>255 and x1<345:
                        degrees = math.pi - degrees
                        
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockFive, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textFive, state='hidden')
                notUsed5 = False
    
    #for hitting block6
    if y2>85 and y2<110:
        if x1>375 and x1<475:
            if notUsed6:
                print("IN THE ZONE")
                
                #helps the code to decide whether the ball bounces vertically or horizontally
                if y2<90 or y2>105:
                    degrees = degrees * -1
                elif y2>90 and y2<105:
                    if x1>375 and x1<475:
                        degrees = math.pi - degrees
                        
                playerPointas = playerPointas + blockScore
                canvas.itemconfig(blockSix, state='hidden')
                canvas.itemconfig(playerPoints, text="Points: " + str(playerPointas))
                canvas.itemconfig(textSix, state='hidden')
                notUsed6 = False
    
    if notUsed1 == False:
        if notUsed2 == False:
            if notUsed3 == False:
                if notUsed4 == False:
                    if notUsed5 == False:
                        if notUsed6 == False:
                            
                            print('You Win!')
                
                            canvas.delete(ball)
                            
                            hideStuff(1)
                            winCount(1)
                            
                            return None

def ball_moveLoop():
    
    #globalizing necessary variables
    global ball
    
    #setting up speed difficulty changes
    movement = 5*(wins+1)
    
    #determines the x and y components of the balls movement, so that I may use it later
    x = movement * math.cos(degrees)
    y = movement * math.sin(degrees)
       
    #actually moves the ball with the provided components
    canvas.move(ball, x, y)
    degrees

    #used to check the balls coordinates constantly and see if they meet any conditions    
    checkCoords()
    
    #somewhat loops the animation
    canvas.after(20, ball_moveLoop)

#begins the game
def begin(event):
    
    #globalizing variables
    global buttonBG
    global buttonText
    
    global playerPointas
    global playerPoints
    
    global degrees
    
    global ball
    global playerBar
    
    global blockScore
    
    global notUsed1
    global notUsed2
    global notUsed3
    global notUsed4
    global notUsed5
    global notUsed6
    
    global playerPointas
    
    #randomizes the player degrees direction
    degrees = random.uniform(3.5,6)
    
    #prevents the direction from making the game awkward or difficult
    while degrees>4.5 and degrees<5:
        degrees = random.uniform(3.5,6)
    
    #may seem redundant because this is done eawrlier in code however, this is so that when the code restarts itself it allows the blocks to be touched, Inversely, if they were not there, the ball would be adding points for every time it passes through
    notUsed1 = True
    notUsed2 = True
    notUsed3 = True
    notUsed4 = True
    notUsed5 = True
    notUsed6 = True
    
    #tests the event
    print("game has begun")
    
    #Hides title stuff
    canvas.itemconfig(buttonBG, state='hidden')
    canvas.itemconfig(buttonTXT, state='hidden')
    canvas.itemconfig(title, state='hidden')
    canvas.itemconfig(winText, state='hidden')
    
    #hides stuff if the game is a restart
    canvas.itemconfig(game_over, state='hidden')
    canvas.itemconfig(points_end, state='hidden')
    
    #creates the player-controlled bar
    playerBar = canvas.create_rectangle(225,525,375,540, fill='black')
    canvas.move(playerBar, 0, 50)
    canvas.update()    
    
    #creates the points and wins and displays them on the canvas    
    canvas.itemconfig(playerPoints, state='normal', text='Points: ' + str(playerPointas))
    canvas.itemconfig(winsText, state='normal', text='Wins: '+str(winsDisplay))
    
    #make the objective hit blocks appear
    canvas.itemconfig(blockOne, state='normal')
    canvas.itemconfig(blockTwo, state='normal')
    canvas.itemconfig(blockThree, state='normal')
    canvas.itemconfig(blockFour, state='normal')
    canvas.itemconfig(blockFive, state='normal')
    canvas.itemconfig(blockSix, state='normal')
    
    #finds out the current blockScore and sets it
    returnBlockScore()
    print(str(blockScore) + "is the blockScore")
    
    #showing the points texts
    canvas.itemconfig(textOne,state='normal',text=blockScore)
    canvas.itemconfig(textTwo,state='normal',text=blockScore)
    canvas.itemconfig(textThree,state='normal',text=blockScore)
    canvas.itemconfig(textFour,state='normal',text=blockScore)
    canvas.itemconfig(textFive,state='normal',text=blockScore)
    canvas.itemconfig(textSix, state='normal', text=blockScore)
    
#registers keys and uses them to create playermovement
    def keyMove(e):
        
        #registers if key "a" or "A" are pressed
        if e.char == "a" or e.char == "A":
            
            #moves the rectangle
            canvas.move(playerBar, -20, 0)         
            canvas.update()
            
            
        #registers if key "d" or "D" are pressed
        elif e.char == "d" or e.char == "D":

            #moves the rectangle
            canvas.move(playerBar, 20, 0)         
            canvas.update()
            
    
    #binds key usage to the function keyMove
    canvas.bind("<Key>", keyMove)
    
    #creates the ball and calls the "animation"
    ball = canvas.create_oval(295,550,305,560, fill='black')
    ball_moveLoop()
    
#When the items are clicked they call begin()
canvas.tag_bind(buttonBG, "<Button-1>", begin)
canvas.tag_bind(buttonTXT, "<Button-1>", begin)

canvas.pack()
canvas.focus_set()

root.mainloop()
