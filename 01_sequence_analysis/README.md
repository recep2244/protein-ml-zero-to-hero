# Module 01 — Sequence Analysis
This module covers the algorithmic and statistical foundations of biological sequence analysis, from pairwise alignment to hidden Markov models and 45 Rosalind problem solutions.

## What You'll Learn
- Implement Needleman-Wunsch (global) and Smith-Waterman (local) alignment from scratch
- Understand BLOSUM62 and PAM substitution matrices and when to use each
- Solve 45 Rosalind.info problems spanning DNA, RNA, protein, and combinatorics
- Work with advanced alignment techniques: affine gap penalties, multiple sequence alignment
- Build phylogenetic trees using distance and parsimony methods
- Tackle genome assembly and mass spectrometry sequence problems
- Model biological sequences with Hidden Markov Models (Viterbi, forward-backward)

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Python proficiency (loops, dicts, recursion) | `00_python_ml_basics/01_python_core_for_bioinformatics.ipynb` |
| NumPy array operations | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| Basic probability (conditional probability, Bayes) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_alignment_algorithms.ipynb` | NW, SW, affine gaps, BLOSUM62, PAM, pairwise statistics | ~5h |
| 2 | `02_rosalind_complete.ipynb` | 45 core Rosalind problems (DNA, RNA, protein, combinatorics) | ~8h |
| 3 | `03_rosalind_combinatorics_strings.ipynb` | Advanced string algorithms, suffix arrays, BWT, k-mers | ~4h |
| 4 | `04_rosalind_alignment_advanced.ipynb` | Semiglobal, overlap, profile alignment, scoring variations | ~4h |
| 5 | `05_rosalind_phylogeny.ipynb` | UPGMA, neighbor-joining, parsimony, Newick format | ~4h |
| 6 | `06_rosalind_assembly_massspec.ipynb` | De Bruijn graphs, Eulerian paths, peptide sequencing | ~4h |
| 7 | `07_hidden_markov_models.ipynb` | HMM theory, Viterbi, forward-backward, Baum-Welch | ~5h |

## After This Module You Can
- Implement global and local pairwise alignment with custom scoring matrices
- Solve the full Rosalind bioinformatics textbook problem set programmatically
- Build phylogenetic trees from distance matrices and interpret them biologically
- Design and train Hidden Markov Models for gene finding and profile alignment
- Explain the algorithmic complexity and tradeoffs of each alignment method

## Key Concepts Introduced
- **Dynamic programming**: Algorithmic paradigm that breaks alignment into overlapping subproblems, enabling O(mn) solutions.
- **BLOSUM62**: Log-odds substitution matrix derived from aligned blocks of sequences with 62% identity.
- **Viterbi algorithm**: Dynamic programming method that finds the most likely hidden state sequence in an HMM.
- **De Bruijn graph**: Directed graph where k-mers are edges, used for genome assembly from short reads.
- **Affine gap penalty**: Gap scoring model (open + extend costs) that discourages many short gaps over one long gap.

## Next Module
→ [Module 02 — Genomics & Gene Analysis](../02_genomics_gene_analysis/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 34–38 hours
