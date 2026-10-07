# Project 02-Virtual-Screening-Molecular-Docking: Structure-Based High-Throughput Virtual Screening & Pose Generation

## 🎯 Biological Objective & Clinical Impact
Screen multi-million molecule chemical libraries against difficult oncology targets (e.g. KRAS G12D) combining fast graph transformer affinity filtering and AutoDock Vina / DiffDock structural pose docking.

---

## 🧠 Model Architecture & Methodology
Equivariant Graph Neural Network (EGNN) score head + AutoDock Vina rigid-receptor docking pipeline.

---

## 📊 Datasets & Biological Provenance
DUD-E benchmark, ChEMBL 33 KRAS bioassays, PDB crystal complexes (7T4S).

---

## ⚖️ Baseline Methods for Benchmarking
Random forest with ECFP4 fingerprints, traditional Smina empirical scoring, AutoDock Vina.

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
