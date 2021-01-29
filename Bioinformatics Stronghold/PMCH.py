def fakult(n):
    if n == 0:
        return 1
    else:
        return n * fakult(n - 1)


sequence = 'CCACCACUUCGCAGACUGUGUUGGUCGGCUUAUUUGAGAAGAAGGAUCAGUCCCCGCUGCAAAUGAUACG'
countA = sequence.count('A')
countU = sequence.count('U')
countC = sequence.count('C')
countG = sequence.count('G')

if(countA == countU and countC == countG):
    print("Balanced")
    matchings = fakult(countA)*fakult(countC)
    print(matchings)
    
