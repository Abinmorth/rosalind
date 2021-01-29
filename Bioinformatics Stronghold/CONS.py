import READ_FASTA
from collections import defaultdict

data = READ_FASTA.read_fasta('cons_in.txt')
index = 0
profile = {'A':[],'C':[],'G':[],'T':[]}
consensus = ''

sequence = next(iter(data.values()))
seqLen = len(sequence) #guaranteed to be equal for all sequences

# initialise with 0s
for i in range(0, seqLen):
    profile['A'].append(0)
    profile['C'].append(0)
    profile['G'].append(0)
    profile['T'].append(0)

for seq in data.values():
    for i in range(0, seqLen):
        if seq[i] == 'A':
            profile['A'][i] += 1
        elif seq[i] == 'C':
            profile['C'][i] += 1
        elif seq[i] == 'G':
            profile['G'][i] += 1
        elif seq[i] == 'T':
            profile['T'][i] += 1

#program is biased towards G > C > A > T if multiple consensus sequences exist
for i in range(0, seqLen):
    if profile['G'][i] >= profile['A'][i] and profile['G'][i] >= profile['C'][i] and profile['G'][i] >= profile['T'][i]:
        consensus += 'G'
    elif profile['C'][i] >= profile['A'][i] and profile['C'][i] >= profile['G'][i] and profile['C'][i] >= profile['T'][i]:
        consensus += 'C'
    elif profile['A'][i] >= profile['C'][i] and profile['A'][i] >= profile['G'][i] and profile['A'][i] >= profile['T'][i]:
        consensus += 'A'
    elif profile['T'][i] >= profile['A'][i] and profile['T'][i] >= profile['G'][i] and profile['T'][i] >= profile['C'][i]:
        consensus += 'T' 

with open('cons_out.txt', 'w') as file_out:
    file_out.write(consensus)
    file_out.write('\n')
    file_out.write('A: %s' % (' '.join(map(str, profile['A']))))
    file_out.write('\n')
    file_out.write('C: %s' % (' '.join(map(str, profile['C']))))
    file_out.write('\n')
    file_out.write('G: %s' % (' '.join(map(str, profile['G']))))
    file_out.write('\n')
    file_out.write('T: %s' % (' '.join(map(str, profile['T']))))
