# Module 10 — OpenFold3 Fine-Tuning (Capstone)
This module is where the curriculum converges — you navigate the OpenFold3 codebase, implement backbone rigid body math, and apply LoRA fine-tuning to predict mutation stability (deltadeltaG) and model TCR-pMHC interactions at Isomorphic Labs research depth.

## What You'll Learn
- Navigate a production-scale protein ML codebase (OpenFold3, 1M+ lines) using a structured map
- Implement backbone rigid body frames (SimpleRigid) and coordinate transforms from scratch
- Understand how FAPE loss uses backbone frames rather than global coordinates
- Apply LoRA to fine-tune a Pairformer model with dramatically fewer trainable parameters
- Build a deltadeltaG prediction head on top of fine-tuned structure embeddings
- Model TCR-pMHC multi-chain complexes as a drug discovery application
- Design a fine-tuning strategy when labeled data is scarce (< 500 examples)

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Transformer architecture and attention | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| LoRA concept and implementation | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| AlphaFold3 full architecture (Pairformer, FAPE, diffusion) | `07_alphafold3_core/` (all 6 notebooks) |
| Rigid body math, RMSD, Kabsch | `03_protein_structural_biology/01_structure_analysis.ipynb` |
| SE(3) equivariance and GNN message passing | `06_structural_ml_gnns/02_gnn_deep_dive.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 0 | `00_openfold3_walkthrough.ipynb` | Codebase navigation guide, SimpleRigid frames, backbone coordinate transforms, triangle attention implementation | ~6h |
| 1 | `01_protein_structure_finetuning.ipynb` | LoRA fine-tuning Pairformer, deltadeltaG prediction, SKEMPI dataset, TCR-pMHC modeling, low-data strategy | ~8h |

## After This Module You Can
- Open the OpenFold3 repository and immediately locate Pairformer, rigid utils, FAPE loss, and the data pipeline
- Implement LoRA adapters for any linear layer in a large model and verify parameter count reductions
- Fine-tune a structure prediction model on a small thermodynamics dataset with proper train/val splits
- Explain the relationship between backbone frames, FAPE loss, and SE(3) equivariance in an interview
- Design a TCR-pMHC binding prediction pipeline from AF3 multi-chain inference to affinity scoring

## Key Concepts Introduced
- **Backbone frame**: Local coordinate system (N-Ca-C triangle) attached to each residue; enables SE(3)-equivariant geometry reasoning.
- **FAPE (Frame-Aligned Point Error)**: Structure quality loss that measures atom position errors in each residue's local frame, decoupling accuracy from global orientation.
- **LoRA (Low-Rank Adaptation)**: Parameter-efficient fine-tuning that injects low-rank matrices (rank r << d) into frozen weight layers, typically reducing trainable params by 99%.
- **deltadeltaG**: Free energy change upon mutation (deltaG_mutant - deltaG_wildtype); negative values indicate stabilizing mutations.
- **SKEMPI**: Structural Kinetics and Energetics of Mutant Protein Interactions — benchmark dataset of ~7,000 measured binding affinity changes.
- **TCR-pMHC**: T-cell receptor / peptide-MHC complex — the molecular target for cancer immunotherapy; modeled as a multi-chain AF3 input.

## Next Module
→ [Module 11 — Membrane Protein Dynamics](../11_membrane_protein_dynamics/README.md)

## Difficulty: ⭐⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 14–18 hours
