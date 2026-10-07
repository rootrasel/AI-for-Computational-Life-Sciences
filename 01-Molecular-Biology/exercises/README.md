# Module 01 Exercises: Molecular Biology for AI/ML

### Exercise 1.1: SantaLucia Nearest-Neighbor Free Energy ($\Delta G$) Engine
- **Objective**: Implement SantaLucia (1998) 10-pair nearest-neighbor thermodynamic model for DNA duplexes including initiation and terminal A-T penalties.
- **Input**: Target 20-mer oligonucleotide and complementary probe.
- **Deliverable**: Return $\Delta H^\circ$, $\Delta S^\circ$, $\Delta G_{37}^\circ$, and exact $T_m$ given user-specified salt concentration $[Na^+]$ and oligonucleotide concentration.

### Exercise 1.2: Codon Optimization & Secondary Structure Minimization
- **Objective**: Write an algorithm that takes a target protein sequence and designs an mRNA sequence that simultaneously:
  1. Maximizes the Codon Adaptation Index (CAI) for human expression ($Homo\ sapiens$).
  2. Avoids stable hairpin stems ($\Delta G < -15\ 	ext{kcal/mol}$) near the ribosome binding site / Kozak consensus.
- **Evaluation**: Compare with wild-type sequences on synthetic expression benchmarks.
