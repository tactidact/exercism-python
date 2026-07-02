def to_rna(dna_strand):
    dna_rna_mapping = {"G": "C", "C": "G", "T": "A", "A": "U"}

    if not dna_strand:
        return ""

    rna_strand = ""

    for nucleotide in dna_strand:
        rna_strand += dna_rna_mapping[nucleotide]

    return rna_strand
