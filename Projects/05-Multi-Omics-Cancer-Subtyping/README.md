# Project 05-Multi-Omics-Cancer-Subtyping: Unsupervised Pan-Cancer Patient Stratification & Survival Prediction via Multi-Omics VAE

## 🎯 Biological Objective & Clinical Impact
Discover clinically distinct cancer subtypes and predict overall survival by learning joint representations from transcriptomics, somatic mutations, and DNA methylation.

---

## 🧠 Model Architecture & Methodology
Multimodal Variational Autoencoder (MVAE) with Cox Proportional Hazards survival loss head.

---

## 📊 Datasets & Biological Provenance
The Cancer Genome Atlas (TCGA) Pan-Cancer Atlas (BRCA, LUAD, GBM cohorts).

---

## ⚖️ Baseline Methods for Benchmarking
Principal Component Analysis + K-Means, Similarity Network Fusion (SNF), single-omic Cox models.

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
