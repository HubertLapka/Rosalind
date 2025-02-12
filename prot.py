input_file = "./input.txt"
with open(input_file, "r") as file:
    rna = file.read()

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
