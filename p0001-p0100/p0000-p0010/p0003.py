'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

# Python program to print prime factors 

import math 

# A function to print all prime factors of 
# a given number n 
def primeFactors(n): 
	arr = []
	# Print the number of two's that divide n 
	while n % 2 == 0: 
		arr.append(2), 
		n = n / 2
		
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		
		# while i divides n , print i ad divide n 
		while n % i== 0: 
			arr.append (i), 
			n = n / i 
			
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		arr.append(n)
	
	return arr
		

# Initialization 
n = 600851475143
# calling primeFactors funtion
arr = primeFactors(n)
# Removing Duplicate Values
arr = tuple(arr)
#Printing Answer.
print(max(arr)) 

# This code of primefactors function is contributed by Harshit Agrawal 
