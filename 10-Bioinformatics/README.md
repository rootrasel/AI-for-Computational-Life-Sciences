# Module 10-Bioinformatics: Reproducible Bioinformatics & Pipeline Engineering

## 🔬 Domain Overview
Scientific workflow management (Nextflow, Snakemake), containerization (Docker, Apptainer/Singularity), standard biological file formats, CI/CD for science, and cloud computing.

---

## 📚 Core Scientific Curriculum & Concepts
- **Workflow Orchestration**: Directed Acyclic Graph (DAG) task execution, resume caching, dynamic process scaling
- **Nextflow & nf-core Architecture**: Channels, processes, operators, modules, parameter schemas
- **Snakemake Design**: Wildcards, rules, conda integration, shadow directories, cluster execution profiles
- **Containerization & Reproducibility**: Bioconda, multi-stage Docker builds, Apptainer in HPC SLURM environments
- **File Format Specifications**: FASTA, FASTQ (Phred scores), SAM/BAM/CRAM, VCF, BED, BigWig, GFF3/GTF

---

## 🧮 Mathematical & Algorithmic Foundations
- Phred quality score logarithmic error probability: $Q = -10 \log_{10} P_{\text{error}}$
- Topological sorting algorithms (Kahn's algorithm) for workflow DAG dependency resolution
- Deterministic cryptographic hash verification (SHA-256) for reproducible pipeline inputs

---

## 🗄️ Key Biological Databases & Software Tools
- Registries: nf-core, Bioconda, BioContainers, Galaxy ToolShed
- Tools: Nextflow, Snakemake, FastQC, MultiQC, Docker, Singularity, Conda

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Construct a robust Python pipeline DAG validator with cycle detection and parallel execution simulator
- [ ] Milestone 2: Build a complete FASTQ quality control parser calculating per-base Phred scores and adapter contamination
- [ ] Milestone 3: Write a production-ready Snakemake workflow for raw reads to BAM alignment and QC

---

## 📂 Subdirectory Architecture
```text
10-Bioinformatics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── workflow_dag_validator.py
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
