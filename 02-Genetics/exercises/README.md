# Module 02 Exercises: Genetics & Population Genomics

### Exercise 2.1: GWAS Association Scanner & QQ/Manhattan Plot Engine
- **Objective**: Implement a vectorized GWAS linear association engine for $N=5,000$ individuals across $M=50,000$ SNPs.
- **Requirements**:
  1. Add covariates (first 5 genotype principal components and age/sex).
  2. Compute genomic inflation factor $\lambda_{GC} = rac{	ext{median}(\chi^2)}{0.455}$.
  3. Export publication-quality Manhattan and QQ plots with bonferroni significance line ($p = 5 	imes 10^{-8}$).

### Exercise 2.2: LD-Clumping & Thresholding (C+T) PRS Evaluator
- **Objective**: Given a PLINK LD matrix and GWAS summary statistics, implement greedy LD clumping ($r^2 < 0.1$, window $250	ext{ kb}$) across $p$-value thresholds $[10^{-8}, 10^{-6}, 10^{-4}, 10^{-2}, 0.1, 1.0]$.
- **Evaluation**: Assess incremental $R^2$ and AUC on held-out phenotype simulation.
