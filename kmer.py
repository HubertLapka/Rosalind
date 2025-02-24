from Bio import SeqIO
from itertools import product

def generate_kmers(k):
    return ["".join(p) for p in product("ACGT", repeat=k)]

def kmer_composition(dna_sequence, k=4):
    kmer_dict = {kmer: 0 for kmer in generate_kmers(k)}
    for i in range(len(dna_sequence) - k + 1):
        kmer = dna_sequence[i:i+k]
        kmer_dict[kmer] += 1
    return [kmer_dict[k] for k in sorted(kmer_dict.keys())]

def main(input_file, output_file):
    with open(input_file, "r") as file:
        record = next(SeqIO.parse(file, "fasta"))
        dna_sequence = str(record.seq)
    
    composition = kmer_composition(dna_sequence)
    
    with open(output_file, "w") as out:
        out.write(" ".join(map(str, composition)) + "\n")

if __name__ == "__main__":
    input_file = "./input.txt"  
    output_file = "output.txt" 
    main(input_file, output_file)
