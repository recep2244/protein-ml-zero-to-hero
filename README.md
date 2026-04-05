# Bioinformatics & Structural Biology ML — Zero to Expert Curriculum

![Notebooks](https://img.shields.io/badge/Notebooks-50-blue)
![Modules](https://img.shields.io/badge/Modules-18-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-orange)
![Level](https://img.shields.io/badge/Level-Zero%20to%20Expert-purple)

---

## What Is This?

This is a **complete, self-contained curriculum** for learning computational biology and structural ML — from your first line of Python to implementing AlphaFold3 components, fine-tuning OpenFold, and building a real drug discovery pipeline. It is designed for anyone who wants to work at the intersection of machine learning and biology, targeting roles at companies like computational biology ML teams, drug discovery companies, and drug discovery companies. By the end, you will have built a production-quality EGFR kinase pipeline and be ready to pass HackerRank ML assessments and technical interviews.

---

## You Can Do This

> **Zero Python required. Zero biology required. Zero ML required. High school math is enough.**

Module 00 starts at the very beginning. Every notebook opens with a plain-English TL;DR. You will never be dropped into the deep end without context.

---

## What You Will Build (Capstone)

The final project is an end-to-end EGFR kinase domain drug discovery pipeline integrating every module:

```
Protein Sequence (FASTA)
        │
        ▼
ESM-2 Embeddings          ← Module 05 (Transformers)
        │
        ▼
AlphaFold3 Structure      ← Module 07 (Pairformer, diffusion)
  + Confidence Scores
        │
        ▼
ΔΔG Mutation Scanning     ← Module 10 (OpenFold fine-tuning)
        │
        ▼
Uncertainty Quantification ← Module 13 (Bayesian methods)
        │
        ▼
Drug Candidate Ranking    ← Module 17 (Capstone: EGFR pipeline)
```

All steps are reproducible in a single Jupyter notebook using public datasets and free compute.

---

## Quick Start

```bash
git clone https://github.com/your-username/hackerrank-bioinformatics
cd hackerrank
pip install -r requirements.txt
jupyter notebook
```

Open `00_python_ml_basics/01_python_refresher.ipynb` and follow the TL;DR cell at the top. That's it.

---

## Learning Paths

Choose the path that matches your goal:

| Path | Goal | Time | Modules |
|------|------|------|---------|
| 🟢 **Path A** | HackerRank Certification | 2 weeks | 00/03 → 00/04 → 00/05 → 08/01–08/05 |
| 🔵 **Path B** | Bioinformatics & Rosalind | 3 weeks | 01/01–01/06 → 02/01–02/04 → 08 |
| 🟡 **Path C** | Structural ML (computational biology ML teams) | 4 weeks | 03 → 05 → 06 → 07/01–07/04 → 10 |
| 🔴 **Path D** | Full Curriculum | 10 weeks | Modules 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 |

---

## Module Overview

All 18 modules, 50 notebooks. Difficulty is rated relative to the curriculum — not relative to the field.

| # | Module | Key Topics | Difficulty | Notebooks |
|---|--------|-----------|------------|-----------|
| 00 | 🐍 Python & ML Basics | Python, NumPy, Pandas, cross-validation, metrics | ⭐⭐ | 9 |
| 01 | 🧬 Sequence Analysis | NW/SW alignment, BLOSUM62, Rosalind 284 problems | ⭐⭐⭐ | 7 |
| 02 | 🔬 Genomics & Gene Analysis | Codon tables, ORF finding, variants, phylogenetics | ⭐⭐⭐ | 4 |
| 03 | 🏗️ Protein Structural Biology | PDB parsing, RMSD, Kabsch algorithm, TM-score | ⭐⭐⭐ | 1 |
| 04 | 📊 ML for Omics | Gene expression, p>>n problem, PCA, regularization | ⭐⭐⭐ | 1 |
| 05 | 🧠 Deep Learning & Fine-Tuning | CNNs, LoRA, Transformers, EarlyStopping, gradient flow | ⭐⭐⭐⭐ | 2 |
| 06 | 🕸️ Structural ML & GNNs | Protein graphs, message passing, SE(3) equivariance | ⭐⭐⭐⭐ | 2 |
| 07 | 🔮 AlphaFold3 Core | Pairformer, FAPE loss, triangle attention, diffusion module, training loop | ⭐⭐⭐⭐⭐ | 6 |
| 08 | 💪 Practical Problems | HackerRank + Rosalind combined by topic | ⭐⭐⭐ | 5 |
| 09 | 📐 ML Teaching Essentials | Bias-variance, learning curves, model diagnostics | ⭐⭐⭐ | 1 |
| 10 | ⚙️ OpenFold3 Fine-Tuning | OpenFold code walkthrough, LoRA on Pairformer, ΔΔG, TCR-pMHC | ⭐⭐⭐⭐⭐ | 2 |
| 11 | 🧫 Membrane Protein Dynamics | TM topology, membrane-specific fine-tuning, conformational modeling | ⭐⭐⭐⭐ | 2 |
| 12 | 🌀 Generative Models | Diffusion models, score matching, protein design with flow matching | ⭐⭐⭐⭐⭐ | 2 |
| 13 | 🎲 Bayesian Methods | Uncertainty quantification, MCMC, Gaussian processes | ⭐⭐⭐⭐ | 1 |
| 14 | 🎮 Reinforcement Learning | DQN, PPO, GFlowNets, design-time optimization | ⭐⭐⭐⭐⭐ | 1 |
| 15 | 🔄 Self-Supervised Learning | MLM, SimCLR, BYOL, protein foundation-model pretraining | ⭐⭐⭐⭐ | 1 |
| 16 | 🚀 MLOps & Deployment | Experiment tracking, model serving, monitoring, CI/CD | ⭐⭐⭐⭐ | 1 |
| 17 | 🏆 Capstone Project | End-to-end EGFR pipeline integrating all 17 prior modules | ⭐⭐⭐⭐⭐ | 1 |

---

## What Every Notebook Contains

Every notebook in this curriculum is built to the same 10-point quality standard:

1. **TL;DR cell** — Plain English: what is this, why does it matter, zero background required
2. **Beginner frame** — Intuition-first explanation before any math or code
3. **Real datasets** — Public data from UniProt, PDB, NCBI, Kaggle, and HuggingFace
4. **Exercises with TODOs** — Guided fill-in-the-blank coding exercises with solutions
5. **Debug exercises** — Intentionally broken code for you to diagnose and fix
6. **Resources** — Curated papers, videos, and tutorials; beginner-friendly options marked
7. **Interview Q&A** — 4–6 questions with full technical answers, calibrated to senior ML roles
8. **Real-world context** — How this topic is used at computational biology ML teams, Genentech, or in the clinic
9. **Mastery check** — Self-assessment checklist before moving on
10. **Cross-module connections** — Explicit links to prerequisite and follow-on notebooks

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [`ZERO_TO_HERO.md`](ZERO_TO_HERO.md) | Complete free learning path from absolute beginner to research level (6–18 months) |
| [`SYLLABUS.md`](SYLLABUS.md) | University-quality syllabus with weekly objectives and assessments |
| [`HOW_TO_LEARN_INDEPENDENTLY.md`](HOW_TO_LEARN_INDEPENDENTLY.md) | MIT/Stanford/Harvard independent learner guide |
| [`BEGINNER_ROADMAP.md`](BEGINNER_ROADMAP.md) | Step-by-step onboarding for complete beginners |
| [`GLOSSARY.md`](GLOSSARY.md) | Plain-English definitions of every technical term used in the curriculum |
| [`QUICK_START.md`](QUICK_START.md) | Get your first notebook running in under 10 minutes |
| [`CLOUD_SETUP.md`](CLOUD_SETUP.md) | Run any notebook for free on Colab, Kaggle, or Lightning.ai |

---

## Industry Relevance

This curriculum is directly targeted at the techniques and problem domains used by:

- **computational biology ML teams** (structural biology research labs spinout) — AlphaFold3, structure prediction, drug design
- **drug discovery companies** — Generative protein design, diffusion models
- **drug discovery companies** — High-throughput phenomics, ML-guided screening
- **Eikon Therapeutics** — Single-molecule imaging, target ID with ML
- **Relay Therapeutics** — Conformational dynamics, structure-based drug design

The capstone project (Module 17) is designed to be portfolio-ready for a junior ML engineer or research scientist application at any of these companies.

---

## Prerequisites

None. The curriculum is entirely self-contained.

- No prior Python experience needed (Module 00 covers it)
- No biology background needed (each module introduces the biology it needs)
- No ML experience needed (Module 00 covers the essentials)
- High school math (algebra, basic statistics) is sufficient for Modules 00–06
- Calculus and linear algebra are introduced gradually from Module 05 onward

---

## Contributing

Contributions are welcome — bug fixes, new exercises, improved explanations, and additional Rosalind problems are especially appreciated. Please read [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) before opening a pull request.

---

## License

MIT License. See [`LICENSE`](LICENSE) for details. All datasets referenced are publicly available under their original licenses.

---

*Built for HackerRank ML assessments and technical interviews at computational biology companies. If this curriculum helped you land a role, open an issue and tell us — it keeps the project alive.*
