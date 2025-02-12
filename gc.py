from Bio import SeqIO
import math

seq_name = ''
gc_content = 0
input_file = "./input.txt"
fasta_sequences = SeqIO.parse(open(input_file),'fasta')
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    seq_len = len(sequence)
    gc_count = 0
    for char in sequence:
        if char == "G" or char == "C":
            gc_count += 1
    if (gc_count/seq_len)*100 > gc_content:
        gc_content = (gc_count/seq_len)*100
        seq_name = name
print(seq_name, gc_content)
