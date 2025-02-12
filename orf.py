from Bio import SeqIO
from Bio.Seq import Seq

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def translate_dna_to_protein(dna):
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP', 'TGA': 'STOP', 'TGC': 'C', 'TGT': 'C',
        'TGA': 'STOP', 'TGG': 'W'
    }
    
    protein = []
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if codon_table[codon] == 'STOP':
            break
        protein.append(codon_table[codon])
    return ''.join(protein)

def find_orfs(dna):
    orfs = set()  
    for frame in range(3):
        for i in range(frame, len(dna) - 2, 3):
            if dna[i:i+3] == "ATG":  
                for j in range(i + 3, len(dna) - 2, 3):
                    if dna[j:j+3] in {"TAA", "TAG", "TGA"}:  
                        orf = dna[i:j+3]
                        orfs.add(translate_dna_to_protein(orf))  
                        break

    rev_complement_dna = reverse_complement(dna)
    for frame in range(3):
        for i in range(frame, len(rev_complement_dna) - 2, 3):
            if rev_complement_dna[i:i+3] == "ATG":  
                for j in range(i + 3, len(rev_complement_dna) - 2, 3):
                    if rev_complement_dna[j:j+3] in {"TAA", "TAG", "TGA"}: 
                        orf = rev_complement_dna[i:j+3]
                        orfs.add(translate_dna_to_protein(orf))  
                        break
    return orfs

def process_dna_sequence(dna_sequence):
    orfs = find_orfs(dna_sequence)
    return list(orfs)

def write_results_to_file(proteins, filename):
    with open(filename, 'w') as file:
        for protein in proteins:
            file.write(protein + "\n")

input_file = "./input.txt"  
with open(input_file, "r") as file:
    record = SeqIO.read(file, "fasta")
    dna_sequence = str(record.seq)

result = process_dna_sequence(dna_sequence)
write_results_to_file(result, 'output.txt')
