# pull DNA sequence directly from file
with open('rosalind_revc.txt', 'r') as file:
    dnaseq = file.read().strip()

# reverse sequence
rev_dnaseq = dnaseq[::-1]

# create table to sub out complementary nucleotides
comp_table = str.maketrans("ATGC", "TACG")

# translate reversed DNA sequence to get complementary strand
comp_strand = rev_dnaseq.translate(comp_table)

# print complementary strand
print(comp_strand)
