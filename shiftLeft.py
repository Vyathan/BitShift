"""
Program: shiftLeft.py
Programmer: Matt Brundage II
Date: 4/7/21
Shifts bits one place to the left and prints the result.
"""

#Input the string
string = input()

#Shift bit
shiftLeft = string[1:]+string[0]

#Print result
print(shiftLeft)