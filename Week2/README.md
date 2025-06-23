## 6/23/25

For files fasta1.fa, fasta2.fa, and fasta3.fa

Each of these fasta files contain a repetitive sequence.

Please calculate the following:

1. Length of the sequence
2. Percent of the sequence that is A, T, C, or G (or N?)
3. The sequence and length of the repeat


For the fasta_challenge.fa
Sequence 0 is our reference and we have two sequences (1 and 2) which we want to compare to sequence 1. 
1. How many differences are there between the reference and sequence 1?
2. How many differences are there between the reference and sequence 2? 
3. Can you tell which sequences are more closely related? 


To run python code you will need to be in an environment containing python and any associated packages. I included a yml file that should allow you to create the environment with this command:
`conda env create -f SIP2025_week2.yml`
Then you can activate the environment by running
`conda activate SIP2025_week2`
To run your python script you can execute the following code on the command line
`python3 Week2_starting_template.py`