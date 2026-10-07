# Module 14 Exercises: Protein Engineering

### Exercise 14.1: ESM-2 Zero-Shot Mutation Scanner
- **Objective**: Load the pretrained `esm2_t6_8M_UR50D` or `esm2_t12_35M_UR50D` model from Hugging Face / fair-esm.
- **Task**: Compute masked marginal log-odds scores for all single amino acid substitutions (20 AA $	imes$ sequence length) of a GFP protein sequence and correlate with MaveDB experimental fluorescence.

### Exercise 14.2: In Silico Directed Evolution via Active Learning
- **Objective**: Implement a Bayesian optimization loop using Gaussian Process regression with Matérn kernel to optimize enzyme thermal stability within 5 rounds of 16-variant batches.
