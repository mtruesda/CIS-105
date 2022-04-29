#
# This code will take the yearly attendance totals for Fred and place it on a graph
# @MyronTruesdale
# 4/19/2020
# Lab 6 - Problem 2
# 

# importing matplotlib
import matplotlib.pyplot as plt

# variables
fredDoc = open("Fred_Keys_attendance.txt", "r")
x_coords = list(range(2005, 2019))
fredsList = fredDoc.readlines()

for a in fredsList:
    a_index = fredsList.index(a)
    new = int(a.rstrip("\n"))
    fredsList[a_index] = new
    

print(fredsList)

# intro function
def intro():
    print("This code will take the yearly attendance totals for Fred and place it on a graph")

# graphing function
def graphing():
    # titles
    plt.title("Fred Keys Attendance")
    plt.xlabel("Year")
    plt.ylabel("Amount of Attendance")

    # plotting and limits
    plt.plot(x_coords, fredsList)
    plt.xlim(xmin=2005,xmax=2018)

    # ticks (felt the y was unnecessary)
    plt.xticks(list(range(2005,2019)))

    # preference
    plt.grid(True)

    # shows the plot
    plt.show()

intro()
graphing()
    


