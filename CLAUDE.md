# CLAUDE.md — AI Assistant Navigation Guide

This file helps Claude Code, GitHub Copilot, and Codex understand the curriculum structure so you can get AI-assisted walkthroughs of any notebook.

## Project Overview

**Goal:** Master bioinformatics + structural biology ML for computational biology ML teams / structural biology research labs-level roles
**Structure:** 56 Jupyter notebooks across 18 modules
**Target:** HackerRank ML assessments + technical interviews
**New to the field?** See `ZERO_TO_HERO.md` for the complete free learning path from absolute beginner to research level (6–18 months)

## How to Use AI Walkthroughs

### With Claude Code (Recommended)
Open a terminal in this directory and run:
```bash
claude
```
Then use these prompts to walk through any notebook:

**Start a module:**
> "Walk me through 05_deep_learning_finetuning/01_dl_and_finetuning.ipynb — explain each section and quiz me on the concepts"

**Deep dive on a concept:**
> "Explain the LoRA implementation in module 10 — show me the math and then the code"

**Interview prep:**
> "Quiz me on AlphaFold3 interview questions from module 07 — start easy and get harder"

**Debug help:**
> "I'm working on the GNN training loop in 06/01 — my loss is not decreasing, help me debug"

**Connect concepts:**
> "How does the Pairformer in module 07 relate to the transformer in module 05? Show me the architectural similarities"

### With GitHub Copilot
In VS Code with the Copilot extension:
1. Open any `.ipynb` file
2. Use Copilot Chat (`Ctrl+Shift+I`) with these prompts:
   - `@workspace Explain the EarlyStopping class in 05/01`
   - `@workspace How does collate_graphs work in 06/01?`
   - `@workspace Generate a practice problem similar to the LoRA exercise in 10/01`

### With GitHub Codex (Completions)
Code cells include `# CLAUDE HINT:` comments that trigger useful completions. Look for these markers and let Copilot complete them.

## Module Quick Reference

| Module | Directory | Key Concepts |
|--------|-----------|--------------|
| 0 — Python & ML Basics | `00_python_ml_basics/` | Python, NumPy, Pandas, CV, metrics |
| 1 — Sequence Analysis | `01_sequence_analysis/` | NW/SW alignment, Rosalind 284 problems, BLOSUM62 |
| 2 — Genomics | `02_genomics/` | Codon tables, ORF finding, variants, phylogenetics |
| 3 — Structural Biology | `03_structural_biology/` | PDB parsing, RMSD, Kabsch, TM-score |
| 4 — ML for Omics | `04_ml_for_omics/` | Gene expression, p>>n problem, PCA |
| 5 — Deep Learning | `05_deep_learning_finetuning/` | CNNs, LoRA, Transformers, EarlyStopping, gradient flow |
| 6 — Structural ML + GNNs | `06_structural_ml_gnns/` | Protein graphs, message passing, equivariance |
| 7 — AlphaFold3 Core | `07_alphafold3_core/` | Zero-to-hero on-ramp, Pairformer, FAPE, triangle attention, diffusion, training loop |
| 8 — Practical Problems | `08_practical_problems/` | HackerRank + Rosalind combined by topic |
| 9 — ML Teaching | `09_ml_teaching_essentials/` | Bias-variance, learning curves, model diagnostics |
| 10 — Fine-Tuning (Capstone) | `10_openfold3_finetuning/` | OpenFold code walkthrough, Pairformer fine-tuning, LoRA, ΔΔG, TCR-pMHC |
| 11 — Membrane Proteins | `11_membrane_protein_dynamics/` | TM topology, membrane-specific fine-tuning, MD simulation basics (Verlet, PBC, PME, ML potentials) |
| 12 — Generative Models | `12_generative_models/` | Diffusion models, protein design, unified 12-15 framework (pre-train → generate → filter → steer) |
| 13 — Bayesian Methods | `13_bayesian_methods/` | Uncertainty quantification, MCMC, Bayesian reasoning |
| 14 — Reinforcement Learning | `14_reinforcement_learning/` | DQN, PPO, GFlowNets, design-time optimization |
| 15 — Self-Supervised Learning | `15_self_supervised_learning/` | MLM, SimCLR, BYOL, protein foundation-model pretraining |
| 16 — MLOps & Deployment | `16_mlops_deployment/` | Experiment tracking, serving, monitoring, CI/CD |
| 17 — Capstone Project | `17_capstone_project/` | End-to-end EGFR pipeline integrating all 17 modules |

## Learning Paths

### Path A: HackerRank Certification (2 weeks)
```
00/03 → 00/04 → 00/05 → 08/01 → 08/02 → 08/03 → 08/04 → 08/05
```

### Path B: Rosalind Problems (3 weeks)
```
01/01 → 01/02 → 01/03 → 01/04 → 01/05 → 01/06 → 02/01
```

