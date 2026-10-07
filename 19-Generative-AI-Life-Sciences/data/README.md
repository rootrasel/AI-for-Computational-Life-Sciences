# Data Dictionary & Provenance: Generative AI for Life Sciences

### Directory Policy
- `raw/`: Immutable raw downloads (FASTQ, BAM, VCF, PDB, mzML, H5AD). Ignored by git.
- `processed/`: Sanitized, normalized, and benchmark-ready matrices, features, and tensors.

### Standards & FAIR Compliance
- **Findable**: Document NCBI BioProject, SRA accession IDs, UniProt IDs, or Zenodo DOIs.
- **Accessible**: Provide deterministic automated download scripts (`download_data.sh`).
- **Interoperable**: Store structured representations in standard open formats (`.parquet`, `.h5ad`, `.zarr`).
- **Reusable**: Retain provenance logs, parameter manifests, and licensing records.
