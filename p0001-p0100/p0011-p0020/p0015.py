# This a very Good and Old Question of Permutations.

def npr(n,r):
	temp = 1
	while(n!=r):
		temp*=n
		n-=1
	return temp

def ncr(n,r):
    return (npr(n,n-r)//npr(r,1))

print(ncr(40,20))

# Explanation from my side will be soon
# I recommend you on reading this
# https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/