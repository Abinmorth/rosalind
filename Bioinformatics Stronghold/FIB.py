def rabbits(n, k):
    if n == 1:
        return (0,1)
    elif n == 2:
        return (1,0)
    else:
        (adult1, young1) = rabbits(n-2,k)
        (adult2, young2) = rabbits(n-1,k)

        adult3 = adult2 + young2
        young3 = adult2 * k
        return (adult3, young3)

n = 33
k = 3

(adult, young) = rabbits(n,k)
print(adult + young)
