#Programmer: Collin M. Fields
#Date: 11/05/2018
#Purpose: check if a string is a palindrome, will be stripping the spaces from the string in case of a multiword palindrome.

#Recursive palindrome check.
def recursivePalindromeChecker(stringToBeChecked):
	#Exit condition for recursion loop.
	if(len(stringToBeChecked) == 1 or len(stringToBeChecked) == 0):
		return True
	#Getting rid of possible formatting of the characters that may cause an error.
	stringToBeChecked = stringToBeChecked.lower()
	stringToBeChecked = stringToBeChecked.strip()
	#First and Last value must match.
	if(stringToBeChecked[0] == stringToBeChecked[-1]):
		return recursivePalindrome(stringToBeChecked[1:len(stringToBeChecked)-1])
	else:
		return False
		

#Palindrome check done iteratively using the negative indexing that python allows for backwards traversal of a string.
def iterativePalindromeChecker(stringToBeVerified):
	#Getting rid of possible formatting of the characters that may cause an error.
	stringToBeVerified = stringToBeVerified.lower()
	stringToBeVerified = stringToBeVerified.strip()
	#Traverses half of the string.
	for i in range(len(stringToBeVerified)):
		if(stringToBeVerified[i] == stringToBeVerified[-(i + 1)]):
			continue
		else:
			return False
	return True
