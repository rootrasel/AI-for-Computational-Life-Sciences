"""
Cheminformatics Foundations:
Fingerprint generation, Tanimoto similarity metrics,
and Bemis-Murcko scaffold extraction concepts.
"""

from typing import List, Set, Tuple
import numpy as np


def tanimoto_similarity_bits(bit_vec_a: np.ndarray, bit_vec_b: np.ndarray) -> float:
    """Computes exact Tanimoto similarity between two binary bit vectors."""
    intersection = np.sum(bit_vec_a & bit_vec_b)
    union = np.sum(bit_vec_a | bit_vec_b)
    if union == 0:
        return 1.0
    return float(intersection / union)


def pairwise_tanimoto_matrix(fingerprints: np.ndarray) -> np.ndarray:
    """
    Vectorized pairwise Tanimoto similarity matrix for N molecules.
    fingerprints: shape (N, n_bits) uint8 or bool array
    """
    n = fingerprints.shape[0]
    # Dot product computes intersection
    intersection = np.dot(fingerprints.astype(float), fingerprints.astype(float).T)
    # Sum of active bits per molecule
    active_bits = np.sum(fingerprints, axis=1, keepdims=True)
    # Union = |A| + |B| - |A and B|
    union = active_bits + active_bits.T - intersection
    union[union == 0] = 1.0
    return intersection / union


def lipinski_rule_of_five_check(
    molecular_weight: float,
    log_p: float,
    h_bond_donors: int,
    h_bond_acceptors: int
) -> Tuple[bool, int]:
    """
    Lipinski's Rule of 5:
    - MW <= 500 Da
    - LogP <= 5
    - H-bond donors <= 5
    - H-bond acceptors <= 10
    Returns: (passes_rule, num_violations)
    """
    violations = 0
    if molecular_weight > 500: violations += 1
    if log_p > 5.0: violations += 1
    if h_bond_donors > 5: violations += 1
    if h_bond_acceptors > 10: violations += 1
    return violations <= 1, violations


if __name__ == "__main__":
    np.random.seed(42)
    # 5 molecules with 1024-bit fingerprints
    fake_fps = np.random.binomial(1, 0.05, size=(5, 1024)).astype(bool)
    sim = tanimoto_similarity_bits(fake_fps[0], fake_fps[1])
    print(f"Tanimoto similarity between mol 0 and 1: {sim:.4f}")
    t_mat = pairwise_tanimoto_matrix(fake_fps)
    print("5x5 Pairwise Tanimoto matrix:\n", np.round(t_mat, 3))
    
    # Check Aspirin approx
    passes, viol = lipinski_rule_of_five_check(180.15, 1.19, 1, 3)
    print(f"Aspirin Lipinski pass: {passes} (violations: {viol})")
