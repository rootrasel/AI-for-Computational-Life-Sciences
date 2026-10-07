# Module 19-Generative-AI-Life-Sciences: Generative AI for Life Sciences

## 🔬 Domain Overview
Modern generative architectures for biology: 3D molecular diffusion (TargetDiff, EDM), protein backbone generation with $SO(3)$ and $SE(3)$ diffusion (RFdiffusion, Chroma), autoregressive protein language generation (ProGen), and unified biomolecular foundation models (AlphaFold3, ESM3).

---

## 📚 Core Scientific Curriculum & Concepts
- **Diffusion Models on Geometric Graphs**: Denoising diffusion probabilistic models (DDPM), score matching, continuous flow matching
- **Equivariance & Invariance**: $E(3)$ and $SE(3)$ equivariant message passing (EGNN, Tensor Field Networks), invariant representations
- **Protein Backbone Generation**: Rigid body frame representations ($T \in SE(3)$), torsion diffusion, motif scaffolding
- **Autoregressive Biomolecular Models**: Byte-level and BPE tokenization, sequence infilling, ProGen, ESM3 unified modality tokens
- **De Novo Molecular Design**: 3D pocket-conditioned ligand generation, property-guided sampling via classifier-free guidance

---

## 🧮 Mathematical & Algorithmic Foundations
- EGNN Equivariant Coordinate Update: $x_i^{(l+1)} = x_i^{(l)} + \sum_{j 
eq i} (x_i^{(l)} - x_j^{(l)}) \phi_x(m_{ij})$
- $SO(3)$ Rodrigues rotation formula and isotropic Gaussian distributions on Lie groups
- Classifier-Free Guidance for molecular properties: $	ilde{\epsilon}_	heta(x_t, c) = (1 + w)\epsilon_	heta(x_t, c) - w\epsilon_	heta(x_t, \emptyset)$
- Flow Matching conditional vector field: $v_t(x) = x_1 - (1 - \sigma_{\min})x_0$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: PDB, AlphaFold DB, CATH, ZINC20, PubChem
- Tools: RFdiffusion, ProteinMPNN, DiffDock, TargetDiff, OpenFold, ColabFold, BioNeMo

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement an E(n)-Equivariant Graph Neural Network (EGNN) coordinate update layer in PyTorch
- [ ] Milestone 2: Build a toy 3D coordinate diffusion denoising model with linear noise schedule
- [ ] Milestone 3: Construct an autoregressive protein sequence generator sampling from an ESM language model

---

## 📂 Subdirectory Architecture
```text
19-Generative-AI-Life-Sciences/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── equivariant_diffusion_toy.py
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
