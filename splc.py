from Bio import SeqIO

input_file = "./input.txt"
dna = ""
introns = []
fasta_sequences = SeqIO.parse(open(input_file),'fasta')
idx = 0
for fasta in fasta_sequences:
    if idx == 0:
        dna = str(fasta.seq)
    else:
        introns.append(str(fasta.seq))
    idx += 1

for intron in introns:
    dna = dna.replace(intron,"")
    
rna = dna.replace("T", "U")

sliced_rna = [rna[i:i+3] for i in range(0, len(rna), 3)]
protein_string = ''
proteins = {
    'M': ['AUG'],
    'W': ['UGG'],
    'H': ['CAU', 'CAC'], 
    'N': ['AAU', 'AAC'],
    'Y': ['UAU', 'UAC'],
    'D': ['GAU', 'GAC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'F': ['UUU', 'UUC'],
    'C': ['UGU', 'UGC'],
    'K': ['AAA', 'AAG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACC', 'ACU', 'ACA', 'ACG'],            
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],            
    'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],   
    'L': ['CUU', 'CUC', 'CUA', 'UUA', 'UUG', 'CUG'],            
}
for aminoacid in sliced_rna:
    if len(aminoacid) == 3:
        for protein_id, codons in proteins.items():
            if aminoacid in codons:
                protein_string += protein_id
                
with open("output.txt", "w") as file:
    file.write(protein_string)
