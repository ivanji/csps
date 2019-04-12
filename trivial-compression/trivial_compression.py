class CompressedGene:
    
    def __init__(self, gene:str) -> None: 
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        # _ indicates a 'private' method
        # Tip: using double leading underscores within a class will make Python 'name mangle' 
        # the implementation name. Meaning it'd add a salt to avoid it from being easily discoverable 
        # by other classes.

        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<=2 # shif left two bits
            if nucleotide == "A": # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # change last two bits to 00
                self.bit_string |= 0b01
            elif nucleotide == "G": # change last two bits to 00
                self.bit_string |= 0b10
            elif nucleotide == "T": # change last two bits to 00
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotid: {}".format(nucleotide))
    
    def _decompress(self) -> str:
        gene: str = ""

        for i in range(0, self.bit_string.bit_length() -1, 2): #-1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11 # get just 2 relevant bits
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits: {}".format(bits))

        return gene[::-11] # reverses string by slicing backwards
    
    def __str__(self) -> str:
        return self._decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGGAAATTAAAATGGGGAAATTTTAGAGGGAGAGGATTT" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed)))
    print(compressed)
    decompressed: CompressedGene = compressed._decompress()
    print(decompressed)
    print("original and decompressed are the same: {}".format(original == decompressed))