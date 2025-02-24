from Bio import SeqIO

def reverse_complement(seq):
    complement = str.maketrans("ACGT", "TGCA")
    return seq.translate(complement)[::-1]

def find_reverse_palindromes(dna_sequence, min_len=4, max_len=12):
    palindromes = []
    for length in range(min_len, max_len + 1):
        for i in range(len(dna_sequence) - length + 1):
            subseq = dna_sequence[i:i+length]
            if subseq == reverse_complement(subseq):
                palindromes.append((i + 1, length))
    return palindromes

def main(input_file, output_file):
    with open(input_file, "r") as file:
        record = next(SeqIO.parse(file, "fasta"))
        dna_sequence = str(record.seq)
    
    palindromes = find_reverse_palindromes(dna_sequence)
    
    with open(output_file, "w") as out:
        for pos, length in palindromes:
            out.write(f"{pos} {length}\n")

if __name__ == "__main__":
    input_file = "./input.txt" 
    output_file = "output.txt"  
    main(input_file, output_file)
