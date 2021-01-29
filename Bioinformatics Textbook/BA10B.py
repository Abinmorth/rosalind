emitted = 'zxzyxyyxzzxxyzxxyyxxyyzxxzzzyyxyyxyyxxzyyxyyzxyyyz'
alphabet = ['x','y','z']
states = ['A','B']
emission = [[0.24, 0.459, 0.3], [0.547, 0.412, 0.041]]

path = 'BABBAAABAABBBBAAABBABAAAABBBAABABBABBBBABABBAABAAA'

probability = 1
for k in range(0, len(path)):
	indexState = states.index(path[k])
	indexAlphabet = alphabet.index(emitted[k])
	probability *= emission[indexState][indexAlphabet] 

print(probability)
