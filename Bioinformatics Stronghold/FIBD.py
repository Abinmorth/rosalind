def memoize(f):
    memo = {}
    def helper(x,y):
        if x not in memo:            
            memo[x] = f(x,y)
        return memo[x]
    return helper

@memoize
def rabbits(n, k):
    if n == 1:
        return (0,1)
    elif n == 2:
        return (1,0)
    else:
        (adult1, young1) = rabbits(n-2,k)
        (adult2, young2) = rabbits(n-1,k)
        if n>k:
            (adultX, youngX) = rabbits(n-k,k)
        else:
            (adultX, youngX) = (0,0)

        adult3 = adult2 + young2 - youngX
        young3 = adult2
        return (adult3, young3)

n = 90
k = 19

memo = memoize(rabbits)
(adult, young) = rabbits(n,k)
print(adult + young)
