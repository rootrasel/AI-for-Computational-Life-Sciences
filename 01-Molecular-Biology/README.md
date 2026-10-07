# Module 01-Molecular-Biology: Molecular Biology for AI/ML Engineers

## 🔬 Domain Overview
Rigorous physical and biochemical foundations of nucleic acids and proteins. Bridges the gap between biochemical reality and computational abstractions (sequences, graphs, density grids).

---

## 📚 Core Scientific Curriculum & Concepts
- **Central Dogma**: Dynamic regulation beyond linear information flow
- **Nucleic Acid Chemistry**: Thermodynamics of base pairing, tautomerism, and secondary structure folding (nearest-neighbor parameters)
- **Protein Architecture**: Peptide bonds, Ramachandran steric limits, folding kinetics, and allosteric mechanisms
- **Chromatin Dynamics**: Epigenetics, histone modifications, and 3D genome organization
- **Biophysical Forces**: Hydrogen bonds, hydrophobic effect, van der Waals interactions, and electrostatic screening (Debye-Hückel)

---

## 🧮 Mathematical & Algorithmic Foundations
- Nearest-neighbor thermodynamic models for nucleic acid melting temperature ($T_m$) and free energy ($\Delta G$)
- Codon Adaptation Index (CAI) and codon usage bias calculations
- Hydrophobicity scales (Kyte-Doolittle) and sliding window biochemical profiling
- Kinetics of enzyme catalysis: Michaelis-Menten derivation and steady-state approximations

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: UniProtKB (Swiss-Prot/TrEMBL), NCBI GenBank, Ensembl, RCSB PDB
- Software & Libraries: Biopython, ViennaRNA (RNAfold), DSSP, PyMOL

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an exact nearest-neighbor RNA secondary structure free energy calculator
- [ ] Milestone 2: Build a pipeline parsing FASTA/GenBank files and computing codon usage bias and Kyte-Doolittle hydropathy profiles
- [ ] Milestone 3: Reconstruct biological sequence representations compatible with PyTorch tensors

---

## 📂 Subdirectory Architecture
```text
01-Molecular-Biology/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── biophysical_properties.py
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
