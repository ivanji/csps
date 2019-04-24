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

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while low <= high:      
        mid: int = (low + high) //2
    
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid -1
        else:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
tag: Codon = (Nucleotide.T, Nucleotide.A, Nucleotide.G)
my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
print(binary_contains(my_sorted_gene, tag))

""" To build a more performant binary search we can make use of 
Python's standard library's bisect module """