"""
RNA-Seq Count Normalization and Differential Expression Framework:
Calculates TPM, DESeq2 Median of Ratios size factors,
log2 Fold Changes, and Benjamini-Hochberg FDR adjustments.
"""

import numpy as np
from typing import Dict, Tuple, List


def calculate_tpm(counts: np.ndarray, lengths_bp: np.ndarray) -> np.ndarray:
    """
    counts: (N_genes, M_samples)
    lengths_bp: (N_genes,) transcript lengths in base pairs
    Returns: TPM matrix of shape (N_genes, M_samples)
    """
    lengths_kb = lengths_bp[:, np.newaxis] / 1000.0
    rpk = counts / lengths_kb
    per_sample_sum = np.sum(rpk, axis=0, keepdims=True)
    scaling_factor = per_sample_sum / 1e6
    return rpk / scaling_factor


def median_of_ratios_size_factors(counts: np.ndarray) -> np.ndarray:
    """
    DESeq2 Median of Ratios method:
    counts: shape (N_genes, M_samples)
    """
    # Exclude genes with 0 count in any sample for the geometric mean
    log_counts = np.log(counts.astype(np.float64) + 1e-12)
    geom_means = np.exp(np.mean(log_counts, axis=1, keepdims=True))
    
    # Ratios per gene per sample
    valid_genes = (geom_means[:, 0] > 1e-6)
    ratios = counts[valid_genes, :] / geom_means[valid_genes, :]
    size_factors = np.median(ratios, axis=0)
    return size_factors


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    """Calculate Benjamini-Hochberg False Discovery Rate (FDR) / q-values."""
    n = len(p_values)
    sorted_indices = np.argsort(p_values)
    sorted_p = p_values[sorted_indices]
    
    q_values = np.zeros(n)
    min_q = 1.0
    for i in range(n - 1, -1, -1):
        rank = i + 1
        q = (sorted_p[i] * n) / rank
        min_q = min(min_q, q)
        q_values[sorted_indices[i]] = min_q
        
    return np.clip(q_values, 0.0, 1.0)


def compute_log2_fc_and_wald_p(
    norm_counts: np.ndarray,
    is_treatment: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Computes log2FC, standard error, and two-tailed p-values under normality assumption.
    norm_counts: (N_genes, M_samples)
    is_treatment: boolean array of shape (M_samples,)
    """
    treat = norm_counts[:, is_treatment]
    ctrl = norm_counts[:, ~is_treatment]
    
    mean_treat = np.mean(treat, axis=1) + 1.0
    mean_ctrl = np.mean(ctrl, axis=1) + 1.0
    log2_fc = np.log2(mean_treat / mean_ctrl)
    
    # Welch t-test approx for demo
    var_treat = np.var(treat, axis=1, ddof=1) / treat.shape[1]
    var_ctrl = np.var(ctrl, axis=1, ddof=1) / ctrl.shape[1]
    se = np.sqrt(var_treat + var_ctrl) + 1e-8
    
    z_scores = (mean_treat - mean_ctrl) / se
    import scipy.stats as stats
    p_values = 2 * (1 - stats.norm.cdf(np.abs(z_scores)))
    q_values = benjamini_hochberg(p_values)
    
    return log2_fc, p_values, q_values


if __name__ == "__main__":
    np.random.seed(42)
    fake_counts = np.random.poisson(lam=50, size=(100, 6))
    fake_lens = np.random.randint(500, 5000, size=100)
    tpm = calculate_tpm(fake_counts, fake_lens)
    print("TPM matrix calculated, shape:", tpm.shape)
    sf = median_of_ratios_size_factors(fake_counts)
    print("DESeq2 Size Factors:", np.round(sf, 3))
