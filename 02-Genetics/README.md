# Module 02-Genetics: Genetics & Population Genomics

## 🔬 Domain Overview
Mendelian inheritance, population-level allele distribution dynamics, linkage disequilibrium (LD), and genome-wide association study (GWAS) statistical frameworks.

---

## 📚 Core Scientific Curriculum & Concepts
- **Mendelian vs Polygenic Inheritance**: Additive, dominant, and epistatic variance
- **Population Genetics Theory**: Hardy-Weinberg equilibrium, Wright-Fisher model of genetic drift, coalescence
- **Linkage Disequilibrium (LD)**: $D, D'$, and $r^2$ decay over genomic distances, haplotype blocks
- **GWAS Methodology**: Linear mixed models (LMMs), genomic control ($\lambda_{GC}$), QQ-plots, Manhattan plots
- **Polygenic Risk Scores (PRS)**: LD-clumping + thresholding (C+T), Bayesian PRS methods (PRS-CS, LDpred2)

---

## 🧮 Mathematical & Algorithmic Foundations
- Hardy-Weinberg exact test (Wigginton et al.)
- Pairwise LD metrics: $D = p_{AB} - p_A p_B$, $r^2 = \frac{D^2}{p_A(1-p_A)p_B(1-p_B)}$
- Linear Mixed Models: $y = Xeta + u + \epsilon$ where $u \sim \mathcal{N}(0, \sigma_g^2 K)$ with kinship matrix $K$
- LD Score Regression: $\mathbb{E}[\chi_j^2] = 1 + rac{N h^2}{M} \ell_j + N a$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: 1000 Genomes Project, gnomAD (Genome Aggregation Database), UK Biobank summary stats, GWAS Catalog
- Tools: PLINK 1.9 / 2.0, Hail, LDSC, PRS-CS, Regenie

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Compute pairwise LD matrices from multi-sample VCF/dosage matrices
- [ ] Milestone 2: Build a GWAS simulation module testing association with linear regression and visualizing via QQ/Manhattan plots
- [ ] Milestone 3: Implement polygenic risk scoring across held-out ancestry cohorts with cross-validation

---

## 📂 Subdirectory Architecture
```text
02-Genetics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── population_genetics.py
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
