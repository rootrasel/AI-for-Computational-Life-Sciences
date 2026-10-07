# Module 12 Exercises: Structural Bioinformatics

### Exercise 12.1: TM-score Implementation & Evaluation
- **Objective**: Implement Zhang & Skolnick (2004) TM-score with length scale factor $d_0(L) = 1.24 \sqrt[3]{L - 15} - 1.8$.
- **Validation**: Compare structural similarity across homologous and non-homologous AlphaFold2 predictions.

### Exercise 12.2: Backbone Ramachandran ($\phi, \psi$) Parser
- **Objective**: Parse a multi-chain PDB file, compute the $(\phi, \psi)$ dihedral angles for each non-terminal residue using vector plane projections, and generate a 2D scatter plot colored by secondary structure.
