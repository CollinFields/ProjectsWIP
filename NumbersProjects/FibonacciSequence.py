#Programmer: Collin M. Fields
#Date: 11/07/2018
#Purpose: Fibonacci Sequence

def fibonacciSequence(n):
	if(n == 1):
		print(1, end = " ")
		return 1
	elif(n == 0):
		print(0, end = " ")
		return 0
	else:
		print(fibonacciSequence(n-2) + fibonacciSequence(n-1), end = " ")
		return fibonacciSequence(n-2) + fibonacciSequence(n-1)
		
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

#Does not work on values below 6
def fibonacciSequenceBeforeValue(value):
	for x in range(value):
		if(iterativeFibonacci(x) < value):
			continue
		else:
			return iterativeFibonacci(x-1)
