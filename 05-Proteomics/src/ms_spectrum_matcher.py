"""
In-silico Tryptic Digest and Theoretical Fragment Ion (b/y ions) Generator
with Spectrum Cosine Matching for Mass Spectrometry-based Proteomics.
"""

from typing import List, Tuple, Dict
import numpy as np

# Monoisotopic amino acid masses (Da)
AA_MASSES = {
    'A': 71.03711,  'R': 156.10111, 'N': 114.04293, 'D': 115.02694,
    'C': 103.00919, 'E': 129.04259, 'Q': 128.05858, 'G': 57.02146,
    'H': 137.05891, 'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
    'M': 131.04049, 'F': 147.06841, 'P': 97.05276,  'S': 87.03203,
    'T': 101.04768, 'W': 186.07931, 'Y': 163.06333, 'V': 99.06841
}
H2O_MASS = 18.010565
PROTON_MASS = 1.007276


def tryptic_digest(protein_sequence: str, max_missed: int = 1, min_len: int = 7, max_len: int = 30) -> List[str]:
    """Cleaves after K or R unless followed by P (standard trypsin rule)."""
    seq = protein_sequence.upper()
    cleavage_indices = [0]
    for i in range(len(seq) - 1):
        if seq[i] in ('K', 'R') and seq[i + 1] != 'P':
            cleavage_indices.append(i + 1)
    cleavage_indices.append(len(seq))
    
    peptides = []
    num_sites = len(cleavage_indices) - 1
    for missed in range(max_missed + 1):
        for i in range(num_sites - missed):
            start = cleavage_indices[i]
            end = cleavage_indices[i + 1 + missed]
            pep = seq[start:end]
            if min_len <= len(pep) <= max_len:
                peptides.append(pep)
    return sorted(list(set(peptides)))


def generate_theoretical_ions(peptide: str, charge: int = 1) -> Dict[str, List[float]]:
    """Generates singly/doubly charged b- and y-ion m/z values."""
    n = len(peptide)
    b_ions = []
    y_ions = []
    
    # Prefix cumulative mass for b ions
    cum_b = 0.0
    for i in range(n - 1):
        cum_b += AA_MASSES.get(peptide[i], 0.0)
        mz = (cum_b + PROTON_MASS * charge) / charge
        b_ions.append(round(mz, 4))
        
    # Suffix cumulative mass for y ions
    cum_y = 0.0
    for i in range(n - 1, 0, -1):
        cum_y += AA_MASSES.get(peptide[i], 0.0)
        mz = (cum_y + H2O_MASS + PROTON_MASS * charge) / charge
        y_ions.append(round(mz, 4))
        
    return {"b_ions": b_ions, "y_ions": y_ions[::-1]}


def spectrum_cosine_similarity(
    experimental_peaks: List[Tuple[float, float]],
    theoretical_mzs: List[float],
    tolerance_da: float = 0.05
) -> float:
    """Computes cosine similarity between observed experimental peaks and theoretical m/z."""
    matched_exp = []
    matched_theo = []
    
    for tmz in theoretical_mzs:
        # find closest peak
        best_diff = tolerance_da
        best_intensity = 0.0
        for emz, intensity in experimental_peaks:
            diff = abs(emz - tmz)
            if diff < best_diff:
                best_diff = diff
                best_intensity = intensity
        matched_exp.append(best_intensity)
        matched_theo.append(1.0)  # unit weight theoretical
        
    v1 = np.array(matched_exp)
    v2 = np.array(matched_theo)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (norm1 * norm2))


if __name__ == "__main__":
    prot = "MKWVTFISLLLLFSSAYSRGVFRRDTHKSEIAHRFKDLGEEHFKGLVLIAFSQYLQQCPFDEHVKLVNELTEFAK"
    peps = tryptic_digest(prot, max_missed=1)
    print(f"Digest generated {len(peps)} peptides. First 3: {peps[:3]}")
    ions = generate_theoretical_ions(peps[0])
    print(f"Peptide {peps[0]} b-ions: {ions['b_ions'][:3]}, y-ions: {ions['y_ions'][:3]}")
