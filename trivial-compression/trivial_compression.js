function range(start, stop, step) {
    if (typeof stop == 'undefined') {
        // one param defined
        stop = start;
        start = 0;
    }

    if (typeof step == 'undefined') {
        step = 1;
    }

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
        return [];
    }

    var result = [];
    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
        result.push(i);
    }

    return result;
};

class CompressedGene {
    constructor(gene) {
        this._compress(gene);
        
    }

    _compress(gene) {

        this.bit_string = 1;

        gene = gene.toUpperCase();

        for (let nucleotide of gene) {
            this.bit_string <<=2
            if (nucleotide === "A") {
                this.bit_string |= 0b00
            } else if (nucleotide === "C") {
                this.bit_string |= 0b01
            } else if (nucleotide === "G") {
                this.bit_string |= 0b10
            } else if (nucleotide === "T") {
                this.bit_string |= 0b11
            } else {
                console.log("Invalid Nucleotoid")
            }
        }
        console.log("Final Bit String ", this.bit_string.length)
    }

    _decompress() {
        //encoded(encodedGene >>> 0).toString(2)
        let gene = "";
        console.log(this.bit_string.length)
        let rango = range(0, this.bit_string.toString().length)
        
        for (let i of rango) {
            
            let bits = this.bit_string >> i & 0b00

            if (bits == Number("0b00")) {
                gene += "A"
            } else if (bits ===Number("0b01")) {
                gene += "C"
            } else if (bits == Number("0b10")) {
                gene += "G"
            } else if (bits == Number("0b11")) {
                gene += "T"
            } else {
                console.log("Invalid bits")
            }
        }

        return gene
    }
}

let original = "TAGGGGAAATTAAAATGGGGAAATTTTAGAGGGAGAGGATTT".repeat(100);
let compressed = new CompressedGene(original)
console.log(compressed)
let decompressed = compressed._decompress();
console.log(decompressed)