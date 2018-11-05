#Programmer: Collin M. Fields
#Date: 11/05/2018
#Purpose: Count the number of words in a text.

def wordCounter(textToCountWords):
	wordCount = 0
	textToBeCounted = textToCountWords.split(" ")
	for word in textToBeCounted:
		wordCount += 1
	return wordCount

