# Module 11 — Membrane Protein Dynamics
This module applies structural ML to the most pharmacologically important protein class — membrane proteins — covering TM topology prediction, GPCR modeling, conformational dynamics, and membrane-specific fine-tuning strategies.

## What You'll Learn
- Predict transmembrane topology (inside-out orientation, TM helix count) using DeepTMHMM-style models
- Fine-tune ESM2 with LoRA specifically for membrane protein function prediction
- Model GPCR conformational states (active vs inactive) and their drug relevance
- Simulate conformational dynamics using coarse-grained MD and ML potentials
- Build conformational variational autoencoders (VAEs) for sampling alternate GPCR states
- Use OPM/GPCRdb databases effectively for membrane protein research
- Understand why AF3 struggles with membrane proteins and how to mitigate it
- Apply hybrid CG-MD + ML approaches for long-timescale conformational modeling

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PDB parsing, Kabsch, TM-score | `03_protein_structural_biology/01_structure_analysis.ipynb` |
| GNN message passing for proteins | `06_structural_ml_gnns/01_structure_ml.ipynb` |
| LoRA fine-tuning strategy | `10_openfold3_finetuning/01_protein_structure_finetuning.ipynb` |
| AF3 architecture basics | `07_alphafold3_core/01_af3_architecture.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_membrane_protein_dynamics.ipynb` | TM topology, ESM2 LoRA fine-tuning, GPCR conformational modeling, conformational VAE, CG-MD + ML hybrid potentials | ~8h |
| 2 | `02_md_simulation_basics.ipynb` | Verlet integrator, force field basics, periodic boundary conditions, ML potentials (ANI, MACE), NequIP | ~6h |

## After This Module You Can
- Predict transmembrane topology for any membrane protein sequence with confidence
- Fine-tune a protein language model for membrane-specific tasks (ion selectivity, GPCR class prediction)
- Explain why ~60% of approved drugs target membrane proteins and the computational challenges this creates
- Set up a coarse-grained MD simulation with ML-augmented force fields
- Sample GPCR conformational states using a trained VAE and interpret their pharmacological relevance

## Key Concepts Introduced
- **Transmembrane topology**: The arrangement of a membrane protein relative to the lipid bilayer — how many helices cross the membrane and which loops face inside/outside the cell.
- **GPCR**: G protein-coupled receptor — largest druggable protein family (~800 human GPCRs), responsible for signal transduction across cell membranes.
- **Coarse-grained MD**: Molecular dynamics simulation where groups of atoms are represented as single beads, enabling microsecond-to-millisecond timescales.
- **ML potential**: Neural network trained to predict energy and forces on atomic coordinates, replacing classical force fields with quantum-accuracy predictions.
- **Conformational VAE**: Variational autoencoder trained on MD trajectory frames to learn a low-dimensional latent space of protein conformational states.
- **OPM database**: Orientations of Proteins in Membranes — curated database providing spatial orientation and hydrophobic thickness for 9,000+ membrane protein structures.

## Next Module
→ [Module 12 — Generative Models](../12_generative_models/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 14–18 hours
