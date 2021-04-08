"""
Program: shiftRight.py
Programmer: Matt Brundage II
Date: 4/7/21
Shifts bits one place to the right and prints the result.
"""

#Input the string
string = input("Please Enter the String: ")

#Shift bit
shiftRight = string[-1]+string[0:-1]

#Print result
print(shiftRight)