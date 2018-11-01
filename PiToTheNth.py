"""
	Programmer: Collin Michael Fields
	Date: 11/1/2018
	Purpose: Calculate the value of Pi out to a certain decimal place. (Currently only works to the 48th decimal place.
"""
import math
from decimal import *

#Setting the precision to a value that will not cause it to error out.
getcontext().prec = 999

#Calculating Pi using the idea that 2 * (arcsin(1 - 1^2) + arcsin(1)) is equal to pi. 
valueOfPi = Decimal(2 * (math.asin(Decimal.sqrt(Decimal((1 - pow(1,2))))) + abs(math.asin(1))))

print("Welcome to the Pi calculator.\nPlease enter a value to calculate pi to that decimal place (Our current limit is 48).")

while(1 == 1):
	userInput = int(input())
	if(userInput > -1 and userInput < 49):
		break
	else:
		print("You have entered an invalid value. Please re-enter a valid number")

valueToBeDisplayed = round(Decimal(valueOfPi), userInput)

print(valueToBeDisplayed)
