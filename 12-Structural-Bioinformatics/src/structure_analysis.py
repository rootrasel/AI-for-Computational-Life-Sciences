"""
Structural Bioinformatics Foundations:
Kabsch alignment algorithm for optimal rotation, RMSD calculation,
and pairwise C-alpha distance/contact matrix computation.
"""

from typing import Tuple
import numpy as np


def kabsch_superposition(P: np.ndarray, Q: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Kabsch algorithm: superimposes coordinate matrix P onto Q.
    P, Q: shape (N, 3)
    Returns: (P_aligned, R_optimal, rmsd)
    """
    assert P.shape == Q.shape, "P and Q must have identical shapes"
    n = P.shape[0]
    
    # Centroid alignment
    centroid_P = np.mean(P, axis=0)
    centroid_Q = np.mean(Q, axis=0)
    P_centered = P - centroid_P
    Q_centered = Q - centroid_Q
    
    # Covariance matrix H
    H = np.dot(P_centered.T, Q_centered)
    
    # SVD
    U, S, Vt = np.linalg.svd(H)
    R = np.dot(Vt.T, U.T)
    
    # Reflection correction
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = np.dot(Vt.T, U.T)
        
    P_aligned = np.dot(P_centered, R.T) + centroid_Q
    rmsd = float(np.sqrt(np.sum((P_aligned - Q) ** 2) / n))
    return P_aligned, R, rmsd


def compute_contact_map(ca_coords: np.ndarray, threshold_angstrom: float = 8.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes pairwise Euclidean distance matrix and binary contact map.
    ca_coords: shape (N_residues, 3)
    """
    diff = ca_coords[:, np.newaxis, :] - ca_coords[np.newaxis, :, :]
    dist_matrix = np.linalg.norm(diff, axis=-1)
    contact_map = (dist_matrix < threshold_angstrom).astype(int)
    return dist_matrix, contact_map


if __name__ == "__main__":
    np.random.seed(42)
    # Generate random backbone 20 residues
    coords1 = np.cumsum(np.random.normal(size=(20, 3)), axis=0)
    # Apply rotation and noise to create target
    theta = np.pi / 4
    rot = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    coords2 = np.dot(coords1, rot.T) + np.array([5.0, -3.0, 2.0]) + np.random.normal(scale=0.1, size=(20, 3))
    
    aligned, R, rmsd = kabsch_superposition(coords1, coords2)
    print(f"Kabsch Superposition completed! RMSD: {rmsd:.3f} Å")
    dist_mat, contacts = compute_contact_map(aligned)
    print(f"Contact map shape: {contacts.shape}, total contacts (< 8Å): {np.sum(contacts)}")
