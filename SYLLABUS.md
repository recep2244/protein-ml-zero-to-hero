# Bioinformatics ML Curriculum — Official Syllabus
## Modeled After MIT 6.874 / Stanford CS279 / Harvard Systems Biology

**Instructor-level guide:** Use this syllabus to pace your self-study. Each "week" assumes
~15 hours of work (similar to a graduate seminar course).

**For students new to coding:** Budget double the time per week for the first 4 weeks.

---

## Course Description

This curriculum teaches computational biology and machine learning at the level required for
research or industry roles at companies like computational biology ML teams, Genentech, drug discovery companies, and Schrödinger.

**Prerequisites:**
- Python: functions, loops, list comprehensions, basic numpy
- Mathematics: calculus (chain rule), linear algebra (matrix multiply, dot product), basic probability
- Biology: none required — we teach biology as needed

**After completion, students will be able to:**
1. Implement and explain core bioinformatics algorithms (alignment, HMMs, phylogeny)
2. Build, train, and debug deep learning models for protein data
3. Understand and explain the AlphaFold 3 architecture at the component level
4. Fine-tune foundation models on new biological tasks
5. Navigate production ML codebases (OpenFold, Boltz) independently
6. Pass technical interviews at computational biology companies

---

## Week-by-Week Schedule

### UNIT 1: Foundations (Weeks 1-4)
*Goal: Build the Python, ML, and biology foundations needed for the rest of the curriculum.*

---

#### Week 1 — Python & ML Environment

**Notebooks:**
- `00/00_setup_and_troubleshooting.ipynb` — setup and verification
- `00/01_python_core_for_bioinformatics.ipynb` — Python for biology

