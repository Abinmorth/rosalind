def read_fasta(file_in):
    file = open(file_in, "r")
    fasta_strings = {}
    key = ''
    value = ''
    while True:
        line = file.readline().strip('\n')
        if line.startswith('>'):
            key = line
            value = ''
        else:
            value += line
        fasta_strings[key] = value
        if not line: break  # EOF
    return fasta_strings
