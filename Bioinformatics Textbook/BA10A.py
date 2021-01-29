path = 'AABBBABBBABAAAAABBAABAAABABABAABBBABABBBBAABBBBBBA'
transitions = {
                'AA' : 0.325,
                'AB' : 0.675,
                'BA' : 0.286,
                'BB' : 0.714
        }

probability = 0.5
for k in range(0, len(path) - 1):
	transition = path[k:k+2]
	probability *= transitions[transition]
print(probability)