**External Reading:**
- [Harvard CS50P Python](https://cs50.harvard.edu/python/) — complete Weeks 1-3 if Python is new to you
- [MIT 6.S191 Lab 0](https://introtodeeplearning.com/) — environment setup for deep learning

**Learning Objectives:**
- [ ] Python environment set up and verified
- [ ] Can write a DNA complement function, GC content calculator, and k-mer frequency counter
- [ ] Understand time complexity: O(n), O(n²), O(n log n) — can benchmark with code

**Predict Before Running:**
> Before running the GC content function, predict: "What should gc_content('ATAT') return?" (Answer: 0.0)

---

#### Week 2 — ML Foundations

**Notebooks:**
- `00/02_ml_fundamentals.ipynb` — core ML concepts
- `00/06_pytorch_fundamentals.ipynb` — PyTorch

**External Reading:**
- [Stanford CS229 Lecture Notes 1-3](https://cs229.stanford.edu/) — linear regression, logistic regression, regularization
- [MIT 6.S191 Lecture 1](https://introtodeeplearning.com/) — neural network basics

**Learning Objectives:**
- [ ] Can implement train/val/test split with stratification
- [ ] Can build a 3-layer network in PyTorch with a training loop
- [ ] Understand cross-validation and why you must not use the test set for model selection

**Common Mistake to Avoid:**
> Applying `StandardScaler.fit_transform()` on the full dataset BEFORE splitting into train/test.
> This leaks test set statistics into training. Always: `scaler.fit(X_train)` then `scaler.transform(X_test)`.

---

#### Week 3 — Sequence Analysis I

**Notebooks:**
- `01/01_alignment_algorithms.ipynb` — NW, SW, BLAST

**External Reading:**
- [Bioinformatics Algorithms Chapter 1-3](https://www.bioinformaticsalgorithms.org/) — free
- [MIT 7.91J Lecture 2](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — sequence alignment in depth

**Learning Objectives:**
- [ ] Implement Needleman-Wunsch without looking at reference code
- [ ] Can explain the difference between global and local alignment and when to use each
- [ ] Understand why BLAST is fast (seed-and-extend heuristic)

**Hands-On Exercise:**
> Download hemoglobin sequences from UniProt (human, mouse, zebrafish). Align all three pairwise.
> Which pair is most similar? Does this match evolutionary expectations?

---

#### Week 4 — Sequence Analysis II + HMMs

**Notebooks:**
- `01/05_rosalind_phylogeny.ipynb` — phylogenetics
- `01/07_hidden_markov_models.ipynb` — HMMs
- `01/02_rosalind_complete.ipynb` — solve 10+ problems

**External Reading:**
- [MIT 7.91J Problem Set 4 (HMMs)](https://ocw.mit.edu/) — implement and verify
- [Biological Sequence Analysis (Durbin et al.) Chapter 3](https://www.amazon.com/Biological-Sequence-Analysis-Probabilistic-Proteins/dp/0521629713) — HMMs for bioinformatics

**Learning Objectives:**
- [ ] Implement Viterbi algorithm for CpG island detection
- [ ] Implement UPGMA for phylogenetic tree construction
- [ ] Understand Baum-Welch EM and why log-likelihood must monotonically increase

---

### UNIT 2: Structural Biology & Genomics (Weeks 5-7)

---

#### Week 5 — Protein Structure

**Notebooks:**
- `03/01_structure_analysis.ipynb` — PDB, RMSD, Kabsch, TM-score
- `02/01_genomics_core.ipynb` — genomics overview

**External Reading:**
- [iBiology Protein Structure lectures](https://www.ibiology.org/biochemistry/protein-structure/) — free; covers primary through quaternary
- [MIT 5.069 Structure lecture notes](https://ocw.mit.edu/) — X-ray crystallography context

**Learning Objectives:**
- [ ] Parse a PDB file and extract Cα coordinates
- [ ] Implement Kabsch alignment and compute RMSD
- [ ] Understand what TM-score measures and why it's better than RMSD for fold comparison

---

#### Week 6 — Genomics & Omics

**Notebooks:**
- `02/02_rnaseq_analysis.ipynb` — RNA-seq
- `02/03_variant_analysis.ipynb` — GWAS, variants
- `02/04_pathway_enrichment.ipynb` — ORA, GSEA

**External Reading:**
- [StatQuest RNA-seq series (20 videos)](https://www.youtube.com/playlist?list=PLblh5JKOoLUKMmxlpHx3Ntk36e6Q3dOec) — best free resource
- [Harvard MCB112 Biological Data Analysis](https://mcb112.org/) — statistical tests for genomics

**Learning Objectives:**
- [ ] Normalize count data using size factors (DESeq2 approach)
- [ ] Apply Benjamini-Hochberg FDR correction and explain why it's better than Bonferroni for genomics
- [ ] Run overrepresentation analysis (hypergeometric test) on a gene set

---

#### Week 7 — ML for Omics

**Notebooks:**
- `04/01_ml_for_omics.ipynb` — dimensionality reduction, clustering

**External Reading:**
- [Stanford CS229 Lecture 13: Unsupervised Learning](https://cs229.stanford.edu/) — PCA, k-means with math
- [UMAP paper](https://arxiv.org/abs/1802.03426) — understand why UMAP preserves local structure better than t-SNE for scRNA-seq

**Learning Objectives:**
- [ ] Apply 5-step single-cell preprocessing pipeline (QC → norm → log → HVG → PCA → UMAP)
- [ ] Interpret a UMAP plot: what clusters mean, what they don't mean
- [ ] Know when PCA is sufficient vs when UMAP is needed

---

### UNIT 3: Deep Learning for Biology (Weeks 8-10)

---

#### Week 8 — Deep Learning Foundations

**Notebooks:**
- `05/01_dl_and_finetuning.ipynb` — CNN, LSTM, Transformer, LoRA

**External Reading:**
- [MIT 6.S191 Lectures 1-3](https://introtodeeplearning.com/) — watch before this week
- [Stanford CS224n Lecture 7: Transformers](https://web.stanford.edu/class/cs224n/) — best transformer explanation

**Learning Objectives:**
- [ ] Implement scaled dot-product attention from scratch (Q, K, V → output)
- [ ] Understand LoRA: why low-rank, what rank r means, how it reduces parameters
- [ ] Can diagnose overfitting from a training curve and apply the correct fix

**Implementation Exercise:**
> Implement LoRA from scratch: `ΔW = BA` where B ∈ R^(d×r), A ∈ R^(r×d), rank r << d.
> Verify: when r=d, it's equivalent to full fine-tuning.

---

#### Week 9 — Graph Neural Networks

**Notebooks:**
- `06/01_structure_ml.ipynb` — protein graphs
- `06/02_gnn_deep_dive.ipynb` — message passing, SE(3) equivariance

**External Reading:**
- [Stanford CS224W Lectures 1-5](https://web.stanford.edu/class/cs224w/) — best GNN course; free
- [SE(3)-Transformers paper](https://arxiv.org/abs/2006.10503) — equivariant networks for 3D structures

**Learning Objectives:**
- [ ] Build a protein contact graph from PDB Cα coordinates (8Å threshold)
- [ ] Implement one round of message passing by hand for N=3 nodes
- [ ] Test SE(3) equivariance: rotate input 90° → verify output rotates consistently

---

#### Week 10 — Sequence Models & Protein Language Models

**Notebooks:**
- `05/02_sequence_models_rnn_lstm.ipynb` — RNN, LSTM
- `15/01_contrastive_ssl.ipynb` — ESM-2, self-supervised learning

**External Reading:**
- [Stanford CS224n Lecture 6](https://web.stanford.edu/class/cs224n/) — RNNs and their limitations
- [ESM-2 paper](https://www.science.org/doi/10.1126/science.ade2574) — protein language models

**Learning Objectives:**
- [ ] Explain why transformers replaced LSTMs (attention = O(N²) but parallelizable; LSTM = O(N) but serial)
- [ ] Extract ESM-2 embeddings for a protein sequence using the fair-esm library
- [ ] Understand contrastive learning: how SimCLR learns representations without labels

---

### UNIT 4: AlphaFold 3 (Weeks 11-14)

*This is the core of the curriculum. Spend extra time here.*

---

#### Week 11 — AF3 Architecture

**Notebooks:**
- `07/00_af3_zero_to_hero.ipynb` — on-ramp (start here if new to AF3)
- `07/01_af3_architecture.ipynb` — Pairformer, triangle attention

**External Reading:**
- [AF3 Nature 2024 Methods Sections 1-2](https://www.nature.com/articles/s41586-024-07487-w)
- [Jumper EMBL lecture (1 hour)](https://www.youtube.com/watch?v=gg7WjuFs8F4)
- [Yannic Kilcher AF2 paper walkthrough](https://www.youtube.com/watch?v=nGVFbPKB3iE)

**Learning Objectives:**
- [ ] Draw the AF3 architecture from memory (Input Embedder → Pairformer → Diffusion → Confidence)
- [ ] Explain why triangle attention updates z[i,k] using paths through j
- [ ] Compute (on paper) what the pair tensor z shape is for N=100 residues, c_z=128

---

#### Week 12 — AF3 Data Pipeline & Diffusion

**Notebooks:**
- `07/02_af3_data_pipeline.ipynb` — features, Atom14, MSA
- `07/03_af3_evaluation.ipynb` — pLDDT, PAE, TM-score

**External Reading:**
- [AF3 Methods Section 2-3](https://www.nature.com/articles/s41586-024-07487-w)
- [Denoising Diffusion Probabilistic Models paper](https://arxiv.org/abs/2006.11239) (Ho et al. 2020)
- [Lilian Weng: Diffusion Models](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — best explainer

**Learning Objectives:**
- [ ] Explain the forward diffusion process: x_t = sqrt(α_bar_t)·x_0 + sqrt(1-α_bar_t)·ε
- [ ] Compute pseudo-Cβ position from backbone N, Cα, C atoms (using the formula)
- [ ] Interpret a PAE plot: what high PAE between domains tells you about confidence

---

#### Week 13 — AF3 Full Scale & Training

**Notebooks:**
- `07/04_af3_fullscale_and_ccd.ipynb` — production engineering
- `07/05_af3_training_loop.ipynb` — losses, schedules, memory tricks

**External Reading:**
- [AF3 Methods Section 4 (Training)](https://www.nature.com/articles/s41586-024-07487-w)
- [Flash Attention paper](https://arxiv.org/abs/2205.14135)
- [OpenFold utils/loss.py (GitHub)](https://github.com/aqlaboratory/openfold/blob/main/openfold/utils/loss.py)

**Learning Objectives:**
- [ ] Implement FAPE loss and verify it gives 0 for perfect prediction
- [ ] Explain gradient accumulation and when you need it
- [ ] Name 3 memory optimization techniques for long-sequence training and the tradeoff of each

---

#### Week 14 — OpenFold Code & Fine-tuning

**Notebooks:**
- `10/00_openfold3_walkthrough.ipynb` — navigate the codebase
- `10/01_protein_structure_finetuning.ipynb` — SKEMPI v2 ΔΔG prediction

**External Reading:**
- [OpenFold GitHub — model/model.py](https://github.com/aqlaboratory/openfold)
- [Boltz-1 GitHub](https://github.com/jwohlwend/boltz) — more accessible AF3 codebase
- [SKEMPI v2 database](https://life.bsc.es/pid/skempi2) — the dataset you fine-tune on

**Learning Objectives:**
- [ ] Can navigate OpenFold source to find any class/function within 2 minutes
- [ ] Implement LoRA-based fine-tuning on SKEMPI v2 with correct protein-level splitting
- [ ] Know 5 failure modes of fine-tuning and the fix for each

---

### UNIT 5: Advanced Topics (Weeks 15-18)

---

#### Week 15 — Generative Models & Protein Design

**Notebooks:**
- `12/01_diffusion_protein_design.ipynb` — diffusion for structure generation

**External Reading:**
- [RFdiffusion paper](https://www.nature.com/articles/s41586-023-06415-8) — protein design with diffusion
- [MIT 6.S192 Deep Generative Models](https://mit-deep-learning.com/) — free; covers VAEs, GANs, diffusion

**Learning Objectives:**
- [ ] Explain the difference between AF3 (prediction) and RFdiffusion (generation)
- [ ] Implement a toy DDPM forward and reverse process for 1D data

---

#### Week 16 — Bayesian Methods & Uncertainty

**Notebooks:**
- `13/01_bayesian_ml_uncertainty.ipynb`

**External Reading:**
- [Harvard AM207 (full course)](https://am207.github.io/2018fall/) — complete this week's topic
- [Stanford CS228 PGM notes](https://cs228.stanford.edu/) — variational inference chapter

---

#### Week 17 — Reinforcement Learning for Biology

**Notebooks:**
- `14/01_rl_protein_design.ipynb`

**External Reading:**
- [Stanford CS234 Lecture 1-4](https://web.stanford.edu/class/cs234/) — RL foundations
- [GFlowNets for molecular design](https://arxiv.org/abs/2106.04399)

---

#### Week 18 — MLOps & Deployment

**Notebooks:**
- `16/01_mlops_for_protein_ml.ipynb`
- `11/01_membrane_protein_dynamics.ipynb`

**External Reading:**
- [Stanford CS329S ML Systems Design](https://mlsys.stanford.edu/)
- [MLflow documentation](https://mlflow.org/docs/latest/index.html)
- [FastAPI documentation](https://fastapi.tiangolo.com/)

---

## Assessment (Self-Assessment at Key Milestones)

### After Week 4 (Sequence Analysis Checkpoint)
Attempt these without reference:
1. Implement Smith-Waterman for 2 short sequences (< 30 min)
2. Implement UPGMA from a 4×4 distance matrix (< 45 min)
3. Explain what a profile HMM is and why it's more sensitive than BLAST (2 min verbal)

### After Week 10 (Deep Learning Checkpoint)
Attempt these without reference:
1. Implement scaled dot-product attention: `softmax(QK^T/sqrt(dk)) V` (< 20 min)
2. Build a protein contact graph and run one message-passing step (< 30 min)
3. Explain LoRA: draw the weight decomposition diagram, state the parameter count (2 min verbal)

### After Week 14 (AF3 Checkpoint — Interview-Ready Level)
Attempt these without reference:
1. Draw AF3 architecture with approximate tensor shapes at each stage (< 15 min)
2. Implement FAPE loss for 3 residues with identity frames (< 30 min)
3. Navigate OpenFold to find triangle attention implementation (< 5 min using grep)
4. Fine-tune a mini model on 50 ΔΔG data points with proper splitting (< 1 hour)

### After Week 18 (Full Curriculum Completion)
You should be able to:
- Pass a technical screen at computational biology ML teams / structural biology research labs / Schrödinger
- Read any new protein ML paper and understand it within 3 hours
- Implement any component from the AF3 paper from scratch
- Design a ML pipeline for a new biological prediction task

---

## Office Hours Equivalent (Self-Study Analogues)

When you need synchronous help:
- **[Biostars Q&A](https://www.biostars.org/)** — post questions, usually answered in hours
- **[PyTorch Discuss](https://discuss.pytorch.org/)** — ML/PyTorch implementation questions
- **[Machine Learning subreddit](https://www.reddit.com/r/MachineLearning/)** — paper discussions
- **[OpenFold GitHub Issues](https://github.com/aqlaboratory/openfold/issues)** — OpenFold-specific questions
- **[AlphaFold Community Forum](https://alphafold.ebi.ac.uk/faqs)** — AF3 usage questions

---

## Supplementary Tracks (Optional Deep Dives)

### Track A: Pure Theory (for PhD aspirants)
- [MIT 18.657 Mathematics of Machine Learning](https://ocw.mit.edu/)
- [Princeton Information Theory (Cover & Thomas)](http://www.elementsofinformationtheory.com/)
- [Stanford Probabilistic Graphical Models (CS228)](https://cs228.stanford.edu/)

### Track B: Systems & Engineering (for MLOps roles)
- [Stanford CS329S ML Systems](https://mlsys.stanford.edu/)
- [MIT 6.S965 TinyML](https://tinyml.mit.edu/)
- [NVIDIA Deep Learning Performance Guide](https://docs.nvidia.com/deeplearning/performance/)

### Track C: Drug Discovery Focus (for pharma/biotech)
- [MIT 6.874 Computational Biology of Disease](https://mit6874.github.io/)
- [EMBL-EBI Drug Discovery Training](https://www.ebi.ac.uk/training/)
- [ChEMBL database tutorials](https://chembl.gitbook.io/chembl-interface-documentation/)
