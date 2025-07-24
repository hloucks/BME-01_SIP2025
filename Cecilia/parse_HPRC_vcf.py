# import packages
import pandas as pd 


vcf_file="OR4C12_vars.vcf"

# Store header and sample names
with open(vcf_file, 'r') as f:
    for line in f:
        if line.startswith('#CHROM'):
            header = line.strip().split('\t')
            samples = header[10:]  # everything after FORMAT
            break

# Prepare column names for haplotypes
haplotype_columns = []
for sample in samples:
    haplotype_columns.append(f"{sample}_hap1")
    haplotype_columns.append(f"{sample}_hap2")

# Parse the data rows
variant_rows = []
with open(vcf_file, 'r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        chrom, pos, vid, ref, alt, qual, flt, info, fmt, hg38 = fields[:10]
        sample_fields = fields[10:]

        # Create a dict for this variant
        row_data = {
            "CHROM": chrom,
            "POS": int(pos),
            "ID": vid,
            "REF": ref,
            "ALT": alt,
            "QUAL": qual,
            "FILTER": flt,
            "INFO": info,
            "GRCh38": hg38,
        }

        # Add haplotypes from each sample
        for sample, value in zip(samples, sample_fields):
            gt = value.split(":")[0]  # get GT (may be GT:DP:...)
            if "|" in gt:
                hap1, hap2 = gt.split("|")
            elif "/" in gt:
                hap1, hap2 = gt.split("/")
            else:
                hap1 = hap2 = None
            row_data[f"{sample}#1"] = hap1
            row_data[f"{sample}#2"] = hap2

        variant_rows.append(row_data)

vars = pd.DataFrame(variant_rows)

# Reorder: metadata columns first, then haplotypes
meta_cols = ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "GRCh38"]
hap_cols = [col for col in vars.columns if col not in meta_cols]


# data objects created are below:

# this is the dataframe with all information about variants and samples
full_vars = vars[meta_cols + hap_cols]
print(full_vars)

# hap_cols is a list of all of the samples in the vcf 
hap_cols += ['GRCh38']
print(hap_cols)















