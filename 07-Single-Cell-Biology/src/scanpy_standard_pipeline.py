"""
Single-Cell RNA-Seq Standard Processing Pipeline:
Quality control filtering, normalization, highly variable gene selection,
and cell neighborhood graph analysis.
"""

from typing import Tuple, Dict
import numpy as np


class MiniAnnData:
    """Lightweight AnnData stand-in demonstrating computational transformations."""
    def __init__(self, X: np.ndarray, var_names: np.ndarray, obs_names: np.ndarray):
        self.X = X.astype(np.float64)  # shape (n_obs, n_vars)
        self.var_names = var_names
        self.obs_names = obs_names
        self.obs: Dict[str, np.ndarray] = {}
        self.var: Dict[str, np.ndarray] = {}
        self.obsm: Dict[str, np.ndarray] = {}


def run_qc_and_filtering(
    adata: MiniAnnData,
    min_genes: int = 200,
    max_mito_fraction: float = 0.20
) -> MiniAnnData:
    """Calculate QC metrics and filter damaged / low quality cells."""
    n_counts = np.sum(adata.X, axis=1)
    n_genes = np.sum(adata.X > 0, axis=1)
    
    # Identify mitochondrial genes (starting with MT-)
    is_mito = np.array([name.startswith('MT-') for name in adata.var_names])
    if np.any(is_mito):
        mito_counts = np.sum(adata.X[:, is_mito], axis=1)
        mito_frac = mito_counts / (n_counts + 1e-12)
    else:
        mito_frac = np.zeros(adata.X.shape[0])
        
    adata.obs['n_counts'] = n_counts
    adata.obs['n_genes'] = n_genes
    adata.obs['mito_fraction'] = mito_frac
    
    keep = (n_genes >= min_genes) & (mito_frac <= max_mito_fraction)
    filtered = MiniAnnData(adata.X[keep, :], adata.var_names, adata.obs_names[keep])
    for k, v in adata.obs.items():
        filtered.obs[k] = v[keep]
    return filtered


def normalize_total_and_log1p(adata: MiniAnnData, target_sum: float = 1e4) -> MiniAnnData:
    """Standard 10k library size normalization followed by natural log1p."""
    counts_per_cell = np.sum(adata.X, axis=1, keepdims=True)
    counts_per_cell[counts_per_cell == 0] = 1.0
    adata.X = (adata.X / counts_per_cell) * target_sum
    adata.X = np.log1p(adata.X)
    return adata


def select_highly_variable_genes(adata: MiniAnnData, n_top_genes: int = 2000) -> np.ndarray:
    """Identifies top variable genes using mean-variance dispersion."""
    means = np.mean(adata.X, axis=0)
    vars_ = np.var(adata.X, axis=0)
    # Dispersion score
    dispersion = vars_ / (means + 1e-6)
    top_indices = np.argsort(dispersion)[::-1][:min(n_top_genes, len(adata.var_names))]
    return top_indices


if __name__ == "__main__":
    np.random.seed(42)
    n_cells = 500
    n_features = 1000
    genes = np.array([f"GENE_{i}" if i >= 10 else f"MT-ND{i}" for i in range(n_features)])
    cells = np.array([f"CELL_{j}" for j in range(n_cells)])
    counts = np.random.poisson(lam=1.5, size=(n_cells, n_features))
    
    ad = MiniAnnData(counts, genes, cells)
    print("Initial cells:", ad.X.shape[0])
    ad_filt = run_qc_and_filtering(ad, min_genes=10)
    print("Cells after QC:", ad_filt.X.shape[0])
    ad_norm = normalize_total_and_log1p(ad_filt)
    hvg = select_highly_variable_genes(ad_norm, n_top_genes=100)
    print("Top variable genes selected:", len(hvg))
