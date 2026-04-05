# Module 06 — Structural ML & GNNs
This module bridges 3D protein structure and deep learning by teaching you to represent proteins as graphs and train geometric neural networks — the foundation for AlphaFold3's Pairformer and SE(3)-equivariant models.

## What You'll Learn
- Represent a protein structure as a graph: nodes (residues/atoms), edges (spatial neighbors), and node/edge features
- Implement message passing neural networks (MPNNs) from scratch in PyTorch
- Use PyTorch Geometric (PyG) and DGL for scalable graph learning on protein datasets
- Understand equivariance and invariance under 3D rotations and translations (SE(3) symmetry)
- Build E(3)-equivariant graph neural networks for structure-sensitive tasks
- Train a GNN for protein property prediction (stability, binding affinity, fold classification)
- Implement graph-level pooling strategies: mean, sum, hierarchical, attention-weighted

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PDB parsing and coordinate manipulation | `03_protein_structural_biology/01_structure_analysis.ipynb` |
| PyTorch `nn.Module` and training loops | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| Attention mechanisms | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| Basic graph theory (nodes, edges, adjacency matrix) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_structure_ml.ipynb` | Protein graph construction, node/edge features, MPNN implementation, protein property prediction | ~7h |
| 2 | `02_gnn_deep_dive.ipynb` | Equivariance vs invariance, SE(3)/E(3) networks, EGNN, frame-based representations, benchmarks | ~8h |

## After This Module You Can
- Convert any PDB structure into a PyG/DGL graph with biologically meaningful features
- Implement a message passing layer from the mathematical definition to working PyTorch code
- Explain why SE(3) equivariance matters for 3D molecular learning and how to enforce it
- Train a GNN for protein stability prediction and evaluate its generalization across protein families
- Describe the architectural connection between protein MPNNs and AlphaFold3's Pairformer

## Key Concepts Introduced
- **Message passing**: Iterative scheme where each node aggregates feature vectors from its neighbors to update its representation.
- **SE(3) equivariance**: Property where a model's output transforms predictably (rotates/translates) when the input structure is rotated/translated.
- **EGNN (E(n) Equivariant GNN)**: Architecture that maintains equivariant coordinate updates using relative distance and direction features.
- **Graph-level pooling**: Aggregation operation (mean, sum, attention) that reduces per-node embeddings to a single graph-level representation.
- **Frame-based representation**: Encoding local geometry as a rigid body frame (rotation + translation) attached to each residue, used in AlphaFold and ESMFold.
- **collate_graphs**: Custom PyTorch DataLoader collation function that batches variable-sized protein graphs into a single disconnected graph.

## Next Module
→ [Module 07 — AlphaFold3 Core](../07_alphafold3_core/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 15–20 hours
