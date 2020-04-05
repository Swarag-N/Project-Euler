'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from p0003 import primeFactors
#Using prime factors funtion from problem3


# to convert a list item to dict espically when
# elements repeat in list to dict for how many times 
def listToDict(list0):
    temp = {}
    for ele in list0:
        temp[ele]=0
    for ele in list0:
        temp[ele]+=1
    return temp

#union of dict [in python ;)] 
def dictUnion(dict1,dict2):
    tempDict = {}
    for key in dict1:
        if key in dict2:
            tempDict[key] = max(dict1[key],dict2[key])
        else:
            tempDict[key]=dict1[key]
    for key in dict2:
        if key in dict1:
            tempDict[key] = max(dict1[key],dict2[key])
        else:
            tempDict[key]=dict2[key]
    return tempDict

# Using Key Value pairs disolving the
# Dict to int => power the key to thier values
def dissolveDict(dict0):
    product = 1
    for key in dict0:
        product*=key**dict0[key]
    return (product)


# Initialization
arr = {}
# Question was upto 20
for i in range(1,20):
    temp = primeFactors(i)
    temp = listToDict(temp)
    arr = dictUnion(temp,arr)
# Disolving the Dictionary 
product = dissolveDict(arr)
print(product)