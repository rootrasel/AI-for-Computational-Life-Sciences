# Module 16-Biomedical-AI: Biomedical Artificial Intelligence

## 🔬 Domain Overview
Clinical Natural Language Processing, Electronic Health Record (EHR) representation learning, medical image analysis, Biomedical Knowledge Graphs (Hetionet, PrimeKG), and graph neural networks.

---

## 📚 Core Scientific Curriculum & Concepts
- **Biomedical NLP**: Pretrained domain models (PubMedBERT, BioLinkBERT), clinical entity linking, relation extraction
- **Electronic Health Records (EHR)**: Longitudinal patient trajectories, ICD-10 and SNOMED-CT codes, survival modeling
- **Biomedical Knowledge Graphs**: Node types (diseases, drugs, genes, phenotypes), link prediction, PrimeKG
- **Graph Neural Networks (GNNs)**: Relational Graph Convolutional Networks (R-GCN), HetGNN, message passing
- **Multimodal Clinical Intelligence**: Vision-language alignment (Med-CLIP), clinical note summarization

---

## 🧮 Mathematical & Algorithmic Foundations
- Knowledge Graph Embedding: TransE loss $\mathcal{L} = \max(0, \gamma + \|h + r - t\| - \|h' + r - t'\|)$
- RotatE complex rotation embedding in complex vector space: $t = h \circ r$ where $|r_i| = 1$
- Relational Graph Convolution: $h_i^{(l+1)} = \sigma \left( W_0^{(l)} h_i^{(l)} + \sum_{r \in \mathcal{R}} \sum_{j \in \mathcal{N}_i^r} \frac{1}{c_{i,r}} W_r^{(l)} h_j^{(l)} \right)$

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: MIMIC-IV, PrimeKG, Hetionet, BioPortal, UMLS, ClinVar
- Tools: Hugging Face Transformers, PyTorch Geometric (PyG), DGL, spaCy/scispaCy, MedPy

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Construct a biomedical knowledge graph loader with PyG HeteroData representations
- [ ] Milestone 2: Train a TransE / RotatE link prediction model predicting novel drug-disease therapeutic indications
- [ ] Milestone 3: Build a clinical NLP pipeline for named entity recognition (NER) on biomedical abstracts

---

## 📂 Subdirectory Architecture
```text
16-Biomedical-AI/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── biomedical_kg_loader.py
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
