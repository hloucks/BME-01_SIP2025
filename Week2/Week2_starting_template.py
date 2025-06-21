#file name goes here 
filepath=("fasta1.fa")


def parse_fasta_manual(filepath):
    #fasta sequences will exist as a dictionary 
    sequences = {}
    current_header = None
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            if line.startswith('>'):
                current_header = line[1:]  # Remove '>'
                sequences[current_header] = []
            elif current_header:
                sequences[current_header].append(line)
    return {header: "".join(seq_parts) for header, seq_parts in sequences.items()}

# fasta is the dictionary containing all of the information from your input fasta file 
fasta = parse_fasta_manual(filepath)

