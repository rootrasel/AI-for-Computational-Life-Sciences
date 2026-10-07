"""
Drug Repurposing via Transcriptomic Signature Matching:
Implements Connectivity Map (CMap) Kolmogorov-Smirnov style
enrichment score comparing disease signatures to drug perturbagens.
"""

from typing import List, Tuple
import numpy as np


def compute_ks_enrichment_score(ranked_genes: List[str], query_gene_set: List[str]) -> float:
    """
    Computes Kolmogorov-Smirnov running sum enrichment score.
    ranked_genes: all genes ordered from most upregulated to most downregulated by drug.
    query_gene_set: disease signature genes (e.g. disease upregulated genes).
    """
    n = len(ranked_genes)
    t = len(query_gene_set)
    if t == 0 or n == 0:
        return 0.0
        
    query_set = set(query_gene_set)
    in_set_step = 1.0 / t
    out_set_step = 1.0 / (n - t)
    
    running_sum = 0.0
    max_dev = 0.0
    for gene in ranked_genes:
        if gene in query_set:
            running_sum += in_set_step
        else:
            running_sum -= out_set_step
        if abs(running_sum) > abs(max_dev):
            max_dev = running_sum
            
    return float(max_dev)


def connectivity_score(
    drug_ranked_genes: List[str],
    disease_up_genes: List[str],
    disease_down_genes: List[str]
) -> float:
    """
    Connectivity Score: A negative score suggests the drug reverses the disease phenotype.
    """
    es_up = compute_ks_enrichment_score(drug_ranked_genes, disease_up_genes)
    es_down = compute_ks_enrichment_score(drug_ranked_genes, disease_down_genes)
    return (es_up - es_down) / 2.0


if __name__ == "__main__":
    all_genes = [f"G_{i}" for i in range(1000)]
    # Disease has G_0..G_9 up, G_990..G_999 down
    dis_up = [f"G_{i}" for i in range(10)]
    dis_down = [f"G_{i}" for i in range(990, 1000)]
    
    # Drug reverses disease: downregulates G_0..G_9, upregulates G_990..G_999
    drug_ranked = all_genes[::-1]
    
    c_score = connectivity_score(drug_ranked, dis_up, dis_down)
    print(f"Connectivity score for reversing drug: {c_score:.3f} (Negative = Therapeutic Reversal)")
