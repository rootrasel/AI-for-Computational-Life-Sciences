"""
Generative AI for Life Sciences:
E(3)-Equivariant Graph Layer (EGNN) and toy 3D coordinate denoising step
for pocket-conditioned molecular diffusion.
"""

from typing import Tuple
import torch
import torch.nn as nn


class EGNNLayer(nn.Module):
    """
    Equivariant Graph Convolutional Layer (Satorras et al., 2021).
    Ensures translation, rotation, and reflection equivariance for 3D coordinates.
    """
    def __init__(self, node_dim: int, edge_dim: int = 0):
        super().__init__()
        self.message_mlp = nn.Sequential(
            nn.Linear(node_dim * 2 + 1 + edge_dim, 64),
            nn.SiLU(),
            nn.Linear(64, 64),
            nn.SiLU()
        )
        self.coord_mlp = nn.Sequential(
            nn.Linear(64, 1, bias=False)
        )
        self.node_mlp = nn.Sequential(
            nn.Linear(node_dim + 64, node_dim),
            nn.SiLU()
        )

    def forward(
        self,
        h: torch.Tensor,
        x: torch.Tensor,
        edge_index: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        h: shape (N, node_dim) invariant node features
        x: shape (N, 3) 3D coordinate tensor
        edge_index: shape (2, E)
        """
        row, col = edge_index
        # Pairwise squared Euclidean distance (invariant scalar)
        rel_x = x[row] - x[col]
        dist_sq = torch.sum(rel_x ** 2, dim=-1, keepdim=True)
        
        # Message computation
        msg_input = torch.cat([h[row], h[col], dist_sq], dim=-1)
        m_ij = self.message_mlp(msg_input)
        
        # Equivariant coordinate update: sum (x_i - x_j) * phi_x(m_ij)
        coord_weights = self.coord_mlp(m_ij)
        # Aggregate coordinates per node
        coord_diff = rel_x * coord_weights
        agg_x = torch.zeros_like(x)
        agg_x.index_add_(0, row, coord_diff)
        x_new = x + agg_x
        
        # Aggregate invariant messages
        agg_m = torch.zeros_like(h)
        agg_m.index_add_(0, row, m_ij)
        h_new = self.node_mlp(torch.cat([h, agg_m], dim=-1))
        
        return h_new, x_new


if __name__ == "__main__":
    torch.manual_seed(42)
    layer = EGNNLayer(node_dim=16)
    h = torch.randn(6, 16)
    x = torch.randn(6, 3)
    # Fully connected edges (no self loops)
    row = []
    col = []
    for i in range(6):
        for j in range(6):
            if i != j:
                row.append(i)
                col.append(j)
    edge_idx = torch.tensor([row, col], dtype=torch.long)
    
    h_out, x_out = layer(h, x, edge_idx)
    print("EGNN Forward Pass successful!")
    print("Updated coords shape:", x_out.shape)
    print("Updated features shape:", h_out.shape)
