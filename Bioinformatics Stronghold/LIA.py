def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fakult(n):
    if n == 0:
        return 1
    else:
        return n * fakult(n - 1)

def choose(n, k):
    return fakult(n) / (fakult(k) * fakult(n-k))

memoize(fakult)

generationI = {'xx': 0, 'XX': 0, 'Xx': 1}
n = 2
k = 1

for i in range(0, k):
        xx = generationI['xx'] * 0.5 + generationI['Xx'] * 0.25
        XX = generationI['XX'] * 0.5 + generationI['Xx'] * 0.25 
        Xx = generationI['XX'] * 0.5 + generationI['xx'] * 0.5  + generationI['Xx'] * 0.5
        generationI = {'xx': xx, 'XX': XX, 'Xx': Xx}
        
total = 2**k
p = generationI['Xx'] ** 2 / total
cumulatedBinomial = 0
for i in range(0,n):
    cumulatedBinomial += choose(total, i) * (p**i) * ((1-p)**(total-i))
print(1-cumulatedBinomial)
