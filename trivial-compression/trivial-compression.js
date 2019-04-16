let log = console.log;
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

        this.bit_string = "";
        
        for (let nucleotide of gene.toUpperCase()) {
            log(this.bit_string)
            this.bit_string <<=2
            log(this.bit_string)
            log("----")
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
        console.log("---", this.bit_string, "---")
        
    }

    _decompress() {
        console.log(this.bit_string)
        let gene = "";

        let rango = range(0, this.bit_string.length)
        
        for (let i of rango) {
            console.log("original ", Number(i).toString(2))
            console.log("Before ", Number(i >>> 0  & 0b11))
            //let bits = this.bit_string
            let bits = (i >>> 0).toString(2)
            console.log("after ", bits)
            if (bits == Number("0b00")) {

                gene += "A"
            } else if (bits == Number("0b01")) {
                gene += "C"
            } else if (bits == Number("0b10")) {
                gene += "G"
            } else if (bits == 0b11) {
                gene += "T"
            } else {
                console.log("Invalid bits")
            }
        }
    
        return gene
    }
}

let original = "TAGGGGAAATTAAAATGGGGAAATTTTAGAGGGAGAGGATTT".repeat(1);
let compressed = new CompressedGene(original);
console.log(compressed)
let decompressed = compressed._decompress();
//console.log(decompressed)
//console.log(compressed === decompressed)