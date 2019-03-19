#Programmer: Collin M. Fields
#Date: 03/19/2019
#Purpose: Fibonacci Sequence

#Displays only the value at that point in the sequence.
def fibonacciSequence(n):
	if(n == 1):
		return 1
	elif(n == 0):
		return 0
	else:
		return fibonacciSequence(n-2) + fibonacciSequence(n-1)
		
#Shows entire Fibonacci sequence up to and including the value at n.
def iterativeFibonacciShowing(n):
	fibList = [ 0, 1, 1 ]
	if(n == 0):
		print("0")
		return 0
	elif(n == 1):
		print("0")
		return 1
	else:
		for i in range(n):
			fibList[2] = fibList[0] + fibList[1]
			fibList[1] = fibList[0]
			fibList[0] = fibList[2]
			if(i == 0):
				print("0 1", end = " ")
			else:
				print(fibList[2], end = " ")
		return fibList[2]

#Displays only the value at that point in the sequence.
def iterativeFibonacci(n):
	fibList = [ 0, 1, 1 ]
	if(n == 0):
		return 0
	elif(n == 1):
		return 1
	else:
		print(fibList)
		for i in range(n):
			fibList[2] = fibList[0] + fibList[1]
			fibList[1] = fibList[0]
			fibList[0] = fibList[2]
		return fibList[2]

#Does not work for values equal to or below 6.
#Meant to show the value in the fibonacci sequence just before some static value.
def fibonacciSequenceBeforeValue(value):
	for x in range(value):
		if(iterativeFibonacci(x) < value):
			continue
		else:
			return iterativeFibonacci(x-1)

