# Module 05-Proteomics: Quantitative Proteomics & Mass Spectrometry

## 🔬 Domain Overview
LC-MS/MS data acquisition strategies (DDA vs DIA), peptide-spectrum matching, FDR calculation via target-decoy search, label-free quantification (LFQ), isobaric labeling (TMT), and protein interaction networks.

---

## 📚 Core Scientific Curriculum & Concepts
- **Mass Spectrometry Principles**: Electrospray ionization (ESI), Orbitrap/ToF analyzers, collision-induced dissociation (CID/HCD)
- **DDA vs DIA**: Data-dependent vs data-independent acquisition (SWATH-MS)
- **Peptide Identification**: In-silico digestion, theoretical b/y ion series, cross-correlation scoring (SEQUEST), hyperscore (X!Tandem)
- **Target-Decoy Database Search**: False discovery rate (FDR) control at PSM, peptide, and protein levels
- **Quantification & PTMs**: Precursor intensity integration, TMT reporter ions, phosphorylation site localization

---

## 🧮 Mathematical & Algorithmic Foundations
- Theoretical fragment ion m/z formulas for b- and y-ions: $m/z(b_n) = \frac{\sum_{i=1}^n M(aa_i) + M(H^+)}{z}$
- Target-Decoy FDR: $\text{FDR} = \frac{N_{\text{decoy}}}{N_{\text{target}}}$
- Percolator SVM score optimization for multi-feature PSM reranking
- MaxLFQ algorithm for consistent label-free quantification across missing values

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: PRIDE, ProteomeXchange, PhosphoSitePlus, STRING, BioGRID
- Tools: MaxQuant, MSFragger, DIA-NN, Pyteomics, OpenMS, Percolator

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Build an in-silico tryptic cleavage engine with missed cleavages support
- [ ] Milestone 2: Implement theoretical b/y ion series generator and compute spectrum cosine similarity against experimental peaks
- [ ] Milestone 3: Construct a target-decoy FDR filtering pipeline and protein roll-up quantifier

---

## 📂 Subdirectory Architecture
```text
05-Proteomics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── ms_spectrum_matcher.py
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
