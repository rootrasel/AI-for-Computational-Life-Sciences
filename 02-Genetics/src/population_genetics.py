"""
Population genetics algorithms:
Hardy-Weinberg equilibrium testing, Pairwise Linkage Disequilibrium (r^2, D'),
and Polygenic Risk Score (PRS) calculator.
"""

import math
from typing import Tuple, List, Dict
import numpy as np


def hardy_weinberg_chi_square(n_aa: int, n_ab: int, n_bb: int) -> Tuple[float, float, bool]:
    """
    Perform Chi-square test for Hardy-Weinberg Equilibrium.
    Returns: (chi_square_stat, p_value_approx, is_in_equilibrium_at_0.05)
    """
    total = n_aa + n_ab + n_bb
    if total == 0:
        return 0.0, 1.0, True
    
    p = (2 * n_aa + n_ab) / (2.0 * total)
    q = 1.0 - p
    
    exp_aa = (p ** 2) * total
    exp_ab = (2 * p * q) * total
    exp_bb = (q ** 2) * total
    
    chi2 = 0.0
    for obs, exp in [(n_aa, exp_aa), (n_ab, exp_ab), (n_bb, exp_bb)]:
        if exp > 0:
            chi2 += ((obs - exp) ** 2) / exp
            
    # For df=1, critical value at alpha=0.05 is 3.841
    is_eq = chi2 < 3.841
    # Simple normal-based p-value approximation for 1 d.f.
    p_approx = math.erfc(math.sqrt(chi2 / 2.0))
    return chi2, p_approx, is_eq


def calculate_linkage_disequilibrium(
    haplotype_counts: Dict[str, int]
) -> Tuple[float, float, float]:
    """
    Given counts of haplotypes 'AB', 'Ab', 'aB', 'ab',
    calculates D, D_prime, and r_squared.
    """
    total = sum(haplotype_counts.values())
    if total == 0:
        return 0.0, 0.0, 0.0
    
    p_AB = haplotype_counts.get('AB', 0) / total
    p_Ab = haplotype_counts.get('Ab', 0) / total
    p_aB = haplotype_counts.get('aB', 0) / total
    p_ab = haplotype_counts.get('ab', 0) / total
    
    p_A = p_AB + p_Ab
    p_B = p_AB + p_aB
    p_a = 1.0 - p_A
    p_b = 1.0 - p_B
    
    D = p_AB - (p_A * p_B)
    
    if D >= 0:
        d_max = min(p_A * p_b, p_a * p_B)
    else:
        d_max = max(-p_A * p_B, -p_a * p_b)
        
    d_prime = (D / d_max) if abs(d_max) > 1e-12 else 0.0
    
    denom = p_A * p_a * p_B * p_b
    r_squared = (D ** 2 / denom) if denom > 1e-12 else 0.0
    
    return D, d_prime, r_squared


def compute_polygenic_risk_score(
    genotypes: np.ndarray,
    effect_sizes: np.ndarray
) -> np.ndarray:
    """
    genotypes: shape (N_samples, M_snps) with dosage {0, 1, 2}
    effect_sizes: shape (M_snps,) beta coefficients from GWAS summary stats
    Returns: vector of PRS for each sample, normalized to standard normal N(0,1).
    """
    raw_prs = np.dot(genotypes, effect_sizes)
    mean = np.mean(raw_prs)
    std = np.std(raw_prs)
    if std < 1e-12:
        return raw_prs - mean
    return (raw_prs - mean) / std


if __name__ == "__main__":
    chi2, p_val, eq = hardy_weinberg_chi_square(60, 30, 10)
    print(f"HWE Test: chi2={chi2:.3f}, p={p_val:.4f}, in equilibrium={eq}")
    
    haps = {'AB': 40, 'Ab': 10, 'aB': 10, 'ab': 40}
    d, d_prime, r2 = calculate_linkage_disequilibrium(haps)
    print(f"LD: D={d:.4f}, D'={d_prime:.4f}, r2={r2:.4f}")
