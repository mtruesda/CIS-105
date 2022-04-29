import sympy as sym
from sympy import *
import math

# setting symbols
x, y = sym.symbols('x y')

# function sets
fullFunction = 0
dupFullFunction = 0
functionSub = 0

# functions themselves
function = E**3*x
dupFunction = function.copy()

# inputtable items (n and base)
length = int(input("How many iterations? "))
base = int(input("What is the base? "))

# for handling just w/ variables
print('\n\n##### JUST TAYLOR #####')

for i in range(length):
    
    for j in range(i):
        function = sym.diff(function)

    fullFunction = (fullFunction) +(((function)*(x-base)**i)/math.factorial(i))    

print(fullFunction)

# handling with the base
print('\n\n##### SUBBING BASES #####')

for i in range(length):
    
    for j in range(i):
        dupFunction = sym.diff(dupFunction)
        functionSub = dupFunction.subs(x,base)

    dupFullFunction = (dupFullFunction) +((functionSub*(x-base)**i)/math.factorial(i))    

print(dupFullFunction)

print("\n\n##### PLUGGING #####")

value = input("Do you want to sub full function? (enter value if want, 'N' otherwise) ")

if(value != 'N'):
    print(float(dupFullFunction.subs(x, float(value))))


