'''
from p0003 import primeFactors

primes = set([2,3,5])


for i in range(1,2000000):
    if (i%2!=0 and i%3!=0 and i%5!=0):
        a = set(primeFactors(i))
        print(i,'\t:',a)
        primes.update(a)

print('\n\n\n\n\n\n')
print(primes)
print(sum(primes))
'''
marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print(s)
