#Programmer: Collin M. Fields
#Date: 11/05/2018
#Purpose: Create the Pig Latin variation of a string passed to the function. (Simplified rules based on only moving the first letter of a consonant word.

#Function to actually alter the string. Should pass only a single word in a string to be altered at any time.
def pigLatinAlter(toBeAltered):
	vowels = "aeiou"
	toBeAltered = toBeAltered.lower()
	if(toBeAltered[0] in vowels):
		return toBeAltered + "ay"
	else:
		return toBeAltered[1:] + toBeAltered[0] + "ay"
