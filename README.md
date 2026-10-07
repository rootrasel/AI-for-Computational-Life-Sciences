# AI for Computational Life Sciences 🧬🤖
### Comprehensive Curriculum & Research Repository for AI/ML Engineers in the Life Sciences

Welcome to the **AI for Computational Life Sciences** repository. This repository provides an end-to-end, PhD-level computational curriculum, production-grade code pipelines, landmark scientific literature, and research project blueprints at the intersection of Artificial Intelligence, Structural Biology, Genomics, and Drug Discovery.

---

## 🗺️ Master Curriculum Roadmap

The curriculum is structured into 20 progressive modules followed by end-to-end research capstones:

```text
.
├── 01-Molecular-Biology              # Physical/biochemical foundations, Central Dogma, thermodynamics
├── 02-Genetics                       # Mendelian genetics, population dynamics, GWAS, Polygenic Risk Scores
├── 03-Genomics                       # High-throughput sequencing, variant calling, GATK, DeepVariant
├── 04-Transcriptomics                # Bulk RNA-Seq, Salmon, count normalization, DESeq2 GLMs
├── 05-Proteomics                     # LC-MS/MS, DDA/DIA, spectrum matching, target-decoy FDR, MaxQuant
├── 06-Metabolomics                   # LC-MS/GC-MS profiling, PQN normalization, GNPS molecular networking
├── 07-Single-Cell-Biology            # Droplet scRNA-seq, Scanpy, manifold learning, Leiden, RNA velocity
├── 08-Systems-Biology                # Biochemical ODEs, stoichiometric Flux Balance Analysis (COBRA)
├── 09-Computational-Biology          # Dynamic programming, Needleman-Wunsch, Smith-Waterman, HMMs
├── 10-Bioinformatics                 # Workflow DAGs (Nextflow, Snakemake), containerization, file standards
├── 11-Cheminformatics                # SMILES, SELFIES, Morgan/ECFP4 fingerprints, Bemis-Murcko scaffolds
├── 12-Structural-Bioinformatics      # 3D macromolecular structures, PDB/mmCIF, Kabsch RMSD, TM-score
├── 13-Drug-Discovery                 # Target validation, AutoDock Vina, DiffDock, ADMET profiling (TDC)
├── 14-Protein-Engineering            # Fitness landscapes, DMS, zero-shot ESM language models, ProteinGym
├── 15-Vaccine-Design                 # Immunoinformatics, MHC-I/II binding, reverse vaccinology, mRNA design
├── 16-Biomedical-AI                  # Clinical NLP, EHR trajectories, biomedical knowledge graphs (PrimeKG)
├── 17-Pharmaceutical-AI              # Clinical trial matching, CMap L1000 signature reversal, FDA GMLP
├── 18-Multi-Omics-AI                 # Multimodal fusion (MOFA+), cross-modal autoencoders, patient subtyping
├── 19-Generative-AI-Life-Sciences    # 3D molecular diffusion, RFdiffusion, SE(3) equivariance, AlphaFold3
├── 20-Research-Methodology           # Biological data leakage prevention, MMseqs2, Conformal Prediction, DOME
│
└── Projects/                         # Research capstones & cookiecutter reproducible template
    ├── template/                     # Standardized, runnable research project scaffold
    ├── 01-Target-Identification-GWAS-GNN/
    ├── 02-Virtual-Screening-Molecular-Docking/
    ├── 03-Protein-Inverse-Folding-Design/
    ├── 04-Single-Cell-Perturbation-Prediction/
    └── 05-Multi-Omics-Cancer-Subtyping/
```

---

## 🔬 Standard Structure of Each Module

Every module folder (`01` through `20`) is equipped with:
- **`README.md`**: Curriculum syllabus, theoretical formulations, mathematical equations, software/database registries, and milestone deliverables.
- **`notebooks/`**: Exploratory data analysis, educational tutorials, and model prototyping.
- **`src/`**: Fully tested, typed Python algorithms and pipelines.
- **`data/`**: FAIR-compliant data directory:
  - `raw/`: Immutable raw inputs (gitignored to protect repository size).
  - `processed/`: Normalized matrices, engineered features, and splits.
  - `README.md`: Data provenance, accession IDs, and schemas.
- **`literature/`**:
  - `references.bib`: BibTeX citations for foundational peer-reviewed papers.
  - `summaries/`: Structured paper critique and literature evaluation templates.
- **`exercises/`**: Real-world research challenges and benchmarking tasks.

---

## 🛠️ Computational Environment & Dependencies

We provide both a complete Conda environment (`environment.yml`) and modern Python package configurations (`pyproject.toml`).

### Setup with Conda / Mamba (Recommended)
```bash
# Clone the repository
git clone https://github.com/rootrasel/AI-for-Computational-Life-Sciences.git
cd AI-for-Computational-Life-Sciences

# Create and activate environment
conda env create -f environment.yml
conda activate bio-ai-env

# Verify installation
python -c "import torch, rdkit, scanpy, Bio; print('Bio-AI Environment Ready!')"
```

---

## 📋 Scientific Rigor & Principles (DOME & FAIR)

All experiments and project implementations in this repository adhere to the **DOME guidelines** (*Nature Methods*, 2021):
1. **No Homology Leakage**: Sequences are partitioned using MMseqs2 or CD-HIT at < 30% identity; small molecules are split via Bemis-Murcko scaffolds.
2. **Deterministic Seed Control**: All random seeds are fixed and documented across hardware runs.
3. **Uncertainty Quantification**: Predictions provide calibrated confidence scores or conformal prediction intervals.
4. **Open Data & Reproducibility**: Workflows are orchestrated via Snakemake with versioned environments.

---

## 📜 Citation & Academic Use
If you find this repository or its curated curriculum helpful in your research or studies, please cite:
```bibtex
@misc{ai_computational_life_sciences_2026,
  author = {AI for Computational Life Sciences Contributors},
  title = {AI for Computational Life Sciences: Research-Grade Curriculum and Pipelines},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/rootrasel/AI-for-Computational-Life-Sciences}}
}
```

---

## 📄 License
This repository is open-sourced under the [MIT License](LICENSE).
