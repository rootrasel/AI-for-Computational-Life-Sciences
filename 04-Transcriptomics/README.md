# Module 04-Transcriptomics: Transcriptomics & RNA-Seq Analysis

## 🔬 Domain Overview
Bulk RNA sequencing pipelines, alignment-free quantification (k-mer pseudoalignment), count normalization, negative binomial generalized linear models for differential expression, and pathway enrichment.

---

## 📚 Core Scientific Curriculum & Concepts
- **RNA-Seq Library Prep**: Poly-A enrichment, ribo-depletion, stranded libraries, batch effects
- **Quantification**: Pseudoalignment (Salmon, Kallisto), transcript compatibility classes, GC bias correction
- **Count Normalization**: CPM, FPKM/RPKM, TPM, DESeq2 Median of Ratios, TMM (edgeR)
- **Differential Expression**: Negative binomial dispersion estimation, Wald test, Likelihood Ratio Test (LRT)
- **Downstream Functional Profiling**: GSEA, over-representation analysis (ORA), Gene Ontology (GO), Reactome

---

## 🧮 Mathematical & Algorithmic Foundations
- TPM Formula: $\text{TPM}_i = \frac{c_i / l_i}{\sum_j (c_j / l_j)} \times 10^6$
- Median of Ratios: Pseudo-reference sample geometric mean $m_i = \left(\prod_{k=1}^K c_{ik}\right)^{1/K}$, scaling factor $s_k = \text{median}_i \left(\frac{c_{ik}}{m_i}\right)$
- Negative Binomial distribution: $\text{Var}(Y) = \mu + lpha \mu^2$, empirical Bayes shrinkage of dispersion parameter $\alpha$
- Kolmogorov-Smirnov running-sum enrichment statistic for GSEA

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: NCBI GEO, EBI ArrayExpress, SRA, MSigDB, Enrichr
- Tools: Salmon, Kallisto, STAR, DESeq2, PyDESeq2, edgeR, FastQC, MultiQC

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an exact Salmon-style TPM and Median of Ratios normalizer from raw count matrices
- [ ] Milestone 2: Build a negative binomial GLM testing module computing $\log_2$ fold changes, Wald statistics, and Benjamini-Hochberg FDR
- [ ] Milestone 3: Construct an automated Volcano Plot and GSEA enrichment pipeline

---

## 📂 Subdirectory Architecture
```text
04-Transcriptomics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── differential_expression.py
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
