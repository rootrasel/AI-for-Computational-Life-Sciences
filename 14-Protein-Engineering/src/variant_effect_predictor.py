"""
Protein Variant Effect Scorer:
Computes zero-shot log-odds mutation scores, compares against BLOSUM62 baseline,
and evaluates Spearman rank correlation with experimental fitness values.
"""

from typing import Dict, List, Tuple
import numpy as np
from scipy.stats import spearmanr

# Simplified BLOSUM62 subset for demo baseline
BLOSUM62_DIAG = {
    'A': 4, 'R': 5, 'N': 6, 'D': 6, 'C': 9, 'Q': 5, 'E': 5, 'G': 6,
    'H': 8, 'I': 4, 'L': 4, 'K': 5, 'M': 5, 'F': 6, 'P': 7, 'S': 4,
    'T': 5, 'W': 11, 'Y': 7, 'V': 4
}


def compute_zero_shot_log_odds(
    wt_token_log_probs: np.ndarray,
    mut_token_log_probs: np.ndarray
) -> float:
    """
    Log-odds score: log p(x_mut) - log p(x_wt)
    Higher score indicates higher predicted tolerance / fitness.
    """
    return float(mut_token_log_probs - wt_token_log_probs)


def evaluate_variant_predictions(
    predicted_scores: List[float],
    experimental_fitness: List[float]
) -> Tuple[float, float]:
    """Computes Spearman rank correlation and two-tailed p-value."""
    rho, p_value = spearmanr(predicted_scores, experimental_fitness)
    return float(rho), float(p_value)


if __name__ == "__main__":
    # Simulate 50 experimental variants
    np.random.seed(42)
    n_vars = 50
    true_fitness = np.random.normal(loc=0.0, scale=1.0, size=n_vars)
    # Model predictions with signal + noise
    model_preds = true_fitness * 0.6 + np.random.normal(loc=0.0, scale=0.5, size=n_vars)
    
    rho, p_val = evaluate_variant_predictions(model_preds, true_fitness)
    print(f"Variant Prediction Benchmark:")
    print(f"  Spearman rho: {rho:.3f} (p-value: {p_val:.2e})")
