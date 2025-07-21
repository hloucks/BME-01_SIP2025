import pandas as pd

def parse_custom_vcf(filepath):
    metadata = {}
    variants = []
    sample_names = []

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("##"):
                # Parse metadata lines
                if '=' in line[2:]:
                    key, value = line[2:].split('=', 1)
                    metadata[key] = value
            elif line.startswith("#CHROM"):
                # Parse column headers (includes sample names)
                columns = line.lstrip("#").split("\t")
                fixed_cols = columns[:9]
                sample_names = columns[9:]
            else:
                # Parse variant rows
                parts = line.split("\t")
                variant_data = dict(zip(fixed_cols, parts[:9]))
                genotypes = parts[9:]
                variant_data.update(dict(zip(sample_names, genotypes)))
                variants.append(variant_data)

    # Create DataFrame
    df = pd.DataFrame(variants)

    # Optional: convert POS to integer
    df["POS"] = df["POS"].astype(int)

    return metadata, sample_names, df


vcf_file = "Example.vcf"
metadata, samples, vcf_df = parse_custom_vcf(vcf_file)

print(metadata)
print(samples)
print(vcf_df)