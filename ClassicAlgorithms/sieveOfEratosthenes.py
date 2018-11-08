#Programmer: Collin M. Fields
#Date: 11/08/2018
#Purpose: Create the Sieve of Eratosthenes

def sieveOfEratosthenes(n):
	listOfNotPrimes = []
	listOfPrimes = []
	for i in range(2, n+1):
		if i not in listOfNotPrimes:
			listOfPrimes.append(i)
			for j in range(i*i, n+1, i):
				listOfNotPrimes.append(j)
	return listOfPrimes
