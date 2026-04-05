# Module 07 — AlphaFold3 Core
This module is the centerpiece of the curriculum — a zero-to-hero walkthrough of AlphaFold3's full architecture, training pipeline, data processing, and evaluation, culminating in a complete training loop implementation.

## What You'll Learn
- Trace the full AlphaFold3 pipeline from MSA input to atomic coordinate output
- Implement Pairformer blocks: triangle multiplicative updates, triangle self-attention, and transition layers
- Understand FAPE (Frame-Aligned Point Error) as the core structure prediction loss
- Work with the AF3 data pipeline: MSA featurization, template search, cropping, and batching
- Implement diffusion-based structure generation (the Diffusion Module replacing Evoformer's recycling)
- Evaluate predictions: LDDT, TM-score, GDT-TS, per-residue confidence (pLDDT), PAE matrices
- Handle the Chemical Component Dictionary (CCD) for ligand and small molecule featurization
- Build and debug the full AF3 training loop with mixed-precision, gradient checkpointing, and EMA

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Attention mechanisms and Transformer blocks | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| SE(3)-equivariant representations and frames | `06_structural_ml_gnns/02_gnn_deep_dive.ipynb` |
| PDB parsing, RMSD, TM-score | `03_protein_structural_biology/01_structure_analysis.ipynb` |
| PyTorch training loops with schedulers | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 0 | `00_af3_zero_to_hero.ipynb` | Conceptual on-ramp, big-picture architecture, plain-English AF3 overview | ~3h |
| 1 | `01_af3_architecture.ipynb` | Pairformer, triangle attention, triangle multiplicative updates, diffusion module | ~8h |
| 2 | `02_af3_data_pipeline.ipynb` | MSA featurization, template search, cropping strategies, atom14/atom37 encoding | ~5h |
| 3 | `03_af3_evaluation.ipynb` | LDDT, TM-score, GDT-TS, pLDDT, PAE, DockQ, evaluation benchmarks | ~4h |
| 4 | `04_af3_fullscale_and_ccd.ipynb` | Full-scale inference, CCD ligand featurization, multi-chain assemblies | ~5h |
| 5 | `05_af3_training_loop.ipynb` | Full AF3 training loop, mixed precision, gradient checkpointing, EMA, curriculum sampling | ~7h |
| 6 | `06_af3_diffusion_deep_dive.ipynb` | AF3 noise schedule (σ(t)=t), trunk-conditioned denoising, self-conditioning, all-atom atom37, loss weighting (λ=1/σ²), all 5 confidence heads (pLDDT/PAE/pDE/pTM/ipTM), PDB clustering anti-leakage | ~6h |

## After This Module You Can
- Explain every major component of AlphaFold3's architecture in a technical interview
- Implement Pairformer blocks from the paper's pseudocode in PyTorch
- Featurize an MSA and template for AF3 input
- Compute FAPE loss and explain why it is superior to coordinate RMSD for training
- Build a complete structure prediction training loop with production-quality engineering practices

## Key Concepts Introduced
- **Pairformer**: AF3's core module that refines per-residue (single) and residue-pair (pair) representations using triangle operations and attention.
- **Triangle multiplicative update**: Operation that updates each pair (i,j) using a sum of outer products of paths through a third residue k, enforcing triangle inequality-like consistency.
- **FAPE (Frame-Aligned Point Error)**: Loss function measuring atom position errors in the local coordinate frame of each backbone rigid body, making it rotation-invariant and locally sensitive.
- **pLDDT**: Per-residue confidence metric (0–100) predicted by AF3; residues above 90 are highly confident, below 50 are likely disordered.
- **PAE (Predicted Aligned Error)**: Matrix of expected position errors when aligning on one residue; low off-diagonal values indicate confident inter-domain or inter-chain predictions.
- **Diffusion module**: Replaces AF2's recycled structure module with an iterative denoising process that generates all-atom coordinates from noisy samples.
- **AF3 noise schedule**: Variance-exploding schedule xₜ = x₀ + σ(t)·ε where σ(t)=t, distinct from DDPM's signal-shrinking schedule; enables stable all-atom denoising.
- **pDE (Predicted Distance Error)**: 5th AF3 confidence metric — alignment-free predicted error on inter-residue distances; complements PAE for non-sequential assemblies.
- **PDB clustering**: MMseqs2 at 40% sequence identity; train/val/test splits are made at cluster level (not sequence level) to prevent data leakage from homologous structures.

## Next Module
→ [Module 08 — Practical Problems](../08_practical_problems/README.md)

## Difficulty: ⭐⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 38–46 hours
