dna = "ATCGCAAATTGGTATGCTTCAGAATAGGTGTAGGTATCTCTTGCCGGACGTTCGTGATCGTATCGAGTCCACTAAAAGGTACGTCGGGCAGGACCGGCTAGCCCTGTGACTACTAGTAGACAATAACACCTTGGCCCTGAGATCCCATTGCTAACAGGGCGCTAGCTGTAGGCAAAACGAGAAGAGTTAAAGCTAGAGGGGATCCCGGCCGGGTCGAGCTATCAGTGAACCGCGGTCGCTAGGCCCTCCTCAGACTTGGTAAGATAAGCAGCTGCAATTGAGGCTGTTTTAAAGCTGAGGAGCCATAACTGGAACGAGACCTTATGGCCCTCTTAACAAACATGCACTTCTGGAGCCCCCGCTATCTATTCAAAAGACTACATAAGTTGCGACCGCTCGTACGCCGGGGTGGAAAGCCCACCGAAATTCCCTACGACATAGACAACACTGGGTGATTAACGCTGCGGTCTTTTTGTTGAGCGACAGTACAAAATAGGTGTTGCCTACCTACTGTTCATTGTGACCGAGGTCGTGTTTAGATTCAATTAAAAAATGTAGGGTAACCAATAGGCCACGCGCCGGCTGTTAAACCGATTAACCCAGTTAACACAGGTCCCGCTCTTTTAGGTAGATAAAAACCTTGCGTTCCATATCATATACCTCACTACACACCGCGCGGTGACCTTTTTATCCATCGTGGCACAGGAAAACGGGGCTACTAGGCGATTCTATCAATCAAGAATGCCTTCCCGATCACTGTTTCGTTTCCGTCAGCCTTCTGTCACACACGCGGTAACGTCTTACGGCACAAAGTTACCGACGTCGAACGATTGATAGGTTGTCTGCGCGATCTGGATGTTGACGTGTGCGGGTGA";
adenine = 0;
cytosine = 0;
guanine = 0;
thymine = 0;
 
for nucleotide in dna:
	if(nucleotide == "A"):
		adenine = adenine + 1
	elif(nucleotide == "G"):
		guanine = guanine + 1
	elif(nucleotide == "C"):
		cytosine = cytosine + 1
	elif(nucleotide == "T"):
		thymine = thymine + 1

print adenine,cytosine,guanine,thymine;