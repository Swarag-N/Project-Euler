'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# Python3 program to generate pythagorean 
# triplets smaller than a given limit 

# Function to generate pythagorean 
# triplets smaller than limit 
def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    # Limiting c would limit 
    # all a, b and c 
    while c < limits : 
        # Now loop on n from 1 to m-1 
        # 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
            # if c is greater than 
            # limit then break it 
            if c > limits : 
                break
            print(a, b, c)
            if ((a+b+c)==limits):
                print('\t\t',a,b,c,a*b*c)
                return (a,b,c)
        m = m + 1



if __name__ == '__main__' :
        limit = 1000
        ans = pythagoreanTriplets(limit)


'''
Without programming:

a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
a + b + c = 1000;

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
2mn + 2m^2 = 1000;
2m(m+n) = 1000;
m(m+n) = 500;

m>n;

m= 20; n= 5;

a= 200; b= 375; c= 425;
'''

# This code is contributed by Shrikant13. 
