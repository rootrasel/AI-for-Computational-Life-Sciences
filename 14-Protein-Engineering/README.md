# Module 14-Protein-Engineering: Machine Learning for Protein Engineering

## 🔬 Domain Overview
Directed evolution in silico, fitness landscapes, Deep Mutational Scanning (DMS), zero-shot mutation effect prediction with Protein Language Models (ESM-1v, ESM-2), and sequence-to-function modeling.

---

## 📚 Core Scientific Curriculum & Concepts
- **Fitness Landscapes**: Epistasis (additive vs non-additive), ruggedness, sequence-space exploration
- **Deep Mutational Scanning (DMS)**: Experimental platforms (phage display, deep sequencing), enrichment ratio quantification
- **Protein Language Models**: Masked language modeling (MLM) on UniRef, evolutionary representation learning
- **Zero-Shot Variant Prediction**: Log-odds ratios of wildtype vs mutant residues, ProteinGym benchmarks
- **Fixed-Backbone Sequence Design**: ProteinMPNN inverse folding, autoregressive sequence generation

---

## 🧮 Mathematical & Algorithmic Foundations
- ESM Zero-Shot Log-Odds Score: $\Delta \mathcal{S}(x, i, a_{\text{mut}}) = \log P(x_i = a_{\text{mut}} \mid x_{\setminus i}) - \log P(x_i = a_{\text{wt}} \mid x_{\setminus i})$
- Gaussian Process Regression with string kernels / ESM embeddings for active learning optimization
- Spearman rank correlation coefficient $\rho$ for evaluation against experimental fitness

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: ProteinGym, FitnessScape, UniProt, MaveDB
- Tools: fair-esm, ProteinMPNN, FoldX, Rosetta, ColabFold

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an exact zero-shot mutation effect scorer computing wild-type vs mutant log-odds ratios
- [ ] Milestone 2: Build an active learning loop with Gaussian Process Upper Confidence Bound (GP-UCB) for directed evolution
- [ ] Milestone 3: Benchmark variant effect predictions against a MaveDB DMS dataset using Spearman rank correlation

---

## 📂 Subdirectory Architecture
```text
14-Protein-Engineering/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── variant_effect_predictor.py
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
