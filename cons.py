from Bio import SeqIO
from collections import Counter

def generate_profile_and_consensus(fasta_file):
    sequences = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    num_sequences = len(sequences)
    seq_length = len(sequences[0])

    profile = {'A': [0] * seq_length, 'C': [0] * seq_length, 'G': [0] * seq_length, 'T': [0] * seq_length}

    for seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1
    
    consensus = ''
    for i in range(seq_length):
        column = {base: profile[base][i] for base in 'ACGT'}
        consensus += max(column, key=column.get)
    return consensus, profile

def save_result(consensus, profile, output_file):
    with open(output_file, 'w') as f:
        f.write(consensus + "\n")
        for base in 'ACGT':
            f.write(f"{base}: " + " ".join(map(str, profile[base])) + "\n")


def main():
    input_file = "input.txt" 
    output_file = "output.txt"  
    
    consensus, profile = generate_profile_and_consensus(input_file)
    save_result(consensus, profile, output_file)

if __name__ == "__main__":
    main()
