def reverseString(toReverse):
	if(isinstance(toReverse, str)):
		return toReverse[::-1]
	else:
		print("You must pass a string to this function")
