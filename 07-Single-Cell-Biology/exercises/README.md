# Module 07 Exercises: Single-Cell Omics

### Exercise 7.1: Variational Autoencoder for scRNA-seq (Mini-scVI)
- **Objective**: Build a PyTorch Variational Autoencoder modeling scRNA-seq count distributions via Zero-Inflated Negative Binomial (ZINB) likelihood.
- **Task**: Disentangle cell-specific library size scaling factors from biologically meaningful 10-dimensional latent cell state embeddings.

### Exercise 7.2: RNA Velocity Phase-Portrait & Arrow Plotting
- **Objective**: Implement the dynamical model of RNA velocity ($ds/dt = u - \gamma s$).
- **Task**: Given spliced and unspliced matrices, estimate the degradation rate $\gamma$ per gene and project velocity arrows onto 2D UMAP space.
