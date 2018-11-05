#Programmer: Collin M. Fields
#Date: 11/05/2018
#Purpose: Function to reverse a function in python.

def reverseString(toReverse):
	if(isinstance(toReverse, str)):
		return toReverse[::-1]
	else:
		print("You must pass a string to this function")
