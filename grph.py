from Bio import SeqIO

def overlap_graph(fasta_file, k=3, output_file="output.txt"):
    sequences = {record.id: str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")}
    edges = []
    
    for s_id, s_seq in sequences.items():
        for t_id, t_seq in sequences.items():
            if s_id != t_id and s_seq[-k:] == t_seq[:k]:  
                edges.append(f"{s_id} {t_id}")
    
    with open(output_file, "w") as file:
        file.write("\n".join(edges))

overlap_graph("./input.txt")
