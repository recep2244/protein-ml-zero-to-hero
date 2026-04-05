# HackerRank Bioinformatics & Structural Biology ML — Study Plan

## Goal
Score in top 10% on HackerRank ML + Bioinformatics assessments for structural biology roles.

This study plan is the **core 4-week sprint** inside a larger 39-notebook curriculum. The full repository now includes advanced extension modules for AlphaFold 3 internals, membrane proteins, diffusion models, Bayesian uncertainty, reinforcement learning for design, self-supervised protein representation learning, and MLOps for deployment.

Teaching note:
- This 4-week plan is the **minimum viable core path**, not the full research path.
- If you are new to ML, prioritize understanding over speed.
- Modules `11-16` are advanced electives and should not block progress through the core.

---

## Project Structure

```
hackerrank/
├── 00_python_ml_basics/
│   ├── 01_python_core_for_bioinformatics.ipynb   ← START HERE
│   ├── 02_ml_fundamentals.ipynb
│   ├── 03_hackerrank_all_modules.ipynb
│   ├── 04_hackerrank_python_track.ipynb
│   ├── 05_hackerrank_statistics_ml_tracks.ipynb
│   ├── 06_pytorch_fundamentals.ipynb
│   ├── 07_tensorflow_keras.ipynb
│   ├── 08_mathematical_foundations.ipynb
│   └── 09_classical_ml_advanced.ipynb
├── 01_sequence_analysis/
│   ├── 01_alignment_algorithms.ipynb
│   ├── 02_rosalind_complete.ipynb
│   ├── 03_rosalind_combinatorics_strings.ipynb
│   ├── 04_rosalind_alignment_advanced.ipynb
│   ├── 05_rosalind_phylogeny.ipynb
│   ├── 06_rosalind_assembly_massspec.ipynb
│   └── 07_hidden_markov_models.ipynb
├── 02_genomics_gene_analysis/
│   └── 01_genomics_core.ipynb
├── 03_protein_structural_biology/
│   └── 01_structure_analysis.ipynb
├── 04_ml_bioinformatics/
│   └── 01_ml_for_omics.ipynb
├── 05_deep_learning_finetuning/
│   └── 01_dl_and_finetuning.ipynb
├── 06_structural_ml_gnns/
│   ├── 01_structure_ml.ipynb
│   └── 02_gnn_deep_dive.ipynb
├── 07_alphafold3_core/
│   ├── 01_af3_architecture.ipynb
│   ├── 02_af3_data_pipeline.ipynb
│   ├── 03_af3_evaluation.ipynb
│   └── 04_af3_fullscale_and_ccd.ipynb
├── 08_practical_problems/
│   ├── 01_strings_dna.ipynb
│   ├── 02_dynamic_programming.ipynb
│   ├── 03_graphs_assembly.ipynb
│   ├── 04_statistics_ml_practical.ipynb
│   └── 05_alignment_phylogeny.ipynb
├── 09_ml_teaching_essentials/
│   └── 01_model_diagnostics.ipynb
├── 10_openfold3_finetuning/
│   └── 01_protein_structure_finetuning.ipynb
├── 11_membrane_protein_dynamics/
│   └── 01_membrane_protein_dynamics.ipynb
├── 12_generative_models/
│   └── 01_diffusion_protein_design.ipynb
├── 13_bayesian_methods/
│   └── 01_bayesian_ml_uncertainty.ipynb
├── 14_reinforcement_learning/
    └── 01_rl_protein_design.ipynb
├── 15_self_supervised_learning/
│   └── 01_contrastive_ssl.ipynb
└── 16_mlops_deployment/
    └── 01_mlops_for_protein_ml.ipynb
```

---

## Study Roadmap (4-Week Sprint)

