file_in = open('rosalind_ini5.txt', 'r')
file_out = open('INI5_out.txt', 'w')
index = 0
for line in file_in:
    index = index + 1
    if index % 2 == 0:
        file_out.write(line)
file_out.close()
