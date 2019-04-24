from enum import IntEnum
from typing import Tuple, List

""" A Nucleotide is represented by one of the letters A, C, G and T
A Codon is composed of three nucleotides, and a gene is composed of
multiple codons """

# using IntEnum instead of just Enum, as it gives us comparison operators
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# Codons are defined as types
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "TAGGGGAAATTAAAATGGGGAAATTTTAGAGGGAGAGGATTT"

# We need to convert the string into a gene
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        # This function is for illustrative purposes only. As we could make use
        # of __contains__() method within an 'in' operato
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon) # add codon to gene
    return gene

my_gene: Gene = string_to_gene(gene_str)

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
ttt: Codon = (Nucleotide.T, Nucleotide.A, Nucleotide.G)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))
print(linear_contains(my_gene, ttt))

