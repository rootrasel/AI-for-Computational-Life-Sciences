"""
Metabolomics Feature Processing:
Implements Probabilistic Quotient Normalization (PQN),
missing value imputation, and adduct detection.
"""

import numpy as np
from typing import Tuple, List, Dict

COMMON_ADDUCTS_POS = {
    '[M+H]+': 1.007276,
    '[M+Na]+': 22.989218,
    '[M+K]+': 38.963158,
    '[M+NH4]+': 18.033823
}


def probabilistic_quotient_normalization(feature_matrix: np.ndarray) -> np.ndarray:
    """
    feature_matrix: shape (N_samples, M_metabolites)
    PQN corrects for dilution variance (e.g. urine/plasma concentrations).
    """
    # Reference sample: median of all samples for each metabolite
    reference = np.median(feature_matrix, axis=0)
    reference[reference == 0] = 1e-6
    
    # Quotient of each sample relative to reference
    quotients = feature_matrix / reference[np.newaxis, :]
    
    # Dilution factor is median quotient per sample
    dilution_factors = np.median(quotients, axis=1, keepdims=True)
    dilution_factors[dilution_factors == 0] = 1.0
    
    return feature_matrix / dilution_factors


def detect_adduct_pairs(
    mz_list: List[float],
    ppm_tol: float = 10.0
) -> List[Tuple[int, int, str]]:
    """
    Identifies candidate [M+H]+ and [M+Na]+ pairs.
    Delta mass = 22.989218 - 1.007276 = 21.981942 Da.
    """
    delta_na_h = COMMON_ADDUCTS_POS['[M+Na]+'] - COMMON_ADDUCTS_POS['[M+H]+']
    pairs = []
    
    for i, mz1 in enumerate(mz_list):
        for j, mz2 in enumerate(mz_list):
            if i >= j:
                continue
            diff = abs(mz2 - mz1)
            target_diff = delta_na_h
            ppm_error = abs(diff - target_diff) / mz1 * 1e6
            if ppm_error <= ppm_tol:
                pairs.append((i, j, f"[M+Na]+ vs [M+H]+ (ppm={ppm_error:.1f})"))
    return pairs


if __name__ == "__main__":
    np.random.seed(42)
    raw_metabolites = np.random.exponential(scale=1000.0, size=(10, 50))
    # inject artificial dilution
    raw_metabolites[0] *= 4.0
    pqn_norm = probabilistic_quotient_normalization(raw_metabolites)
    print("Raw sample 0 median:", np.median(raw_metabolites[0]))
    print("PQN sample 0 median:", np.median(pqn_norm[0]))
