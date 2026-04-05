# Module 17 — Capstone Project: EGFR End-to-End Pipeline
This module integrates every skill from the curriculum into a single production-quality pipeline: starting from an EGFR kinase sequence, progressing through ESM2 embeddings, AlphaFold3 structure prediction, LoRA-based deltadeltaG scoring, uncertainty quantification, and clinical interpretation.

## What You'll Learn
- Design and implement a complete ML pipeline from raw sequence to clinically actionable output
- Chain ESM2 embedding, AF3 structure prediction, and deltadeltaG scoring into a single reproducible workflow
- Apply conformal prediction and bootstrap methods to produce uncertainty bounds on mutation effect predictions
- Integrate Bayesian optimization to prioritize which EGFR mutations to characterize experimentally
- Interpret model outputs in the context of known oncogenic EGFR mutations (L858R, T790M, exon 19 del)
- Connect all 17 modules in one unified project: sequence analysis, structural biology, GNNs, generative models, SSL, RL, Bayesian methods, and MLOps
- Present findings with publication-quality visualizations and a clinically framed executive summary

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| AlphaFold3 architecture, pLDDT, and PAE | `07_alphafold3_core/` (all 6 notebooks) |
| LoRA fine-tuning and deltadeltaG prediction | `10_openfold3_finetuning/01_protein_structure_finetuning.ipynb` |
| Uncertainty quantification and Bayesian optimization | `13_bayesian_methods/01_bayesian_ml_uncertainty.ipynb` |
| ESM2 embeddings and SSL fine-tuning | `15_self_supervised_learning/01_contrastive_ssl.ipynb` |
| MLflow experiment tracking and FastAPI serving | `16_mlops_deployment/01_mlops_for_protein_ml.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 0 | `00_end_to_end_pipeline.ipynb` | EGFR sequence validation → ESM2 embeddings → AF3 structure → deltadeltaG mutation scanning → bootstrap uncertainty → Bayesian optimization → clinical ranking → FastAPI deployment | ~12h |

## After This Module You Can
- Build and present an end-to-end protein ML pipeline at Isomorphic Labs / DeepMind interview depth
- Explain every component of the EGFR pipeline — why each module is there and what it contributes
- Quantify prediction uncertainty and communicate it to both technical and clinical audiences
- Design a Bayesian optimization loop that identifies the highest-value EGFR mutations to test experimentally
- Use this capstone notebook as a portfolio piece to demonstrate integrated drug discovery ML skills

## Key Concepts Introduced
- **EGFR (Epidermal Growth Factor Receptor)**: Receptor tyrosine kinase mutated in ~15% of non-small-cell lung cancers; targeted by erlotinib, gefitinib, and osimertinib.
- **L858R**: Activating EGFR point mutation in the kinase domain; most common sensitizing mutation, conferring sensitivity to first-generation EGFR inhibitors.
- **T790M**: EGFR resistance mutation that emerges under first/second-generation inhibitor treatment; blocked by third-generation inhibitor osimertinib.
- **End-to-end pipeline**: ML system where raw biological input (sequence) flows through all processing and modeling steps to produce a final clinically interpretable output without manual intervention.
- **Mutation scanning**: Systematic in silico substitution of each residue position with all 20 amino acids to predict the effect of every possible point mutation on stability or binding.
- **Bootstrap uncertainty**: Resampling-based confidence interval method that estimates prediction variance by repeatedly fitting a model on random subsamples of the data.

## Next Module
This is the final module. You have completed the full curriculum.

Recommended next steps:
1. Apply to roles at Isomorphic Labs, Generate Biomedicines, Recursion, DeepMind
2. Extend the capstone with real ESM2 inference on Colab A100 or Kaggle GPU
3. Read the primary papers: AlphaFold3 (Abramson et al. 2024), RFdiffusion (Watson et al. 2023), Boltz-1
4. See `HOW_TO_LEARN_INDEPENDENTLY.md` Section 4 for the research reading strategy

## Difficulty: ⭐⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 12–16 hours
