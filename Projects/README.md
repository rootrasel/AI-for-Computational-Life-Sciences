# Computational Life Sciences Research Projects

This directory contains research-grade project blueprints and a reproducible, production-ready project template for computational biology and AI/ML in life sciences.

---

## 🧪 Scientific Project Lifecycle & Standards

Every project in this repository adheres to publication-ready standards:
1. **Hypothesis & Problem Formulation**: Clear biological or clinical utility defined before model exploration.
2. **Homology-Aware & Leakage-Free Splitting**: Strict sequence clustering (< 30% sequence identity via MMseqs2) or chemical scaffold splits (Bemis-Murcko).
3. **Rigorous Baselines**: Comparative evaluation against established biochemical or statistical methods (e.g., standard physics-based docking, classical linear mixed models, standard PCA/logistic regression).
4. **Uncertainty Quantification**: Conformal prediction sets or Bayesian uncertainty intervals rather than point estimates alone.
5. **DOME Compliance**: Transparent documentation of Data, Optimization, Model, and Evaluation parameters.
6. **Reproducibility & FAIR Principles**: Deterministic random seeds, version-pinned Conda/Docker environments, automated pipeline execution (Snakemake).

---

## 📁 Projects Index

| Code | Project Title | Primary Modality | Target Architecture |
|---|---|---|---|
| **01** | [Target Identification via GWAS & GNN](./01-Target-Identification-GWAS-GNN/) | Genomics / Interactome | Relational Graph Convolutional Network (R-GCN) |
| **02** | [Virtual Screening & Molecular Docking](./02-Virtual-Screening-Molecular-Docking/) | Cheminformatics / Structures | Equivariant GNN + AutoDock Vina / DiffDock |
| **03** | [Protein Redesign & Stability Optimization](./03-Protein-Inverse-Folding-Design/) | Structural Proteomics | ProteinMPNN + ESM-2 Language Models |
| **04** | [Single-Cell Perturbation Prediction](./04-Single-Cell-Perturbation-Prediction/) | Single-Cell RNA-seq | Compositional Perturbation Autoencoder (CPA/GEARS) |
| **05** | [Multi-Omics Cancer Patient Stratification](./05-Multi-Omics-Cancer-Subtyping/) | Multi-Omics / Clinical | Multimodal VAE + Cox Survival Regularization |

---

## 🛠️ Reproducible Project Template
Use [`template/`](./template/) as the standardized blueprint for any new research investigation.
