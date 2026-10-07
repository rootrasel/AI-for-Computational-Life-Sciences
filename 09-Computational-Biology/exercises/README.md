# Module 09 Exercises: Algorithmic Computational Biology

### Exercise 9.1: Gotoh Affine Gap Penalty Implementation
- **Objective**: Implement Gotoh (1982) three-matrix dynamic programming ($M, I_x, I_y$) for affine gap penalties ($u + v \cdot k$).
- **Benchmark**: Validate alignment against Biopython pairwise2 / Bio.Align across synthetic mutated sequences with long indel stretches.

### Exercise 9.2: Nussinov RNA Secondary Structure Dynamic Programming
- **Objective**: Implement the Nussinov DP algorithm maximizing Watson-Crick and Wobble (G-U) base pairs with minimum hairpin loop constraint ($l \ge 3$).
- **Output**: Return dot-bracket notation string (e.g. `((((...))))`).
