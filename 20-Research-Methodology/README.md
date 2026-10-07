# Module 20-Research-Methodology: Research Methodology & Rigor in Bio-AI

## 🔬 Domain Overview
Scientific methodology, avoiding data leakage in computational biology, homology-based splitting (MMseqs2 / CD-HIT), chemistry scaffold splits, uncertainty quantification, DOME guidelines, and FAIR principles.

---

## 📚 Core Scientific Curriculum & Concepts
- **Data Leakage in Biology**: Sequence homology leakage, structure similarity leakage, patient batch confounding
- **Homology-Aware Splitting**: Sequence clustering (MMseqs2, CD-HIT) at 30% identity, structural CATH cluster splits
- **Chemistry Splitting**: Bemis-Murcko scaffold split, butina clustering, temporal splits for clinical benchmarks
- **Uncertainty Quantification**: Conformal prediction (coverage guarantees), Bayesian deep learning, temperature scaling
- **Publishing Standards**: DOME recommendations (Data, Optimization, Model, Evaluation), FAIR data, reproducibility checklist

---

## 🧮 Mathematical & Algorithmic Foundations
- Homology Clustering: Sequence identity threshold $S_{id} = \frac{\text{Identical residues}}{\min(L_1, L_2)} < 0.30$
- Conformal Prediction Score: Non-conformity score $s_i = 1 - \hat{p}(y_i \mid x_i)$, $(1-lpha)$ prediction set threshold $\hat{q} = 	ext{Quantile}\left(\frac{\lceil (n+1)(1-lpha) ceil}{n}\right)$
- Expected Calibration Error (ECE): $\text{ECE} = \sum_{m=1}^M \frac{|B_m|}{N} |\text{acc}(B_m) - \text{conf}(B_m)|$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: Zenodo, Dryad, OSF, Hugging Face Datasets, Papers with Code
- Tools: MMseqs2, CD-HIT, MAPIE (conformal prediction), Weights & Biases, MLflow, pytest

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an automated MMseqs2/CD-HIT sequence homology partitioning pipeline enforcing < 30% sequence identity between train and test sets
- [ ] Milestone 2: Build a Split Conformal Prediction engine guaranteeing exact $(1-lpha)$ coverage intervals for binding affinity predictions
- [ ] Milestone 3: Generate a comprehensive DOME validation checklist report for machine learning models in biology

---

## 📂 Subdirectory Architecture
```text
20-Research-Methodology/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── biological_splitters.py
├── data/
│   ├── raw/                # Immutable external datasets (git-ignored)
│   ├── processed/          # Cleaned, standardized tensors and tables
│   └── README.md           # Data dictionary & FAIR provenance specifications
├── literature/
│   ├── summaries/          # Structured critiques of landmark publications
│   └── references.bib      # BibTeX references of seminal peer-reviewed papers
└── exercises/
    └── README.md           # Research-grade coding challenges & validation benchmarks
```

---

## 📖 Curated Landmark Literature
Refer to [`literature/references.bib`](./literature/references.bib) for complete BibTeX citations.
