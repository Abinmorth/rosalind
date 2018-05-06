def rna_to_protein(file_in, file_out):
    codon_table = {
        "UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","UCA":"S","UCG":"S",
        "UAU":"Y","UAC":"Y","UAA":"\n","UAG":"\n","UGU":"C","UGC":"C","UGA":"\n","UGG":"W",
        "CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
        "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","CGU":"R","CGC":"R","CGA":"R","CGG":"R",
        "AUU":"I","AUC":"I","AUA":"I","AUG":"M","ACU":"T","ACC":"T","ACA":"T","ACG":"T",
        "AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S","AGA":"R","AGG":"R",
        "GUU":"V","GUC":"V","GUA":"V","GUG":"V","GCU":"A","GCC":"A","GCA":"A","GCG":"A",
        "GAU":"D","GAC":"D","GAA":"E","GAG":"E","GGU":"G","GGC":"G","GGA":"G","GGG":"G"
        }

    count = 0
    codon = ""
    for line in file_in:
        for char in line.replace("\n", ""):
            codon = codon + char
            count = (count + 1) % 3
            if count == 0:
                protein = codon_table[codon]
                file_out.write(protein)
                codon = ""
                if protein == "\n":
                    return

file_in = open('prot_in.txt', 'r')
file_out = open('prot_out.txt', 'w')
rna_to_protein(file_in, file_out)
print("DONE")
file_out.flush()
file_out.close()
