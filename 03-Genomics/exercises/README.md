# Module 03 Exercises: High-Throughput Genomics & Variant Calling

### Exercise 3.1: Burrows-Wheeler Transform & FM-Index Exact Aligner
- **Objective**: Implement the Burrows-Wheeler Transform (BWT) of a reference genome sequence alongside the suffix array and FM-Index $Occ(c, k)$ table.
- **Task**: Implement $O(|P|)$ exact pattern search for Illumina sequencing reads of length 150 bp against a synthetic bacterial genome (1 Mbp).

### Exercise 3.2: Convolutional Pileup Variant Classifier (Mini-DeepVariant)
- **Objective**: Build a PyTorch CNN that takes a 6-channel pileup tensor:
  1. Base identity (A, C, G, T)
  2. Base quality score
  3. Mapping quality
  4. Strand orientation (forward / reverse)
  5. Read support for insertion / deletion
  6. Variant candidate indicator
- **Task**: Train and evaluate the model to classify genotype: `HOM_REF` (0/0), `HET` (0/1), or `HOM_ALT` (1/1).
