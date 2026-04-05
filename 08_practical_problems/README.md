# Module 08 — Practical Problems
This module is pure practice — HackerRank and Rosalind problems organized by computational topic — designed to sharpen your problem-solving speed and accuracy for timed assessments.

## What You'll Learn
- Solve string and DNA manipulation problems under time pressure (HackerRank-style)
- Apply dynamic programming to classic bioinformatics problems (LCS, edit distance, Viterbi)
- Implement graph algorithms for genome assembly (Eulerian paths, de Bruijn graphs)
- Use statistical reasoning to solve ML assessment problems (distributions, hypothesis tests, regression)
- Combine alignment and phylogeny skills in end-to-end multi-part problems
- Develop pattern recognition for problem types that recur across HackerRank certifications

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Python string and array manipulation | `00_python_ml_basics/01_python_core_for_bioinformatics.ipynb` |
| Dynamic programming (NW, SW) | `01_sequence_analysis/01_alignment_algorithms.ipynb` |
| Graph algorithms (BFS, DFS, topological sort) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |
| Basic ML and statistics | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| RNA-seq and genomic sequence concepts | `02_genomics_gene_analysis/01_genomics_core.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_strings_dna.ipynb` | DNA string manipulation, k-mers, GC content, reverse complement, motif finding | ~4h |
| 2 | `02_dynamic_programming.ipynb` | LCS, edit distance, coin change, Fibonacci variants, RNA secondary structure | ~5h |
| 3 | `03_graphs_assembly.ipynb` | De Bruijn graphs, Eulerian paths, BFS/DFS, genome assembly | ~5h |
| 4 | `04_statistics_ml_practical.ipynb` | Probability distributions, hypothesis testing, linear/logistic regression, confusion matrices | ~5h |
| 5 | `05_alignment_phylogeny.ipynb` | Integrated alignment + phylogeny problems, scoring edge cases, profile alignment | ~4h |

## After This Module You Can
- Complete HackerRank bioinformatics and ML domain problems consistently within time limits
- Identify the DP substructure of an unfamiliar optimization problem quickly
- Code de Bruijn graph construction and find Eulerian paths in under 20 minutes
- Solve HackerRank statistics and probability problems accurately using first principles
- Self-diagnose knowledge gaps after attempting a problem and find the right review notebook

## Key Concepts Introduced
- **Longest Common Subsequence (LCS)**: Classic DP problem that finds the longest subsequence shared by two strings; basis for diff tools and sequence alignment.
- **Edit distance**: Minimum number of insertions, deletions, and substitutions to transform one string into another (Levenshtein distance).
- **Eulerian path**: A trail in a graph that visits every edge exactly once; existence requires at most two vertices of odd degree.
- **k-mer spectrum**: Multiset of all length-k substrings of a sequence; encodes local composition and supports assembly and alignment-free comparison.
- **Fisher's exact test**: Statistical test for association in a 2x2 contingency table; preferred over chi-square when sample sizes are small.

## Next Module
→ [Module 09 — ML Teaching Essentials](../09_ml_teaching_essentials/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 23–28 hours
