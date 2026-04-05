# Module 12 — Generative Models for Biology
This module covers diffusion models and flow matching for protein design — the generative approaches powering AlphaFold3's structure generation, RFdiffusion, and the broader shift from prediction to de novo design.

## What You'll Learn
- Implement DDPM (Denoising Diffusion Probabilistic Models) from scratch: forward process, reverse process, noise schedule
- Understand score matching and the connection between denoising and gradient estimation
- Apply DDIM for accelerated inference (fewer diffusion steps at test time)
- Understand how RFdiffusion adapts diffusion to protein backbone coordinate generation on SE(3)
- Implement flow matching as a more efficient alternative to diffusion for protein design
- Connect the pre-train → generate → filter → steer pipeline across modules 12–15
- Evaluate generated proteins: novelty, diversity, designability (self-consistency TM-score)

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PyTorch training loops and loss functions | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| AlphaFold3 diffusion module and SE(3) geometry | `07_alphafold3_core/01_af3_architecture.ipynb` |
| Basic probability theory (Gaussian distributions, KL divergence) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_diffusion_protein_design.ipynb` | DDPM theory, forward/reverse process, noise schedules, score matching, DDIM sampling, RFdiffusion architecture, SE(3) diffusion | ~8h |
| 2 | `02_connecting_modules_12_to_15.ipynb` | Unified pre-train → generate → filter → steer framework; connecting generative models to SSL, RL, and Bayesian optimization | ~4h |

## After This Module You Can
- Implement DDPM training and sampling in PyTorch from the mathematical definition
- Explain how RFdiffusion extends image diffusion to protein backbone coordinates in SE(3)
- Use DDIM to accelerate sampling by 10–50x with minimal quality loss
- Evaluate a set of generated protein backbones using designability and diversity metrics
- Place diffusion models in the context of the full protein design pipeline (generate, filter, optimize)

## Key Concepts Introduced
- **DDPM**: Denoising Diffusion Probabilistic Model — generative model that learns to reverse a gradual Gaussian noising process to recover data from noise.
- **Forward process**: Fixed Markov chain that gradually adds Gaussian noise to data over T timesteps until the distribution approaches N(0, I).
- **Reverse process**: Learned neural network that predicts the less-noisy version of a sample at each timestep, parameterized as a noise predictor (epsilon prediction).
- **Score matching**: Training objective equivalent to denoising that estimates the gradient of the log data density (score function).
- **DDIM**: Deterministic diffusion sampler that skips timesteps using a non-Markovian reverse process, enabling 10–50x faster inference than DDPM.
- **Flow matching**: Generative framework that learns a vector field transforming noise to data via optimal transport paths; simpler to train and faster to sample than diffusion.
- **Designability**: Self-consistency metric for generated protein backbones — how well ProteinMPNN + ESMFold can recover the original backbone from designed sequences.

## Next Module
→ [Module 13 — Bayesian Methods](../13_bayesian_methods/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 12–16 hours
