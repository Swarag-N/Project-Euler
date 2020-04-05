'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(str1):
    #finding length to run a loop in such a way that,
    # comparing the string from forward and backward by one character 
    len1 = len(str1)
    for i in range(len1//2):
        if str1[i] != str1[len1-1-i]:
            return(False)
    return(True)

# Having two loops to form 2 numbers multiple each 
# Starting from 999*999 ... 999*899 ... 899*899 ... 899*799
for a in range(999,1,-1):
    for b in range(a,a-100,-1):
        if isPalindrome(str(a*b)):
            print(a*b,"\t",isPalindrome(str(a*b)),"\t",a,b)
            break
    else:
        #Using For Else Clause to break two loops at a single time
        continue
    break



'''
More About for/else clause
https://book.pythontips.com/en/latest/for_-_else.html#else-clause
'''