# Module 04 Exercises: Transcriptomics & RNA-Seq Analysis

### Exercise 4.1: End-to-End DESeq2 Python Implementation (PyDESeq2 Replication)
- **Objective**: Implement the negative binomial dispersion curve fitting algorithm.
- **Steps**:
  1. Fit gene-wise dispersion estimates $lpha_i$ via maximum likelihood.
  2. Fit parametric curve $lpha(\mu) = a_0 + a_1 / \mu$.
  3. Shrink gene-wise dispersions toward the curve using Empirical Bayes maximum a posteriori (MAP).
  4. Perform Wald tests for differential expression between treatment and control cohorts.

### Exercise 4.2: Fast GSEA Algorithm Implementation
- **Objective**: Implement Subramanian et al. (2005) Gene Set Enrichment Analysis running sum calculation.
- **Task**: Vectorize running sum calculations across $K=1,000$ MSigDB pathways and compute empirical $p$-values via sample permutation.
