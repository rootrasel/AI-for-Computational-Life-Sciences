# Module 13-Drug-Discovery: Computer-Aided Drug Discovery (CADD)

## 🔬 Domain Overview
Target identification, high-throughput virtual screening, Structure-Based Drug Design (SBDD), Ligand-Based Drug Design (LBDD), molecular docking, and ADMET profiling.

---

## 📚 Core Scientific Curriculum & Concepts
- **Hit-to-Lead Optimization**: Potency ($IC_{50}$, $K_i$), selectivity, ligand efficiency ($LE = \Delta G / N_{\text{heavy}}$)
- **Structure-Based Design**: Active site pocket detection (fpocket), receptor grid generation, steric clash penalties
- **Molecular Docking**: Scoring functions (physics-based, empirical, neural), AutoDock Vina, DiffDock diffusion docking
- **Ligand-Based Screening**: Pharmacophore modeling, shape similarity (ROCS), QSAR bioactivity models
- **ADMET Profiling**: Cytochrome P450 inhibition (CYP3A4, CYP2D6), hERG cardiotoxicity, blood-brain barrier permeability (BBB)

---

## 🧮 Mathematical & Algorithmic Foundations
- AutoDock Vina scoring function: empirical combination of steric, hydrophobic, and hydrogen bonding terms
- Enrichment Factor at fraction $\chi$: $\text{EF}_{\chi} = \frac{\text{Actives discovered in top } \chi}{\text{Total Actives}} / \chi$
- BEDROC metric (Boltzmann-Enhanced Discrimination of ROC) with exponential weighting parameter $\alpha$
- DiffDock score: reverse diffusion on rigid receptor and flexible ligand degrees of freedom

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: ChEMBL, DrugBank, BindingDB, Therapeutics Data Commons (TDC), DUD-E benchmark
- Tools: AutoDock Vina, DiffDock, Smina, OpenBabel, RDKit, Meeko

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Build an automated virtual screening benchmark evaluator computing ROC-AUC, BEDROC, and $EF_{1\%}$
- [ ] Milestone 2: Construct an AutoDock Vina / Smina automated docking wrapper with automated box center and dimensions calculation
- [ ] Milestone 3: Train an ADMET multi-task neural network predicting hERG toxicity and solubility using TDC datasets

---

## 📂 Subdirectory Architecture
```text
13-Drug-Discovery/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── virtual_screening_eval.py
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
