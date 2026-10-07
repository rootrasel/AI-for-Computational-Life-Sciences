# Snakemake workflow for reproducible research pipeline

rule all:
    input:
        "reports/figures/evaluation_benchmark.png",
        "reports/metrics_summary.json"

rule preprocess_data:
    input:
        raw_data="data/raw/dataset.parquet"
    output:
        train="data/processed/train.parquet",
        val="data/processed/val.parquet",
        test="data/processed/test.parquet"
    params:
        config="configs/config.yaml"
    shell:
        "python src/data_loader.py --config {params.config}"

rule train_model:
    input:
        train="data/processed/train.parquet",
        val="data/processed/val.parquet"
    output:
        checkpoint="models/best_model.pt"
    params:
        model_config="configs/model_params.yaml"
    shell:
        "python src/train.py --model_config {params.model_config}"

rule evaluate_model:
    input:
        checkpoint="models/best_model.pt",
        test="data/processed/test.parquet"
    output:
        plot="reports/figures/evaluation_benchmark.png",
        metrics="reports/metrics_summary.json"
    shell:
        "python src/evaluate.py --checkpoint {input.checkpoint} --test_data {input.test}"
