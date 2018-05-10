dna = "AAAGAGGCTTAAGGCTTAGAGGCTTAGTAGCAGGCTTAAGGCTTATTTAGGCTTACTGAAAGGCTTAATCGGATCCTCACGAGGCTTAGAGGCTTAAGGCTTATTAGGCTTACTAGGCTTAGCCGCAAGGCTTATAGGCTTAGAGGCTTAGAGGCTTAGAGGCTTAAGGCTTAGAGGCTTATGAGGCTTATTTAGGCTTACAAGGCTTAAGACCGAGGCTTAAGGCTTAAAGAAGGCTTAAGGCTTAAAGGCTTACAGGCTTAACTGTAAGGCTTAGCAGGCTTACAGGCTTAAAGGCTTAAGGCTTAAACATGTACAGGCTTATCCCAGGCTTATAGGCTTATGCACAAGGCTTAGAGGCTTAGAAGCAGGCTTATAGGCTTAAGCCGAGGCTTAAGGCTTATTAGTACAGGCTTAACAGGCTTACAGGCTTATCCACCAGGCTTAAGGCTTACAACGGAGGCTTATTAAGGCTTAAGGCTTAGAAGGCTTAAGGCTTAAAAGCCGTGACTAGGCTTAAGGCTTAAGGCTTAGAGGCTTAAGGCTTAGCGAACTATAGGCTTAAGAAGGCTTACGAGGCTTAATGAGGCTTAAAGGCTTATCTTGAGGAAAGGCTTAAGGCTTAAGGCTTAAAGGCTTAAGGCTTAAATAGGCTTAGCAGGCTTAGCGGTACAAAACCCAAGGCTTAAGGCTTAAGGCTTAAGGCTTAAGAGGCTTATCCATTGACTAGGCTTAAGGCTTAAGAAGGCTTAAGGCTTACCGCAGGCTTACACGGAGGCTTAAGGCTTACCTAAGATTAAGGCTTAAGGCTTAAGAAGGCTTACTGTAGGCTTAGAAGCAAGGCTTAACAAGGCTTAAGGCTTA"
motif = "AGGCTTAAG"
positionlist = []
for i in range(0, len(dna)):
    substr = dna[i:i+len(motif)]
    if(substr == motif):
        positionlist.append(i+1)
print(" ".join(map(str,positionlist)))