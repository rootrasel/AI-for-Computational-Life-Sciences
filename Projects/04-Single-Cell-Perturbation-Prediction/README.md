# Project 04-Single-Cell-Perturbation-Prediction: Predicting Single-Cell Transcriptomic Responses to Chemical & Genetic Perturbations

## 🎯 Biological Objective & Clinical Impact
Predict full cellular transcriptomic response vectors to unseen drug combinations and CRISPR knockouts in high-dimensional single-cell space.

---

## 🧠 Model Architecture & Methodology
Compositional Perturbation Autoencoder (CPA) / Graph-Enhanced Gene Activation and Repression Simulator (GEARS).

---

## 📊 Datasets & Biological Provenance
Norman et al. (CRISPR Perturb-seq), Sci-Plex 3 (combinatorial drug screening).

---

## ⚖️ Baseline Methods for Benchmarking
Linear additive models, standard Conditional VAE, nearest-neighbor imputation.

---

## 📋 Recommended Work Plan
1. **Phase 1: Data Preparation & Leakage Prevention**:
   - Download and curate benchmark splits.
   - Apply strict homology/scaffold clustering.
2. **Phase 2: Baseline Implementation**:
   - Establish baseline performance metrics (ROC-AUC, PR-AUC, BEDROC, Spearman $\rho$).
3. **Phase 3: Core Model Development**:
   - Build domain-adapted model architecture with biological inductive biases.
   - Implement experiment tracking via Weights & Biases or MLflow.
4. **Phase 4: Ablation Studies & Biological Interpretability**:
   - Conduct feature importance and attention map analyses.
   - Validate predictions against external experimental or clinical databases.
5. **Phase 5: Manuscript & Reproducibility Package**:
   - Package code, configs, and Snakemake workflow for publication release.
