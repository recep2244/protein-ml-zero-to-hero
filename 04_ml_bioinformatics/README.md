# Module 04 — ML for Omics
This module applies machine learning to high-dimensional biological data — RNA-seq tumor classification, the p>>n problem, survival analysis, and multi-omics integration — bridging classical ML and modern bioinformatics.

## What You'll Learn
- Handle the p>>n (features >> samples) regime that dominates genomics and proteomics datasets
- Apply PCA and other dimensionality reduction methods to RNA-seq expression matrices
- Build and evaluate classifiers (logistic regression, random forests, SVMs) for cancer subtype prediction
- Implement survival analysis with Kaplan-Meier curves and Cox proportional hazards models
- Integrate multi-omics data layers (transcriptomics, methylation, copy-number variation)
- Apply cross-validation correctly in high-dimensional settings to avoid information leakage
- Interpret feature importances in biological context (which genes drive predictions)

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| scikit-learn pipelines and classification metrics | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| Advanced classical ML (random forests, SVMs, PCA) | `00_python_ml_basics/09_classical_ml_advanced.ipynb` |
| RNA-seq data processing and normalization | `02_genomics_gene_analysis/02_rnaseq_analysis.ipynb` |
| PDB-level intuition for protein features | `03_protein_structural_biology/01_structure_analysis.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_ml_for_omics.ipynb` | p>>n problem, PCA on RNA-seq, tumor subtype classification, survival analysis, Cox models, feature selection, multi-omics integration | ~8h |

## After This Module You Can
- Preprocess and normalize a raw RNA-seq count matrix for ML
- Build a tumor classifier and evaluate it with nested cross-validation to avoid data leakage
- Plot and interpret Kaplan-Meier survival curves and log-rank test results
- Fit a Cox proportional hazards model and extract prognostic gene signatures
- Explain why standard ML practices break down in the p>>n regime and how to fix them

## Key Concepts Introduced
- **p>>n problem**: The regime where feature count (genes) far exceeds sample count, causing overfitting and spurious correlations.
- **Nested cross-validation**: Cross-validation with an inner loop for hyperparameter selection and an outer loop for unbiased error estimation.
- **Kaplan-Meier estimator**: Non-parametric method that estimates the survival function from censored time-to-event data.
- **Cox proportional hazards**: Semi-parametric regression model relating covariates to hazard ratios in survival analysis.
- **Feature leakage**: Contamination of training data with test-set information, leading to optimistically biased performance estimates.
- **Multi-omics integration**: Combining multiple molecular measurement layers (e.g., RNA + methylation + CNV) to improve biological insight and predictive power.

## Next Module
→ [Module 05 — Deep Learning & Fine-Tuning](../05_deep_learning_finetuning/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
