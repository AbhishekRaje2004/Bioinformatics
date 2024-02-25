amino_acids = [
    "A", "R", "N", "D", "C",
    "Q", "E", "G", "H", "I",
    "L", "K", "M", "F", "P",
    "S", "T", "W", "Y", "V"
]

protein="MREYKVVVLGSGGVGKSALTVQFVTGTFIEKYDPTIEDFYRKEIEVDSSPSVLEILDTAGTEQFASMRDLYIKNGQGFILVYSLVNQQSFQDIKPMRDQIIRVKRYEKVPVILVGNKVDLESEREVSSSEGRALAEEWGCPFMETSAKSKTMVDELFAEIVRQMNYAAQPDKDDPCCSACNIQ"
# Initialize a dictionary to store the counts for each amino acid
amino_acid_counts = {aa: 0 for aa in amino_acids}

# Count the occurrences of each amino acid in the protein sequence
for amino_acid in amino_acids:
    count = protein.count(amino_acid)
    amino_acid_counts[amino_acid] = count

# Print the counts for each amino acid
for amino_acid, count in amino_acid_counts.items():
    print(f"{amino_acid}: {count}")
print(f" Total Amino Acid in protein sequence :{len(protein)}")