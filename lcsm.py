from Bio import SeqIO

def longest_common_substring(fasta_file):
    sequences = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    sequences.sort(key=len)
    shortest_seq = sequences[0]
    
    def is_common_substring(substring):
        return all(substring in seq for seq in sequences)
    
    for length in range(len(shortest_seq), 0, -1):
        for start in range(len(shortest_seq) - length + 1):
            candidate = shortest_seq[start:start + length]
            if is_common_substring(candidate):
                return candidate  
    
    return ""  

result = longest_common_substring("./input.txt")

with open("output.txt", "w") as file:
    file.write(result)
