# Module 18 Exercises: Multi-Omics AI

### Exercise 18.1: Similarity Network Fusion (SNF) Implementation
- **Objective**: Implement SNF for 3 patient similarity matrices (mRNA, miRNA, DNA methylation) across 200 TCGA breast cancer samples.
- **Evaluation**: Perform spectral clustering on fused network and validate survival difference via log-rank test ($p < 0.05$).

### Exercise 18.2: Contrastive Multi-Omics Representation Learning
- **Objective**: Implement InfoNCE loss between single-cell RNA-seq and single-cell ATAC-seq profiles from 10x Multiome data to map chromatin accessibility to gene expression without paired cell supervision.
