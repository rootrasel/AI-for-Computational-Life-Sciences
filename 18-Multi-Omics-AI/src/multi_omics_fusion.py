"""
Multi-Omics Intermediate Fusion Architecture:
PyTorch multimodal autoencoder with shared joint latent bottleneck
for integrating gene expression and DNA methylation data.
"""

from typing import Tuple
import torch
import torch.nn as nn


class MultiOmicsAutoencoder(nn.Module):
    def __init__(self, dim_rna: int = 500, dim_meth: int = 300, latent_dim: int = 32):
        super().__init__()
        # RNA branch
        self.enc_rna = nn.Sequential(
            nn.Linear(dim_rna, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Linear(128, 64)
        )
        # Methylation branch
        self.enc_meth = nn.Sequential(
            nn.Linear(dim_meth, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Linear(128, 64)
        )
        # Joint bottleneck
        self.joint_encoder = nn.Linear(64 + 64, latent_dim)
        
        # Joint decoder to separate reconstructions
        self.joint_decoder = nn.Linear(latent_dim, 128)
        self.dec_rna = nn.Linear(128, dim_rna)
        self.dec_meth = nn.Linear(128, dim_meth)

    def forward(self, x_rna: torch.Tensor, x_meth: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        h_rna = self.enc_rna(x_rna)
        h_meth = self.enc_meth(x_meth)
        # Concatenate intermediate representations
        h_joint = torch.cat([h_rna, h_meth], dim=-1)
        z = self.joint_encoder(h_joint)
        
        # Reconstruction
        d = torch.relu(self.joint_decoder(z))
        rec_rna = self.dec_rna(d)
        rec_meth = self.dec_meth(d)
        return rec_rna, rec_meth, z


if __name__ == "__main__":
    torch.manual_seed(42)
    model = MultiOmicsAutoencoder(dim_rna=500, dim_meth=300, latent_dim=16)
    dummy_rna = torch.randn(8, 500)
    dummy_meth = torch.randn(8, 300)
    r_rna, r_meth, z = model(dummy_rna, dummy_meth)
    print("Multi-Omics Autoencoder forward pass successful!")
    print("Latent embedding shape:", z.shape)
    print("RNA reconstruction shape:", r_rna.shape)
    print("Meth reconstruction shape:", r_meth.shape)
