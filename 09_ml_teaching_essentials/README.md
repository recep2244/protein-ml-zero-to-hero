# Module 09 — ML Teaching Essentials
This module teaches you to diagnose, explain, and fix ML models — covering the bias-variance tradeoff, learning curves, calibration, and a systematic diagnostic checklist applicable to every model in the curriculum.

## What You'll Learn
- Decompose prediction error into bias, variance, and irreducible noise using the bias-variance decomposition
- Generate and interpret learning curves to distinguish underfitting from overfitting at a glance
- Use validation curves to tune hyperparameters systematically rather than by guesswork
- Evaluate and fix model calibration using reliability diagrams, temperature scaling, and Platt scaling
- Apply a structured diagnostic checklist when a model underperforms in production
- Explain ML concepts clearly — a skill essential for technical interviews and collaborative research

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Supervised ML (train/val/test, cross-validation, metrics) | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| Neural network training loops and loss curves | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| Basic probability and statistics | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_model_diagnostics.ipynb` | Bias-variance decomposition, learning curves, validation curves, calibration plots, Platt scaling, diagnostic checklist | ~6h |

## After This Module You Can
- Plot a learning curve and immediately identify whether a model needs more data or reduced complexity
- Produce a calibrated probability output from any classifier using temperature scaling or Platt scaling
- Systematically debug a poorly performing model using a structured checklist rather than trial and error
- Explain the bias-variance tradeoff with concrete biological examples (gene expression p>>n as high-variance case)
- Communicate model failures and their root causes clearly in a technical interview

## Key Concepts Introduced
- **Bias-variance tradeoff**: Decomposition of generalization error into bias (systematic error from wrong model assumptions) and variance (sensitivity to training data fluctuations).
- **Learning curve**: Plot of training and validation performance vs training set size; converging at high error signals high bias, large gap signals high variance.
- **Validation curve**: Plot of train/validation error vs a hyperparameter; reveals the underfitting-to-overfitting transition as complexity grows.
- **Calibration**: Property where predicted confidence scores match empirical outcome frequencies; a well-calibrated model's 70% predictions are correct 70% of the time.
- **Platt scaling**: Post-hoc calibration technique that fits a logistic regression on top of raw model outputs to produce reliable probability estimates.
- **Reliability diagram**: Calibration visualization that plots mean predicted probability vs actual fraction of positives across confidence bins.

## Next Module
→ [Module 10 — OpenFold3 Fine-Tuning (Capstone)](../10_openfold3_finetuning/README.md)

## Difficulty: ⭐⭐ (1–5 stars)
## Estimated Time: 6–8 hours
