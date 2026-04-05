# Module 13 — Bayesian Methods & Uncertainty Quantification
This module teaches you to quantify, communicate, and act on uncertainty in ML predictions — covering Bayesian inference, MCMC, Gaussian processes, conformal prediction, and Bayesian optimization for experimental design.

## What You'll Learn
- Apply Bayes' rule for posterior inference and understand credible intervals vs frequentist confidence intervals
- Implement Metropolis-Hastings MCMC and diagnose chain convergence (R-hat, trace plots)
- Build Gaussian process regression models with custom kernels for protein property prediction
- Implement MC Dropout as a simple approximate Bayesian neural network
- Apply conformal prediction to get finite-sample coverage guarantees on any model
- Use Bayesian optimization (Expected Improvement, GP-UCB) to design efficient experimental campaigns
- Recognize and distinguish epistemic from aleatoric uncertainty in biological data

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Probability theory: Bayes rule, distributions, MLE | `00_python_ml_basics/08_mathematical_foundations.ipynb` |
| Neural network training and dropout | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| Gaussian process intuition (optional but helpful) | `00_python_ml_basics/09_classical_ml_advanced.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_bayesian_ml_uncertainty.ipynb` | Conjugate priors, Metropolis-Hastings MCMC, Gaussian processes, MC Dropout, conformal prediction, Bayesian optimization, uncertainty decomposition | ~8h |

## After This Module You Can
- Distinguish epistemic uncertainty (model ignorance) from aleatoric uncertainty (data noise) and quantify both
- Build a Gaussian process model with a protein-appropriate kernel and extract calibrated confidence bands
- Wrap any pretrained model with conformal prediction to get statistically valid coverage guarantees
- Design a Bayesian optimization loop for directed evolution or drug screening campaigns
- Explain why AlphaFold3's pLDDT score is a confidence signal but not a calibrated probability

## Key Concepts Introduced
- **Bayesian inference**: Update of prior beliefs to posterior beliefs using observed data via Bayes' theorem: P(theta|data) proportional to P(data|theta) * P(theta).
- **Credible interval**: Bayesian interval containing the true parameter with specified posterior probability; interpretable as "there is a 95% chance theta is in this range."
- **MCMC (Markov Chain Monte Carlo)**: Family of algorithms that sample from complex posteriors by constructing a Markov chain whose stationary distribution equals the target.
- **Gaussian process**: Non-parametric probabilistic model that defines a prior over functions; predictions are Gaussian distributions with mean and variance at every input.
- **MC Dropout**: Approximate Bayesian inference technique that runs inference with dropout active multiple times and treats the resulting sample distribution as a posterior.
- **Conformal prediction**: Distribution-free uncertainty quantification framework providing finite-sample coverage guarantees under exchangeability alone.
- **Epistemic uncertainty**: Model uncertainty due to lack of data or knowledge; can in principle be reduced by collecting more data.
- **Aleatoric uncertainty**: Irreducible noise inherent in the data-generating process; cannot be reduced by collecting more data.

## Next Module
→ [Module 14 — Reinforcement Learning](../14_reinforcement_learning/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