### Path C: Structural ML (for computational biology ML teams) (4 weeks)
```
03/01 → 05/01 → 06/01 → 07/01 → 07/02 → 07/03 → 07/04 → 10/01
```

### Path D: Full Curriculum (10 weeks)
All modules in order: 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → **17 (Capstone)**

## AI Walkthrough Tips

1. **Start with the TL;DR cell** — every notebook starts with a Plain English explanation. Ask Claude: "Explain this TL;DR and what I'll be able to do after this notebook"

2. **Work through code cells interactively** — paste a code cell and ask: "Explain this code line by line" or "What would happen if I changed X?"

3. **Use the interview questions** — Modules 05-07 and 10 have `6️⃣ Advanced Interview Preparation` sections. Ask Claude to quiz you.

4. **Request variations** — "Show me an alternative implementation of the Pairformer attention using einops instead of einsum"

5. **Debug with context** — If code fails, paste the error + the cell and ask Claude: "This is from the GNN notebook in module 06 — why is this failing?"

## File Structure

```
hackerrank/
├── CLAUDE.md              ← You are here (AI navigation guide)
├── ZERO_TO_HERO.md        ← Complete free learning path: zero background to hero level
├── README.md              ← Full curriculum overview
├── CURRICULUM.md          ← Detailed topic map with difficulty ratings
├── RESOURCES.md           ← All learning resources (books, videos, datasets)
├── STUDY_PLAN.md          ← Week-by-week study schedule
├── SYLLABUS.md            ← University-quality syllabus with weekly objectives + assessments
├── HOW_TO_LEARN_INDEPENDENTLY.md ← Independent learner guide
├── CLOUD_SETUP.md         ← Free GPU setup: Colab, Kaggle, Lightning AI, Vast.ai
├── CURRICULUM_RATING.md   ← Lecturer assessment: module-by-module ratings and gaps
├── BEGINNER_ROADMAP.md    ← Zero-background 10-week plan with daily targets
├── GLOSSARY.md            ← 55+ terms: biology, ML, structural ML with plain English
├── QUICK_START.md         ← 5-minute setup guide (copy-paste commands)
├── requirements.txt       ← All Python dependencies
├── .gitignore
├── .github/
│   ├── CONTRIBUTING.md    ← How to contribute notebooks or fixes
│   ├── ISSUE_TEMPLATE/    ← Bug report + resource suggestion templates
│   └── workflows/         ← GitHub Actions: notebook JSON validation
├── 00_python_ml_basics/   ← 9 notebooks  [README.md in each module]
├── 01_sequence_analysis/  ← 7 notebooks
├── 02_genomics_gene_analysis/           ← 4 notebooks
├── 03_protein_structural_biology/       ← 1 notebook
├── 04_ml_bioinformatics/                ← 1 notebook
├── 05_deep_learning_finetuning/ ← 1 notebook
├── 06_structural_ml_gnns/ ← 2 notebooks
├── 07_alphafold3_core/    ← 7 notebooks (incl. zero-to-hero, training loop + diffusion deep dive)
├── 08_practical_problems/ ← 5 notebooks
├── 09_ml_teaching_essentials/ ← 1 notebook
├── 10_openfold3_finetuning/ ← 2 notebooks (code walkthrough + capstone)
├── 11_membrane_protein_dynamics/ ← 2 notebooks (dynamics + MD simulation basics)
├── 12_generative_models/   ← 2 notebooks (diffusion + connecting modules 12-15)
├── 13_bayesian_methods/    ← 1 notebook
├── 14_reinforcement_learning/ ← 1 notebook
├── 15_self_supervised_learning/ ← 1 notebook
├── 16_mlops_deployment/ ← 1 notebook
└── 17_capstone_project/ ← 1 notebook (EGFR end-to-end pipeline, integrates all modules)
```

## Common Claude Code Commands for This Project

```bash
# List all notebooks
claude "list all notebook files in this curriculum and their topics"

# Get a concept explanation
claude "explain triangle attention from 07/01 with the math"

# Generate a practice problem
claude "create a new practice problem similar to the Smith-Waterman implementation in 01/01"

# Review your solution
claude "review my implementation of Needleman-Wunsch — here's my code: [paste code]"

# Interview simulation
claude "simulate a 30-minute technical interview for an ML engineer role at computational biology ML teams focused on protein structure prediction"
```

## Dependencies

Install all dependencies:
```bash
pip install -r requirements.txt
```

Key packages: `torch`, `transformers`, `biopython`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Optional packages used in specific notebooks: `tensorflow`, `networkx`, `torch-geometric`, `ogb`, `xgboost`, `umap-learn`, `ViennaRNA`, `mlflow`, `fastapi`, `uvicorn`, `pydantic`
