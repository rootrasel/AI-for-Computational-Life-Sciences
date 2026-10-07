# Module 06 Exercises: Metabolomics

### Exercise 6.1: Probabilistic Quotient Normalization & Partial Least Squares Discriminant Analysis (PLS-DA)
- **Objective**: Implement PLS-DA with cross-validation ($Q^2$ and $R^2$) to identify discriminating biomarkers between diseased and control metabolomic profiles.
- **Task**: Compute Variable Importance in Projection (VIP) scores and report top candidate biomarkers with VIP > 1.5.

### Exercise 6.2: Molecular Networking GNPS Clusterer
- **Objective**: Given a set of MS/MS spectra, calculate modified cosine scores accounting for neutral precursor losses.
- **Task**: Build a NetworkX graph with cosine threshold 0.7 and identify chemical subfamilies via Louvain community detection.
