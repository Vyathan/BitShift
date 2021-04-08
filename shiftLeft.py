"""
Program: shiftLeft.py
Programmer: Matt Brundage II
Date: 4/7/21
Shifts bits one place to the left and prints the result.
"""

#Input the string
string = input("Please Enter the String: ")

#Shift bit
shiftLeft = string[(-1)*((string)-1):]

result = shiftLeft + string[0]

#Print result
print(result)

"""
Dr. Brown, I have tried this damn thing so many different ways
I know that I am getting an index error because my input is an integer
Everytime I try to convert to a string I get a whole slew of errors
You'll see I wrote the two scripts completely different ways
I've googled this to death
I will be excited to see your comments on how to fix this
"""