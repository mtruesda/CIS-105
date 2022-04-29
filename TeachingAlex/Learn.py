#
# @MYRON TRUESDALE
# V1.0
# 4/20/2021
#

# opens
f = open("demofile2.txt", "w")

# writes
f.write("a\n")
f.write("b\n")
f.write("c\n")
f.write("d\n")
f.write("e\n")
f.write("f\n")
f.write("a\n")
f.write("a\n")
f.write("a\n")
f.write("b\n")
f.write("f\n")

# closes
f.close()

# function for checking if the key exists
def checkKey(dict, key):
      
    if key in dict.keys():
        return key
    else:
        return ""

# variables1
f = open("demofile2.txt", "r")
dictionary = {}

# iterates through file
for line in f:
    rstripped = line.rstrip('\n')
    if checkKey(dictionary, rstripped) != "" :
        dictionary[rstripped] += 1
    else:
        dictionary[rstripped] = 1

# prints dictionary
print(dictionary)

# resets the file for viewing full print
f.close()
f = open("demofile2.txt", "r")

# prints the file
print("\n" + f.read())