### Week 1 — Python & ML Foundations
| Day | Notebook | Topics | HackerRank Practice |
|-----|----------|--------|---------------------|
| 1   | 00/01 | Strings, FASTA parsing, k-mers | Python Challenges (Easy) |
| 2   | 00/01 | OOP, generators, NumPy arrays | Python Challenges (Medium) |
| 3   | 00/02 | sklearn pipeline, CV, metrics | ML Basic Certification |
| 4   | 00/02 | Feature engineering, imbalance | ML Intermediate tasks |
| 5   | 00/02 | Hyperparameter tuning, GridCV | Data Science track |
| 6-7 | Review | Redo all exercises from memory | Practice assessments |

### Week 2 — Bioinformatics Algorithms
| Day | Notebook | Topics | HackerRank Practice |
|-----|----------|--------|---------------------|
| 8   | 01/01 | Edit distance, NW algorithm | String manipulation |
| 9   | 01/01 | Smith-Waterman, BLOSUM62 | Alignment problems |
| 10  | 02/01 | Codon table, ORF finding | DNA/protein problems |
| 11  | 02/01 | Variants, phylogenetics | Rosalind problems |
| 12  | 02/01 | Fibonacci/recurrence, probability | Algorithm challenges |
| 13-14 | Review | Full Rosalind problem set | Rosalind.info |

### Week 3 — Structural Biology & Protein ML
| Day | Notebook | Topics | Practice |
|-----|----------|--------|----------|
| 15  | 03/01 | PDB parsing, atom coords | Parse PDB files manually |
| 16  | 03/01 | RMSD, Kabsch algorithm, TM-score | Implement from scratch |
| 17  | 03/01 | Contact maps, phi/psi angles | Ramachandran analysis |
| 18  | 04/01 | Gene expression classification | Full pipeline exercise |
| 19  | 04/01 | Feature selection, PCA, clustering | K-means on omics data |
| 20-21 | Review | End-to-end bioinformatics ML | Kaggle competition |

### Week 4 — Deep Learning & Fine-Tuning
| Day | Notebook | Topics | Practice |
|-----|----------|--------|----------|
| 22  | 05/01 | CNN for sequences | Train on TFBS dataset |
| 23  | 05/01 | Transfer learning, freeze/unfreeze | Fine-tune a CNN |
| 24  | 05/01 | LoRA implementation | Implement from scratch |
| 25  | 06/01 | Protein graphs, GNN architecture | Run on toy dataset |
| 26  | 09/01 | Diagnostics, learning curves, debugging | Build model judgment |
| 27-28 | **Mock assessments** | Full 90-min timed test | HackerRank tests |

### Optional Bridge Week — Before Advanced Modules
| Day | Notebook | Why it matters |
|-----|----------|----------------|
| 29 | 06/02 | Deeper graph intuition before structural ML electives |
| 30 | 07/01 | Conceptual-only first pass of AF3 architecture |
| 31 | 07/03 | Learn to interpret PAE / pTM / ipTM before implementation depth |

### Optional Weeks 5-11 — Advanced Extension Track
| Week | Suggested Modules | Focus |
|------|-------------------|-------|
| 5 | 06/02 + 07/01-07/02 | GNN depth, AF3 architecture, data pipeline |
| 6 | 07/03-07/04 + 09/01 | Evaluation metrics, scaling, diagnostics |
| 7 | 10/01 + 11/01 | Structure-model fine-tuning, membrane proteins |
| 8 | 12/01 + 13/01 | Diffusion models, Bayesian uncertainty |
| 9 | 14/01 | Reinforcement learning and GFlowNet-style design |
| 10 | 15/01 | Self-supervised and contrastive learning for proteins |
| 11 | 16/01 | MLOps, deployment, monitoring, and CI/CD |

---

## HackerRank Scoring Strategy

### What Interviewers Score You On

```
1. CORRECTNESS (40%)
   - Solution passes all test cases
   - Handles edge cases (empty sequences, single residue, etc.)

2. CODE QUALITY (30%)
   - Clean, readable Python
   - Proper type hints
   - Efficient algorithms (know time complexity)

3. APPROACH (20%)
   - Can you explain WHY you chose this method?
   - Know alternatives and their trade-offs

4. DOMAIN KNOWLEDGE (10%)
   - Biological interpretation of results
   - Correct use of metrics for the task
```

