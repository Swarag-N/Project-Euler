def collatz(num):
    temp=0
    while(num!=1):
        if num%2==0:
            temp+=1
            num=num//2
        else:
            temp+=2
            num=(3*num+1)//2
    return temp

ans = 0
maxNum = 0
for i in range(1000000,100000,-1):
    temp = collatz(i)
    if temp>ans:
        ans=temp
        maxNum=i
    # ans = max(temp,ans)
print(maxNum)


# less than 106 is 837799, which has 524 steps,
# https://en.wikipedia.org/wiki/Collatz_conjecture
# The Collatz Conjecture - Numberphile
# https://youtu.be/5mFpVDpKX70