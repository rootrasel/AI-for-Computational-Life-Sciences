# Project 01-Target-Identification-GWAS-GNN: Target Identification via Graph Neural Networks on GWAS & Multi-Omics Interactomes

## 🎯 Biological Objective & Clinical Impact
Prioritize therapeutic drug targets for complex human diseases by integrating GWAS summary statistics, eQTLs, chromatin interaction (Hi-C), and protein-protein interaction networks.

---

## 🧠 Model Architecture & Methodology
Relational Graph Convolutional Network (R-GCN) with Gene-Tissue bipartite attention.

---

## 📊 Datasets & Biological Provenance
Open Targets Genetics, GTEx v8 expression, STRING interactome, UK Biobank GWAS summary statistics.

---

## ⚖️ Baseline Methods for Benchmarking
Random Walk with Restart (RWR), L2-regularized logistic regression, heuristic distance-based target prioritization.

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
