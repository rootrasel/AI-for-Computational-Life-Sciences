# Module 08-Systems-Biology: Systems Biology & Network Medicine

## 🔬 Domain Overview
Dynamic mathematical modeling of biochemical systems, Ordinary Differential Equations (ODEs), Flux Balance Analysis (FBA) of genome-scale metabolic models, and network medicine topology.

---

## 📚 Core Scientific Curriculum & Concepts
- **Biochemical Kinetics**: Mass action, Michaelis-Menten, Hill equations for cooperativity, substrate inhibition
- **Ordinary Differential Equations (ODEs)**: Stiff solvers, sensitivity analysis, limit cycles, and bifurcation analysis
- **Constraint-Based Modeling**: Genome-scale metabolic networks, stoichiometric matrix $S$, Flux Balance Analysis (FBA)
- **Network Biology**: Degree distributions, centrality metrics, disease modules in human interactome
- **Boolean Network Modeling**: Attractors, cell fate decision landscapes, Waddington epigenetic landscape

---

## 🧮 Mathematical & Algorithmic Foundations
- Flux Balance Analysis linear programming: $\max c^T v$ subject to $S v = 0$ and $v_{\min} \le v \le v_{\max}$
- Runge-Kutta 4th Order & Radau stiff ODE integration methods
- Network Medicine Disease Module overlap: $s_{AB} = \langle d_{AB} angle - \frac{\langle d_{AA} angle + \langle d_{BB} angle}{2}$
- Flux Variability Analysis (FVA) min/max span evaluation

---

## 🗄️ Key Biological Databases & Software Tools
- Databases: BioModels Database, KEGG Pathways, Reactome, STRING, BiGG Models
- Tools: COBRApy, Tellurium, COPASI, NetworkX, Cytoscape

---

## 🚀 Research Milestones & Implementation Tasks
- [ ] Milestone 1: Model enzymatic cascade oscillation using ODE numerical solvers in SciPy
- [ ] Milestone 2: Construct an FBA linear program finding optimal growth flux and essential gene knockouts
- [ ] Milestone 3: Implement disease module detection on human PPI networks using random walk with restart (RWR)

---

## 📂 Subdirectory Architecture
```text
08-Systems-Biology/
├── README.md               # Curriculum roadmap & theoretical formulation
├── notebooks/              # Exploratory analysis & interactive notebooks
├── src/                    # Tested, production-ready scientific code
│   ├── __init__.py
│   └── biochemical_network_ode.py
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
