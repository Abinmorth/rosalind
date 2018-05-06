file_in = open('gc_in.txt', 'r')
file_out = open('gc_out.txt', 'w')
max_percentage = 0
max_identifier = ""
max_gc_count = 0
max_total = 0
current_percentage = 0
for index, line in enumerate(file_in):
    if line.startswith(">Rosalind_"):
        if current_percentage > max_percentage:
            max_percentage = current_percentage
            max_identifier = current_identifier
        current_identifier = line[1::]
        gc_count = 0
        total = 0
    else:
        gc_count = gc_count + line.count("G") + line.count("C")
        total = total + line.count("A") + line.count("T") + line.count("G") + line.count("C")
        current_percentage = (float(gc_count) / total) * 100
if current_percentage > max_percentage:
    max_percentage = current_percentage
    max_identifier = current_identifier
file_out.write(max_identifier)
file_out.write(str(round(max_percentage,6)) + "\n")
file_out.close()
