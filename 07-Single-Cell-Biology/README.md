# Module 07-Single-Cell-Biology: Single-Cell Omics & Cellular Atlas

## 🔬 Domain Overview
Single-cell RNA sequencing (scRNA-seq), quality control, ambient RNA correction, normalization, high-dimensional manifold learning (PCA, UMAP), graph-based clustering (Leiden), marker gene discovery, and RNA velocity.

---

## 📚 Core Scientific Curriculum & Concepts
- **Droplet Microfluidics**: 10x Chromium barcoding, GEMs, PCR amplification bias, ambient RNA contamination
- **Quality Control**: Mitochondrial read fractions, ribosomal genes, Scrublet doublet detection
- **Manifold Learning & Clustering**: Highly variable gene selection, k-NN graph construction, Leiden community detection
- **Differential Abundance & Expression**: Wilcoxon rank-sum, hurdle models, marker gene specificity
- **Dynamic Single-Cell Modeling**: Spliced vs unspliced transcripts, RNA velocity ODEs (scVelo), trajectory inference (PAGA)

---

## 🧮 Mathematical & Algorithmic Foundations
- Poisson-Gamma / Negative Binomial modeling of UMI dropouts
- PCA projection and k-nearest neighbors graph with UMAP fuzzy simplicial sets
- Leiden algorithm modularity optimization: $\mathcal{H} = \frac{1}{2m} \sum_{ij} \left( A_{ij} - \gamma \frac{k_i k_j}{2m} \right) \delta(c_i, c_j)$
- RNA Velocity Phase Plane: $\frac{ds}{dt} = u(t) - \gamma s(t)$, steady-state slope $\gamma = \frac{u}{s}$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: Human Cell Atlas (HCA), CellxGene, Single Cell Expression Atlas, Tabula Sapiens
- Tools: Scanpy, AnnData, Seurat, scvi-tools, scVelo, CellRanger, Scrublet

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Build a complete AnnData preprocessing pipeline with QC filtering and doublet score assignment
- [ ] Milestone 2: Implement Leiden graph clustering and automated cell-type annotation using reference marker sets
- [ ] Milestone 3: Construct an RNA velocity phase-portrait solver calculating splicing equilibrium ratios

---

## 📂 Subdirectory Architecture
```text
07-Single-Cell-Biology/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── scanpy_standard_pipeline.py
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
