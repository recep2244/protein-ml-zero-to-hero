# Module 03 — Protein Structural Biology
This module introduces 3D protein structure — how to parse PDB files, measure structural similarity, superimpose structures, and validate geometry — providing the physical intuition that underpins every AlphaFold module ahead.

## What You'll Learn
- Parse PDB/mmCIF files with Biopython and extract atomic coordinates, chain information, and residue metadata
- Compute Cα RMSD between two structures and understand its limitations
- Implement the Kabsch algorithm to find the optimal rigid-body superposition of two point clouds
- Calculate and interpret TM-score as a length-normalized structural similarity metric
- Generate Ramachandran plots and identify allowed/disallowed backbone torsion angle regions
- Understand secondary structure elements (helices, strands, loops) and their geometric definitions
- Visualize 3D protein structures and contact maps programmatically

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Python and NumPy (matrix operations, SVD) | `00_python_ml_basics/01_python_core_for_bioinformatics.ipynb` |
| Basic molecular biology (amino acids, peptide bonds) | `01_sequence_analysis/01_alignment_algorithms.ipynb` |
| Linear algebra (rotation matrices, dot products) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_structure_analysis.ipynb` | PDB parsing, RMSD, Kabsch algorithm, TM-score, Ramachandran plots, contact maps, secondary structure | ~8h |

## After This Module You Can
- Load any PDB structure and extract the Cα coordinate matrix for downstream computation
- Superimpose two protein structures optimally using the Kabsch algorithm
- Distinguish RMSD from TM-score and choose the right metric for a given comparison
- Interpret a Ramachandran plot and identify problematic residues in a model
- Build a residue contact map and relate it to the protein's 3D fold

## Key Concepts Introduced
- **RMSD (Root Mean Square Deviation)**: Average Euclidean distance between paired atomic positions after optimal superposition; sensitive to outliers.
- **Kabsch algorithm**: SVD-based method to compute the rotation matrix minimizing RMSD between two aligned coordinate sets.
- **TM-score**: Length-normalized structural similarity score (0–1) that weights close residue pairs more heavily than distant ones.
- **Ramachandran plot**: 2D scatter plot of backbone phi (φ) and psi (ψ) dihedral angles; forbidden regions reveal steric clashes.
- **Contact map**: Binary or distance matrix encoding which residue pairs are spatially close (< 8 Å Cβ–Cβ distance); encodes fold topology.
- **mmCIF**: Modern macromolecular Crystallographic Information File format, preferred by PDB for large structures.

## Next Module
→ [Module 04 — ML for Omics](../04_ml_bioinformatics/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
