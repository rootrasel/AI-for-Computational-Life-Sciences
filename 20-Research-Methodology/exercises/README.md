# Module 20 Exercises: Research Methodology

### Exercise 20.1: MMseqs2 Homology-Aware Splitter & Data Leakage Audit
- **Objective**: Take a dataset of 5,000 protein sequences and compare a random 80/20 train/test split against an MMseqs2 30% identity cluster-split.
- **Task**: Measure performance inflation on the random split caused by sequence homology leakage.

### Exercise 20.2: Conformal Prediction Set Evaluator for Virtual Screening
- **Objective**: Implement split conformal prediction for molecular classification (active vs inactive) outputting prediction sets $\{0\}$, $\{1\}$, or $\{0, 1\}$.
- **Task**: Measure set size efficiency and coverage across out-of-distribution Bemis-Murcko scaffold test sets.
