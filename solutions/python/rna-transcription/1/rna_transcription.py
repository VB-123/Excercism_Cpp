def to_rna(dna_strand):
    Guide = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna_strand = ""
    for char in dna_strand:
        rna_strand += Guide[char]
    return rna_strand
