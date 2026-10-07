# Module 11-Cheminformatics: Cheminformatics & Molecular Representations

## 🔬 Domain Overview
Small molecule chemical representations (SMILES, SMARTS, InChI, SELFIES), molecular graphs, circular topological fingerprints (Morgan/ECFP), QSAR modeling, and chemical space visualization.

---

## 📚 Core Scientific Curriculum & Concepts
- **Chemical Notation**: Canonical SMILES, tautomerism, chirality tags, InChI/InChIKey, 100% valid SELFIES grammar
- **Molecular Graphs**: Atoms as node feature vectors, bonds as edge feature matrices, adjacency representations
- **Molecular Fingerprints**: Morgan / ECFP4 radial fingerprints, MACCS keys, daylight topological paths
- **Similarity Metrics & Chemical Space**: Tanimoto coefficient, Dice similarity, Bemis-Murcko scaffold decomposition
- **Drug-Likeness Rules**: Lipinski's Rule of 5, Veber filters, PAINS (Pan-Assay Interference Compounds) filtering

---

## 🧮 Mathematical & Algorithmic Foundations
- Morgan Algorithm: Iterative radial environment hashing: $h_v^{(t+1)} = 	ext{hash}(h_v^{(t)}, \{(h_u^{(t)}, b_{uv}) : u \in \mathcal{N}(v)\})$
- Tanimoto Coefficient: $T(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{c}{a + b - c}$ for bit vectors
- Bemis-Murcko Scaffold: Recursive extraction of ring systems and connecting linker atoms
- Continuous molecular descriptors: MolLogP (Wildman-Crippen), Topological Polar Surface Area (TPSA)

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: PubChem, ChEMBL, ZINC20, DrugBank, SureChEMBL
- Tools: RDKit, Datamol, Molfeat, Open Babel, DeepChem

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an algorithmic Morgan/ECFP4 fingerprint generator from molecular graph adjacency matrices
- [ ] Milestone 2: Build a Bemis-Murcko scaffold splitter to enforce rigorous chemical out-of-distribution evaluation
- [ ] Milestone 3: Construct a Tanimoto similarity search engine indexing 100,000 ChEMBL molecules with sub-second queries

---

## 📂 Subdirectory Architecture
```text
11-Cheminformatics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── molecular_descriptors.py
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
