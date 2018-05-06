def rabbits(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rabbits(n-2,k)*k + rabbits(n-1,k)

n = 33
k = 3
print(rabbits(n,k))
