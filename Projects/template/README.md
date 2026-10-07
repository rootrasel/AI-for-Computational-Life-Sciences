# Research Project Template

A cookiecutter-style, publication-grade directory template for machine learning in the computational life sciences.

## Directory Structure
```text
template/
├── configs/
│   ├── config.yaml              # General pipeline execution parameters
│   └── model_params.yaml        # Model hyperparameters and training configs
├── data/
│   ├── raw/                     # Original, immutable raw downloads
│   ├── interim/                 # Intermediate filtered/preprocessed tensors
│   ├── processed/               # Final training/testing splits
│   └── README.md                # Data documentation & FAIR metadata
├── notebooks/
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_model.ipynb
│   └── 04_evaluation_and_interpretability.ipynb
├── pipelines/
│   └── workflow.smk             # Snakemake workflow orchestrator
├── reports/
│   ├── figures/                 # Publication-ready SVG/PDF figures
│   └── manuscript_template.md   # Paper draft outline
├── src/
│   ├── __init__.py
│   ├── data_loader.py           # Dataset loaders with leakage-free splitting
│   ├── features.py              # Biological feature extractors
│   ├── model.py                 # PyTorch model architecture definitions
│   ├── train.py                 # Training loops with early stopping
│   ├── evaluate.py              # Benchmark evaluation metrics
│   └── utils.py                 # Random seeds, logging, hardware config
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py         # Unit tests for data shapes and models
└── pyproject.toml               # Project build configuration
```
