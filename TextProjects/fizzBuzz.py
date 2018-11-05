#Programmer: Collin M. Fields
#Date: 11/05/2018
#Purpose: Goes from 1 to 100 and for each value that is evenly divisible by 3, prints Fizz. If evenly divisible by 5, prints Buzz.
#If both, print FizzBuzz

for counterVariable in range(1, 101):
	stringToBePrinted = ""
	if (counterVariable % 3 == 0):
		stringToBePrinted = "Fizz"
	if (counterVariable % 5 == 0):
		stringToBePrinted += "Buzz"
	if (stringToBePrinted == ""):
		print (counterVariable)
	else:
		print (stringToBePrinted)
