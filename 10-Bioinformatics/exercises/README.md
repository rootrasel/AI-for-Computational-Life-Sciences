# Module 10 Exercises: Reproducible Bioinformatics

### Exercise 10.1: Snakemake NGS Alignment & QC Pipeline
- **Objective**: Write an automated Snakemake workflow taking paired-end FASTQ samples, running:
  1. FastQC quality check
  2. Trimmomatic adapter trimming
  3. BWA-MEM alignment to GRCh38
  4. Samtools sort and index
  5. MultiQC summary aggregation

### Exercise 10.2: Docker Containerization & Bioconda Recipe
- **Objective**: Write a minimal Dockerfile creating a secure, multi-stage image containing SAMtools, BCFtools, and Bedtools with non-root user permissions and verified entrypoint tests.
