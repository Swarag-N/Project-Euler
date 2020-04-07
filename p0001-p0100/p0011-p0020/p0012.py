def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

def sumOfFirst_N_Natural(n):
    return (n*(n+1))//2


# n=12375

factorsOfN = []
n=12300
while (len(factorsOfN)<500):
    n+=1
    print(len(factorsOfN),n)
    factorsOfN = factors(sumOfFirst_N_Natural(n))

print('\t\t',len(factorsOfN),'\t\t',sumOfFirst_N_Natural(n),'\t\t',n,'\n\n')




