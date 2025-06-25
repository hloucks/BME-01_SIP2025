#file name goes here 
filepath=("fasta2.fa")


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
print(fasta)

sequence = fasta["seq2"]
print(sequence)

print(len(sequence))

# use a for loop to count each element 
# python is zero indexed - first element in a list is going to have an index of 0 


# next step is to count each of the nucleotides 


# after that - think about how you can deduce the size of the repeat in your sequence