def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def catalan(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        c = 0
        for k in range(1, n+1):
            c+= catalan(k-1)*catalan(n-k)
        return c

memo = memoize(catalan)

sequence = 'UAGCGUGAUCAC'
countA = sequence.count('A') # guaranteed to equal count U
countG = sequence.count('G') # guaranteed to equal count C
countC = sequence.count('C')
countU = sequence.count('U')

if countA == countU and countG == countC:
    print('Balanced')

cA = catalan(countA)  # place and pair As and 
cG = catalan(countG)
print(catalan(countA + countG))
print(cA)
print(cG)
print(catalan(countA + countG) - cA - cG)

#TODO

