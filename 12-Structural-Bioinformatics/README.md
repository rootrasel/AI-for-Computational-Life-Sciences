# Module 12-Structural-Bioinformatics: Structural Bioinformatics & Macromolecular Modeling

## 🔬 Domain Overview
3D macromolecular architecture, PDB/mmCIF parsing, Ramachandran dihedral geometry, structural superposition (Kabsch algorithm), TM-score, contact maps, and molecular dynamics fundamentals.

---

## 📚 Core Scientific Curriculum & Concepts
- **3D Macromolecular Formats**: PDB coordinate records, mmCIF hierarchical data structures, atom naming conventions
- **Backbone Dihedral Geometry**: $\phi, \psi, \omega$ torsion angles, Ramachandran allowed regions, cis/trans peptide bonds
- **Secondary Structure Assignment**: DSSP hydrogen-bond energy calculations, $\alpha$-helices, $\beta$-sheets, loops
- **Structural Superposition & Similarity**: Kabsch rotation matrix, RMSD, GDT-TS, TM-score length invariance
- **Contact & Distance Maps**: $C_\alpha-C_\alpha$ distance tensors, residue-residue contact graphs ($d < 8	ext{ \AA}$)

---

## 🧮 Mathematical & Algorithmic Foundations
- Kabsch Algorithm: SVD of cross-covariance matrix $H = P^T Q = U \Sigma V^T$, optimal rotation $R = V egin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \det(V U^T) \end{pmatrix} U^T$
- Root-Mean-Square Deviation: $\text{RMSD} = \sqrt{\frac{1}{N} \sum_{i=1}^N \| R p_i + t - q_i \|^2}$
- TM-score: $\text{TM-score} = \frac{1}{L_{\text{target}}} \sum_{i=1}^{L_{\text{aligned}}} \frac{1}{1 + \left(\frac{d_i}{d_0(L_{\text{target}})}\right)^2}$
- Dihedral angle calculation using atan2 on normal vectors to planes

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: RCSB Protein Data Bank, AlphaFold Protein Structure Database, CATH, SCOPe
- Tools: PyMOL, ChimeraX, BioPandas, ProDy, MDAnalysis, OpenMM, TM-align

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an exact Kabsch algorithm computing optimal rotation and minimal RMSD between two coordinates
- [ ] Milestone 2: Build a Ramachandran dihedral angle calculator ($\phi, \psi$) from raw PDB backbone atom coordinates
- [ ] Milestone 3: Construct a pairwise $C_\alpha$ contact map generator and visualize structural domain boundaries

---

## 📂 Subdirectory Architecture
```text
12-Structural-Bioinformatics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── structure_analysis.py
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
