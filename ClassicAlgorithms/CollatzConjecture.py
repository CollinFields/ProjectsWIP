#Programmer: Collin M. Fields
#Date: 03/19/2019
#Purpose: Collatz Conjecture

def CollatzConjectureMethod(n):
	counter = 0
	while True:
		if(n == 1):
			return counter
		elif(n%2 == 0):
			n = n/2
			counter += 1
		else:
			n = n*3 + 1
			counter += 1
