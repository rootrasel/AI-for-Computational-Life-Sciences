# Module 09-Computational-Biology: Algorithmic Computational Biology

## 🔬 Domain Overview
Fundamental algorithmic formulations for biological sequences and structures: dynamic programming, Burrows-Wheeler Transform, Markov models, profile HMMs, and phylogenetic tree algorithms.

---

## 📚 Core Scientific Curriculum & Concepts
- **Sequence Alignment**: Needleman-Wunsch global, Smith-Waterman local, affine gap penalties (Gotoh algorithm)
- **Indexing & Pattern Matching**: Suffix trees, suffix arrays, Burrows-Wheeler Transform, FM-Index
- **Hidden Markov Models**: Profile HMMs, Viterbi decoding, Baum-Welch training, HMMER architecture
- **Phylogenetics**: Distance-based (Neighbor-Joining, UPGMA), character-based (Maximum Parsimony, Maximum Likelihood)
- **Structural Geometry**: Dynamic programming for RNA secondary structure (Nussinov & Zuker algorithms)

---

## 🧮 Mathematical & Algorithmic Foundations
- Needleman-Wunsch matrix recurrence: $F(i,j) = \max \begin{cases} F(i-1,j-1) + s(x_i, y_j) \\ F(i-1,j) - d \\ F(i,j-1) - d \end{cases}$
- Affine gap penalties: $W(k) = u + v \cdot k$, Gotoh's 3-matrix linear formulation
- Nussinov RNA folding recurrence: $\max(E(i+1, j), E(i, j-1), E(i+1, j-1) + \delta(i,j), \max_k [E(i,k) + E(k+1,j)])$
- Neighbor-Joining $Q$-matrix: $Q(i,j) = (n-2)d(i,j) - \sum_{k} d(i,k) - \sum_{k} d(j,k)$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: Rfam, Pfam, TreeBASE, NCBI BLAST
- Tools: BLAST+, HMMER, Clustal Omega, MAFFT, IQ-TREE, Biopython

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Implement Needleman-Wunsch and Smith-Waterman with affine gap penalties and traceback in Python
- [ ] Milestone 2: Implement Nussinov secondary structure base-pair maximization algorithm
- [ ] Milestone 3: Implement the Neighbor-Joining phylogenetic tree reconstruction algorithm

---

## 📂 Subdirectory Architecture
```text
09-Computational-Biology/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── sequence_alignment_algorithms.py
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
