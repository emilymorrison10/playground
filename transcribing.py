with open('rosalind_rna.txt', 'r') as file:
    dnaseq = file.read().strip()

rnaseq = dnaseq.maketrans("T", "U")

print(dnaseq.translate(rnaseq))




