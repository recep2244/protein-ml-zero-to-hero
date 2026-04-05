# Module 16 — MLOps & Deployment
This module teaches you to ship everything built in Modules 00–15 — experiment tracking, model checkpointing, REST API serving, Docker containerization, data drift detection, and CI/CD pipelines for production protein ML systems.

## What You'll Learn
- Track experiments reproducibly with MLflow: log parameters, metrics, artifacts, and register models
- Implement robust model checkpointing with top-K retention and metadata-rich checkpoint files
- Serve a protein ML model as a REST API using FastAPI, Pydantic, and uvicorn
- Containerize a GPU-enabled ML service with Docker and docker-compose
- Detect data drift in production using Kolmogorov-Smirnov tests and visualize drift signals
- Build CI/CD pipelines with GitHub Actions including model regression tests
- Understand train-serve skew and how to prevent it in production systems
- Apply seed management, config dataclasses, and data checksums for full reproducibility

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PyTorch model classes, state_dict, optimizers | `00_python_ml_basics/06_pytorch_fundamentals.ipynb` |
| ML metrics and train/val/test evaluation | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| A trained model to deploy (any from Modules 05–15) | Prior modules |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_mlops_for_protein_ml.ipynb` | MLflow experiment tracking, reproducibility, checkpointing, FastAPI serving, Docker, data drift detection (KS test), GitHub Actions CI/CD | ~8h |

## After This Module You Can
- Log a complete experiment run (hyperparams, metrics, model artifact) to MLflow in under 10 lines of code
- Build a FastAPI endpoint that accepts a protein sequence and returns a prediction with latency logging
- Write a Dockerfile for a GPU-enabled PyTorch service and run it with docker-compose
- Detect when production input data has drifted from training data and trigger a retraining alert
- Set up a GitHub Actions workflow that runs model regression tests on every pull request

## Key Concepts Introduced
- **Train-serve skew**: Discrepancy between the data distribution seen during training and the data encountered at inference time; the most common cause of silent production failures.
- **Model registry**: Central catalog (MLflow, W&B, SageMaker) that versions, stages, and tracks production model artifacts with metadata.
- **Data drift**: Statistical shift in the distribution of input features between training time and production; detected using hypothesis tests (KS test, PSI) on feature distributions.
- **Champion-challenger**: Deployment strategy where a new model (challenger) is evaluated against the current production model (champion) on live traffic before full rollout.
- **Pydantic**: Python library for data validation using type annotations; used in FastAPI to validate and serialize API request/response schemas.
- **KS test (Kolmogorov-Smirnov)**: Non-parametric statistical test measuring the maximum absolute difference between two empirical cumulative distribution functions; used for drift detection.

## Next Module
→ [Module 17 — Capstone Project](../17_capstone_project/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
