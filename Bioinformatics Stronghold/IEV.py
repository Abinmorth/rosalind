data = '16355 18605 17264 16887 19051 17490'
dataAsList = list(map(int, data.split()))
genotypes = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
genes = {'AA': 0, 'Aa': 0, 'aa':0}

expected = dataAsList[0] * 1 + dataAsList[1] * 1 +  + dataAsList[2] * 1
expected += dataAsList[3] * 0.75
expected += dataAsList[4] * 0.5

print(expected * 2)
            
