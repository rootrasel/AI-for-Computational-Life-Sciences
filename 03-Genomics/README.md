# Module 03-Genomics: High-Throughput Genomics & Variant Calling

## 🔬 Domain Overview
Next-generation sequencing (NGS) and third-generation long-read technologies, sequence alignment algorithms, variant discovery (SNVs, Indels, Structural Variants), and genomic annotation.

---

## 📚 Core Scientific Curriculum & Concepts
- **Sequencing Technologies**: Illumina SBS, PacBio HiFi (circular consensus), Oxford Nanopore raw pore signals
- **Reference Genomes**: Coordinate indexing, GRCh38 vs T2T-CHM13, coordinate liftover
- **Read Alignment**: Seed-and-extend heuristics, Burrows-Wheeler Transform with FM-index, minimizers
- **Variant Calling**: GATK HaplotypeCaller local de novo assembly, DeepVariant CNN architecture
- **Structural Variation**: Split reads, discordant read pairs, coverage depth signatures

---

## 🧮 Mathematical & Algorithmic Foundations
- FM-Index backward search for exact string matching: $\mathcal{O}(m)$ time complexity
- CIGAR string parsing and coordinate mapping (M, I, D, N, S, H)
- Transition/Transversion (Ti/Tv) ratio validation: expected $\sim 2.0-2.1$ for whole genome, $\sim 2.8-3.3$ for exome
- DeepVariant inception-style residual CNN operating on multi-channel piled-up read tensors

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: UCSC Genome Browser, Ensembl, dbSNP, ClinVar, gnomAD
- Tools: SAMtools, BCFtools, BWA-MEM2, Minimap2, GATK4, DeepVariant, IGV

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Parse BAM alignments, calculate mapping quality distributions, and detect coverage drops
- [ ] Milestone 2: Build a VCF parser computing sample-level Ti/Tv ratios, depth histograms, and ClinVar pathogenicity matches
- [ ] Milestone 3: Construct a genomic image generator turning aligned read windows into multi-channel tensors for CNN variant classification

---

## 📂 Subdirectory Architecture
```text
03-Genomics/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── vcf_parser_qc.py
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
