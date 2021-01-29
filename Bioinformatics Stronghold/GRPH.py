import READ_FASTA
import sys

data = READ_FASTA.read_fasta('rosalind_grph.txt')

prefixes = {}
suffixes = {}

for entry in data:
    value = data[entry]
    if not value[0:3] in prefixes:
        prefixes[value[0:3]] = []
    if not value[-3:] in suffixes:
        suffixes[value[-3:]] = []
    prefixes[value[0:3]].append(entry)
    suffixes[value[-3:]].append(entry)

with open('grph_output.txt', 'a') as f:
    for key in suffixes:
        if key in prefixes:
            for p in suffixes[key]:
                for s in prefixes[key]:
                    if p != s:
                        f.write("%s %s\n" % (p[1:], s[1:])) #strip >
                            
