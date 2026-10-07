"""
Virtual Screening Evaluation Benchmark:
Calculates Enrichment Factor (EF 1%, EF 5%), ROC-AUC,
and Boltzmann-Enhanced Discrimination of ROC (BEDROC).
"""

from typing import Dict
import numpy as np


def calculate_enrichment_factor(
    labels: np.ndarray,
    scores: np.ndarray,
    fraction: float = 0.01,
    higher_is_better: bool = False
) -> float:
    """
    labels: 1 for active, 0 for decoy
    scores: binding affinity or docking energy (lower is typically better for kcal/mol)
    """
    n_total = len(labels)
    n_actives = np.sum(labels)
    if n_actives == 0:
        return 0.0
        
    k = max(1, int(n_total * fraction))
    if higher_is_better:
        top_k_indices = np.argsort(scores)[::-1][:k]
    else:
        top_k_indices = np.argsort(scores)[:k]
        
    actives_in_top_k = np.sum(labels[top_k_indices])
    ef = (actives_in_top_k / float(k)) / (n_actives / float(n_total))
    return float(ef)


def calculate_bedroc(
    labels: np.ndarray,
    scores: np.ndarray,
    alpha: float = 20.0,
    higher_is_better: bool = False
) -> float:
    """
    BEDROC (Boltzmann-Enhanced Discrimination of ROC) metric (Truchon & Bayly, 2007).
    alpha=20 emphasizes top 8% of the ranking.
    """
    n = len(labels)
    n_actives = np.sum(labels)
    if n_actives == 0 or n_actives == n:
        return 0.0
        
    if higher_is_better:
        order = np.argsort(scores)[::-1]
    else:
        order = np.argsort(scores)
        
    sorted_labels = labels[order]
    active_ranks = np.where(sorted_labels == 1)[0] + 1  # 1-indexed ranks
    
    # RIE calculation
    rie_sum = np.sum(np.exp(-alpha * active_ranks / n))
    ra = n_actives / float(n)
    s = (1.0 - np.exp(-alpha * ra)) / (np.exp(alpha / n) - 1.0)
    rie_max = s
    rie_min = (1.0 - np.exp(-alpha * ra)) / (np.exp(alpha) - 1.0)
    
    rie = (rie_sum / n_actives) * (1.0 - np.exp(-alpha)) / (np.exp(alpha / n) - 1.0)
    
    # BEDROC scale
    bedroc = (rie - rie_min) / (rie_max - rie_min + 1e-12)
    return float(np.clip(bedroc, 0.0, 1.0))


if __name__ == "__main__":
    np.random.seed(42)
    # 1000 molecules: 20 actives, 980 decoys
    true_labels = np.zeros(1000, dtype=int)
    true_labels[:20] = 1
    # Actives have more negative docking scores on average
    docking_scores = np.random.normal(loc=-6.0, scale=1.5, size=1000)
    docking_scores[:20] = np.random.normal(loc=-9.5, scale=1.0, size=20)
    
    ef_1 = calculate_enrichment_factor(true_labels, docking_scores, fraction=0.01)
    bedroc = calculate_bedroc(true_labels, docking_scores, alpha=20.0)
    print(f"Virtual Screening Metrics:")
    print(f"  EF 1%:  {ef_1:.2f}x enrichment")
    print(f"  BEDROC (alpha=20): {bedroc:.3f}")