### Time Complexity Reference
```python
# Must know these for interviews:
Edit Distance:        O(mn)    space O(mn) or O(min(m,n))
NW/SW alignment:      O(mn)    space O(mn)
k-mer frequency:      O(n)     Counter-based
FASTA parsing:        O(n)     streaming generator
RMSD:                 O(N)     N = number of atoms
PCA:                  O(p²n)   p = features, n = samples
Random Forest:        O(t·d·n·log n) t = trees, d = depth
```

### Common HackerRank Mistakes to Avoid
```
✗ Using 0-indexed when problem is 1-indexed (and vice versa)
✗ Not handling overlapping pattern matches
✗ Forgetting stop codons in translation
✗ Data leakage: scaling before train/test split
✗ Not stratifying imbalanced class splits
✗ Using accuracy on imbalanced datasets
✗ Integer overflow on large Fibonacci/recurrence
✗ Off-by-one errors in sliding window
```

---

## Quick Reference — Key Functions to Have Memorized

```python
# 1. Reverse complement
rc = dna.translate(str.maketrans('ATGC','TACG'))[::-1]

# 2. GC content
gc = (seq.count('G') + seq.count('C')) / len(seq)

# 3. k-mer frequency
from collections import Counter
freq = Counter(seq[i:i+k] for i in range(len(seq)-k+1))

# 4. FASTA parse
records = {}
for line in text.split('\n'):
    if line.startswith('>'): key = line[1:].split()[0]; records[key] = ''
    else: records[key] += line.strip()

# 5. Translation
''.join(CODON_TABLE.get(seq[i:i+3],'X') for i in range(0,len(seq)-2,3))

# 6. RMSD
np.sqrt(np.mean(np.sum((coords1 - coords2)**2, axis=1)))

# 7. ML pipeline (always use this pattern)
Pipeline([('scaler', StandardScaler()), ('clf', RandomForestClassifier())])

# 8. Proper split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)
```

---

## Interview Questions Bank

### Python / Algorithms
- What is the time complexity of edit distance? How do you optimize space?
- Explain the difference between NW and SW alignment.
- Why use a generator instead of a list for FASTA parsing?
- How do you handle memory-efficiently for genome-scale data?

### ML Fundamentals
- What is data leakage? Give an example in bioinformatics.
- When would you use ROC-AUC vs PR-AUC?
- Explain the bias-variance tradeoff in protein structure prediction context.
- How do you handle imbalanced datasets (e.g., 1% mutation rate)?
- Why does cross-validation need stratification?

### Structural Biology ML
- What is RMSD and when is it insufficient?
- When does TM-score > 0.5 matter?
- Why represent proteins as graphs?
- What is the Evoformer and why is it novel?
- When would you use ESMFold vs AlphaFold2?

### Fine-Tuning
- What is catastrophic forgetting and how do you prevent it?
- Explain LoRA in your own words. What is the rank parameter?
- Why use differential learning rates when fine-tuning?
- When is LoRA better than full fine-tuning?
- How do you evaluate protein function prediction models?

---

## Resources

| Resource | Use For |
|----------|---------|
| rosalind.info | Bioinformatics algorithm practice |
| hackerrank.com/skills-directory/machine_learning | ML certification |
| RCSB PDB (rcsb.org) | Real protein structures |
| Biopython docs | SeqIO, PDB, Align modules |
| ESM2 paper (Meta, 2022) | Protein LM architecture |
| AlphaFold2 paper (Nature, 2021) | Structure prediction theory |
| sklearn docs | Pipeline, metrics, cross-validation |

---

## Setup

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy biopython torch torchvision jupyter notebook ipykernel requests
# Optional (for GNNs):
pip install networkx torch-geometric ogb
# Optional (for protein LMs and advanced notebooks):
pip install transformers fair-esm
# Optional (for TensorFlow / advanced classical ML):
pip install tensorflow xgboost umap-learn
```
