"""
	Programmer: Collin Michael Fields
	Date: 11/1/2018
	Purpose: Calculate the value of E out to a certain decimal place. (Currently only works to the 48th decimal place.
"""
import math
from decimal import *

#Setting the precision to a value that will not cause it to error out.
getcontext().prec = 999

print("Welcome to the E calculator.\nPlease enter a value to calculate e to that decimal place (Our current limit is 48).")

while(1 == 1):
	userInput = int(input())
	if(userInput > -1 and userInput < 49):
		break
	else:
		print("You have entered an invalid value. Please re-enter a valid number")

valueToBeDisplayed = round(Decimal(math.e), userInput)

print(valueToBeDisplayed)
