# Project 03-Protein-Inverse-Folding-Design: De Novo Protein Redesign & Stability Optimization using Inverse Folding

## 🎯 Biological Objective & Clinical Impact
Redesign enzymatic backbones for elevated thermal stability and catalytic activity using fixed-backbone structural sequence generation.

---

## 🧠 Model Architecture & Methodology
ProteinMPNN message-passing encoder-decoder conditioned on backbone coordinates, filtered by ESM-2 language model zero-shot scoring.

---

## 📊 Datasets & Biological Provenance
CATH 4.3 structural database, ProteinGym deep mutational scanning benchmarks.

---

## ⚖️ Baseline Methods for Benchmarking
Rosetta Fixbb, FoldX energy calculations, random mutation sampling.

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
