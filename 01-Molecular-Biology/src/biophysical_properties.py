"""
Biophysical properties calculator for biological sequences.
Implements GC content, Kyte-Doolittle hydropathy profile, and
simplified nearest-neighbor thermodynamic melting temperature estimates.
"""

from typing import List, Tuple, Dict

# Kyte & Doolittle hydropathy scale (1982)
KYTE_DOOLITTLE = {
    'A': 1.8,  'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8,  'K': -3.9, 'M': 1.9,  'F': 2.8,  'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

# Standard Genetic Code
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}


def calculate_gc_content(dna_sequence: str) -> float:
    """Calculate GC ratio of a DNA sequence."""
    seq = dna_sequence.upper()
    if not seq:
        return 0.0
    gc_count = seq.count('G') + seq.count('C')
    return float(gc_count) / len(seq)


def calculate_melting_temperature_basic(dna_sequence: str) -> float:
    """
    Approximate Tm in degrees Celsius.
    Uses Wallace rule for < 14 bp, and salt-adjusted formula for longer.
    """
    seq = dna_sequence.upper()
    length = len(seq)
    if length < 14:
        return (seq.count('A') + seq.count('T')) * 2 + (seq.count('G') + seq.count('C')) * 4
    gc = calculate_gc_content(seq) * 100.0
    # Basic empirical Marmur-Doty formula (50 mM Na+)
    return 64.9 + 41 * (gc - 16.4) / length


def hydropathy_profile(protein_seq: str, window_size: int = 9) -> List[Tuple[int, float]]:
    """
    Compute sliding-window Kyte-Doolittle hydropathy profile.
    Values > 1.6 in a window of 19-21 typically indicate transmembrane domains.
    """
    seq = protein_seq.upper()
    profile: List[Tuple[int, float]] = []
    half_window = window_size // 2

    for i in range(half_window, len(seq) - half_window):
        window = seq[i - half_window : i + half_window + 1]
        score = sum(KYTE_DOOLITTLE.get(aa, 0.0) for aa in window) / float(window_size)
        profile.append((i, round(score, 3)))
    return profile


def translate_dna(dna_sequence: str) -> str:
    """Translate DNA to amino acid sequence."""
    seq = dna_sequence.upper()
    protein = []
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        amino_acid = CODON_TABLE.get(codon, 'X')
        if amino_acid == '_':
            break  # stop codon
        protein.append(amino_acid)
    return "".join(protein)


if __name__ == "__main__":
    test_dna = "ATGCGTCGTAGCTAGCTAGCTAGCGCTAGCTAGCTAAGTCGATCG"
    print(f"DNA Length: {len(test_dna)} bp")
    print(f"GC Content: {calculate_gc_content(test_dna):.3f}")
    print(f"Estimated Tm: {calculate_melting_temperature_basic(test_dna):.1f} °C")
    test_prot = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF"
    profile = hydropathy_profile(test_prot, window_size=7)
    print(f"Hydropathy profile points: {len(profile)}, first 3: {profile[:3]}")
