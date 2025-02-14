from itertools import permutations
from Bio import SeqIO

def transition_transversion_ratio(s1, s2):
    transitions = 0
    transversions = 0
    
    transition_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    transversion_pairs = {('A', 'C'), ('A', 'T'), ('G', 'C'), ('G', 'T'), ('C', 'A'), ('C', 'G'), ('T', 'A'), ('T', 'G')}
    
    for a, b in zip(s1, s2):
        if (a, b) in transition_pairs:
            transitions += 1
        elif (a, b) in transversion_pairs:
            transversions += 1
    
    return transitions / transversions if transversions != 0 else float('inf')

def read_fasta(filename):
    sequences = []
    for record in SeqIO.parse(filename, "fasta"):
        sequences.append(str(record.seq))
    return sequences[0], sequences[1]

s1, s2 = read_fasta("./input.txt")
print(transition_transversion_ratio(s1, s2))
