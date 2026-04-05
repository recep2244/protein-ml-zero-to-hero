# Beginner Roadmap — Zero to Bioinformatics ML Engineer in 10 Weeks

Welcome. If you found this file, you are either brand new to programming, new to biology, or new to machine learning — maybe all three. That is completely fine. This roadmap was written for exactly that person. Think of it as a mentor sitting next to you, pointing at the screen.

You do not need a degree. You do not need to know what a neural network is yet. You need curiosity, a computer, and about 2 hours a day.

---

## 1. Before You Start — 5-Item Checklist

Work through this list once, in order, before opening any notebook.

- [ ] **Install Python 3.10 or later**
  Go to https://www.python.org/downloads/ and download the installer for your operating system. During installation, check the box that says "Add Python to PATH." Verify by opening a terminal and typing `python --version`. You should see `Python 3.10.x` or higher.

- [ ] **Set up a notebook environment**
  *Option A (local, recommended for long-term use):* Install VS Code from https://code.visualstudio.com, then install the "Jupyter" extension from the Extensions panel. Open any `.ipynb` file and you are ready.
  *Option B (cloud, zero setup):* Go to https://colab.research.google.com, sign in with a Google account, and upload any notebook. Free GPU is available for later modules.

- [ ] **Run the Quick Start commands**
  Open a terminal in this project folder and run:
  ```bash
  pip install -r requirements.txt
  ```
  This installs every package used across all 40 notebooks. It may take 5-10 minutes. If you see red error lines, read the "I'm Stuck" section below before continuing.

- [ ] **Open notebook 00/00 and run Cell 1 successfully**
  Navigate to `00_python_ml_basics/` and open the first notebook. Run the very first code cell. If it executes without an error, your environment is working. If it errors, the most common fix is in the troubleshooting guide below.

- [ ] **Read this roadmap fully before starting Week 1**
  Reading the whole roadmap now — even the parts about Week 10 — gives your brain a map of where you are going. Destination clarity reduces frustration when the road gets bumpy.

---

## 2. Self-Assessment Quiz — Find Your Starting Point

Answer these five yes/no questions honestly. They will tell you exactly where to enter the curriculum.

**Q1. Can you write a Python function?**
For example: can you write `def add(a, b): return a + b` from memory without looking it up?
- **Yes** — You can skip Week 1 and start at Week 2. Skim the Week 1 notebooks anyway for the biology context.
- **No** — Start at Week 1. This is the right place.

**Q2. Do you know what a matrix is?**
A matrix is a rectangular grid of numbers, like a spreadsheet. Do you know how to multiply two matrices?
- **Yes** — The math in Week 3 (NumPy arrays, dot products) will feel familiar. Move through it quickly.
- **No** — Week 3 will introduce this clearly. Do not worry.

**Q3. Do you know what a protein is?**
- **Yes** — You can skim the Biology Primer section below.
- **No** — Read the Biology Primer section below before opening any notebook. It will make everything click faster.

**Q4. Have you used pandas or NumPy before?**
- **Yes** — Notebooks 00/02 and 00/03 will be fast review. Spend your time on 00/05 and 00/06 instead.
- **No** — Spend full time on those notebooks. They are the foundation for every module that follows.

**Q5. Do you know what a neural network is?**
- **Yes** — Module 05 (`05_deep_learning_finetuning/`) is your gateway. You can treat Weeks 1-4 as reinforcement rather than new material.
- **No** — Follow the week-by-week plan in order. You will understand neural networks completely by Week 7, built from first principles.

---

## 3. Biology Primer — In Plain English (No Jargon)

You do not need a biology degree to do this curriculum. But you do need a mental picture of the things the code is working with. Read this once. It takes about 10 minutes.

### What is a protein?

Think of a protein as a tiny machine built from LEGO bricks. Each brick is called an **amino acid**, and there are 20 different types. A protein is a long chain of these bricks — maybe 100 bricks, maybe 1,000 — snapped together in a specific sequence.

Once the chain is built, something remarkable happens: it folds up on its own, like a piece of origami that folds itself. It twists into coils, bends into sheets, and curls into a 3D shape. That shape is not random. It is determined entirely by the sequence of amino acids.

The shape is what matters. A protein's shape determines what it does.

### Why does shape matter?

Imagine a protein shaped like a bowl. Another molecule — maybe a drug — is shaped like a ball that fits perfectly in that bowl. When the ball lands in the bowl, the protein's behavior changes. Maybe it stops sending a signal it was sending. Maybe it starts doing something it was not doing before.

This is how most drugs work. They are molecules designed to fit into the "bowl" (called a **binding site**) of a target protein. If the drug fits perfectly, it can block the protein from doing something harmful — like helping a cancer cell grow.

To design a good drug, you need to know the shape of the protein. That was the hard part for most of the history of biology.

### What is DNA?

DNA is the instruction manual for building every protein in your body. It is a long string written in a 4-letter alphabet: A, T, G, and C. Specific sections of that string — called **genes** — contain the instructions for one protein. The gene says: "make a chain that goes: Alanine, Glycine, Leucine, Valine..." and so on.

Humans have about 20,000 genes. Each one encodes a protein with a specific job.

### What is gene expression?

Having an instruction manual does not mean every instruction is being followed right now. In a muscle cell, certain genes are "on" (active). In a liver cell, different genes are "on." This is called **gene expression** — the process of reading a gene and using it to build the corresponding protein.

When scientists measure gene expression, they are measuring which proteins a cell is currently making, and how much. This is enormously useful for understanding disease: cancer cells often have the wrong genes switched on.

### What is AlphaFold?

For 50 years, predicting the 3D shape of a protein from its amino acid sequence was one of the hardest unsolved problems in science. In 2020, a structural biology research labs AI system called **AlphaFold** solved it with stunning accuracy. It uses deep learning — trained on all the protein structures ever measured by scientists — to predict the shape of any protein you give it, in minutes.

AlphaFold 3 (the version this curriculum focuses on) goes further: it predicts not just protein shapes but how proteins interact with DNA, RNA, and small drug molecules. This is the core technology behind the work done at computational biology ML teams, the company structural biology research labs spun out specifically to use AlphaFold for drug discovery.

### Why does this matter for medicine?

Combine these ideas: if you know a protein's shape (AlphaFold gives you this), and you know that a disease is caused by that protein behaving badly, you can use ML to design a molecule that fits into the protein and fixes the problem. This is the promise of AI-driven drug discovery. The entire curriculum builds toward your ability to work on this problem.

---

## 4. Week-by-Week Plan

Each week has a target of roughly 10 hours (about 2 hours per day on weekdays, or longer sessions on weekends). The daily targets below assume a 2-hour session. If you have more time, do more. If you have less, do less — but maintain the daily habit.

Every week ends with a "By the end of this week, you can..." statement. Use these as your checkpoints.

---

### Week 1 — Python Basics

**Notebooks:** `00_python_ml_basics/00_`, `00_python_ml_basics/01_`
**Supplement:** 2 hours on the official Python tutorial at https://docs.python.org/3/tutorial/ (Chapters 1-5)

| Day | Task |
|-----|------|
| Mon | Read all markdown cells in notebook 00/00. Do not run code yet. |
| Tue | Run every code cell in 00/00 one at a time. Modify at least one value and re-run. |
| Wed | Attempt the exercises at the end of 00/00. Partial completion is fine. |
| Thu | Work through 00/01 the same way: read first, then run, then modify. |
| Fri | Read Python tutorial Chapters 1-3. |
| Sat | Read Python tutorial Chapters 4-5. Write 3 functions of your own. |
| Sun | Revisit the exercises from both notebooks. Try the ones you skipped. |

**By end of Week 1, you can:**
- Write a Python function with arguments and a return value
- Use lists, dictionaries, and loops without looking them up
- Explain what a variable, a function, and a module are

---

### Week 2 — ML Fundamentals (What Is Learning?)

**Notebooks:** `00_python_ml_basics/02_`, `00_python_ml_basics/05_`, `00_python_ml_basics/08_`
**Supplement:** 3Blue1Brown "Neural Networks" YouTube series (first 4 videos, free)

| Day | Task |
|-----|------|
| Mon | Read and run 00/02 (NumPy and pandas fundamentals). Focus on array slicing. |
| Tue | Finish 00/02 exercises. Understand what a DataFrame is. |
| Wed | Work through 00/05 (what is training? what is a loss function?). |
| Thu | Watch 3Blue1Brown videos 1-2. Then re-read the loss function section in 00/05. |
| Fri | Work through 00/08 (metrics, cross-validation). |
| Sat | Watch 3Blue1Brown videos 3-4. |
| Sun | Write down in your own words: what is gradient descent? what is overfitting? |

**By end of Week 2, you can:**
- Explain what training a model means (minimizing a loss function)
- Describe what gradient descent does in plain English
- Explain why we split data into train and test sets

---

### Week 3 — PyTorch Foundations

**Notebooks:** `00_python_ml_basics/06_`, `00_python_ml_basics/07_`
**Supplement:** HackerRank Python track (https://www.hackerrank.com/domains/python) — complete the "Basic" challenges

| Day | Task |
|-----|------|
| Mon | Read 00/06 (intro to PyTorch). Understand tensors vs. NumPy arrays. |
| Tue | Run 00/06 fully. Pay attention to `.backward()` and `.grad`. |
| Wed | Work through 00/07 (building a simple neural network in PyTorch). |
| Thu | Do HackerRank Python "Basic" challenges (aim for 10). |
| Fri | Modify the neural network in 00/07: change the number of layers, the activation function. |
| Sat | Do HackerRank Python "Intermediate" challenges (aim for 5). |
| Sun | Try to build a 2-layer network from scratch without looking at the notebook. |

**By end of Week 3, you can:**
- Create a PyTorch tensor and do basic operations on it
- Write a simple training loop (forward pass, loss, backward, optimizer step)
- Explain what a gradient is and why backpropagation computes it

---

### Week 4 — DNA and Sequences (Biology as Text)

**Notebooks:** `01_sequence_analysis/01_`, `01_sequence_analysis/02_`
**Mental model:** DNA is just a string. Alignment is like finding the best way to line up two strings.

| Day | Task |
|-----|------|
| Mon | Read 01/01 carefully. The biology primer from Section 3 above will help. |
| Tue | Implement Needleman-Wunsch step by step, following the notebook. |
| Wed | Run the tests in 01/01. Make sure your alignment produces correct results. |
| Thu | Start 01/02 (Smith-Waterman, local alignment). Read first, then code. |
| Fri | Finish 01/02. Understand the difference between local and global alignment. |
| Sat | Look up "BLOSUM62" on Wikipedia. Read the explanation in 01/02. |
| Sun | Attempt the Rosalind problem linked in the notebook. |

**By end of Week 4, you can:**
- Explain what sequence alignment is and why it matters
- Implement Needleman-Wunsch from a description
- Explain the difference between local and global alignment

---

### Week 5 — More Sequences + Genomics (Checkpoint Week)

**Notebooks:** `01_sequence_analysis/03_` through `01_sequence_analysis/06_`, `02_genomics_gene_analysis/01_`
**Note:** This is your first checkpoint. End the week with a self-assessment.

| Day | Task |
|-----|------|
| Mon | Work through 01/03 (BLAST concepts, multiple sequence alignment). |
| Tue | Work through 01/04 (Hidden Markov Models — read slowly, this is conceptually new). |
| Wed | Work through 01/05 and 01/06 (De Bruijn graphs, ORF finding). |
| Thu | Start 02/01 (codon tables, translation from DNA to protein). |
| Fri | Finish 02/01. Write down the central dogma: DNA → RNA → Protein. |
| Sat | **Checkpoint:** Without looking at notes, explain Needleman-Wunsch, what an ORF is, and what a codon is. |
| Sun | Fix any gaps from the checkpoint. Re-read sections that felt fuzzy. |

**By end of Week 5, you can:**
- Find all open reading frames in a DNA sequence
- Explain what a Hidden Markov Model models (sequences with hidden states)
- Translate a DNA codon to an amino acid

---

### Week 6 — Genomics Analysis + Structural Biology

**Notebooks:** `02_genomics_gene_analysis/02_`, `02_genomics_gene_analysis/03_`, `02_genomics_gene_analysis/04_`, `03_protein_structural_biology/01_`

| Day | Task |
|-----|------|
| Mon | Work through 02/02 (variants, SNPs, Hardy-Weinberg equilibrium). |
| Tue | Work through 02/03 (phylogenetics, evolutionary trees). |
| Wed | Work through 02/04 (gene expression analysis, differential expression). |
| Thu | Start 03/01 (PDB parsing, protein structure). This is a big notebook — read all markdown first. |
| Fri | Work through the RMSD and Kabsch algorithm sections of 03/01. |
| Sat | Work through TM-score and the structural comparison section. |
| Sun | Attempt the structural comparison exercise at the end of 03/01. |

**By end of Week 6, you can:**
- Parse a PDB file and extract atom coordinates
- Compute RMSD between two protein structures
- Explain what a SNP is and what Hardy-Weinberg equilibrium says

---

### Week 7 — Deep Learning for Biology

**Notebooks:** `04_ml_bioinformatics/01_`, `05_deep_learning_finetuning/01_`

| Day | Task |
|-----|------|
| Mon | Work through 04/01 (ML for gene expression — the p>>n problem, PCA). |
| Tue | Finish 04/01. Understand why dimensionality reduction matters when you have more features than samples. |
| Wed | Start 05/01 (deep learning for biology). Read all markdown. This is a long notebook. |
| Thu | Work through the CNN section of 05/01. |
| Fri | Work through the Transformer section of 05/01. Focus on attention mechanism. |
| Sat | Work through the LoRA and fine-tuning sections. |
| Sun | Work through the EarlyStopping and gradient flow sections. Attempt the mastery check. |

**By end of Week 7, you can:**
- Explain what PCA does and when you would use it
- Describe how attention works in a transformer (query, key, value)
- Explain what LoRA is and why it is more efficient than full fine-tuning

---

### Week 8 — Graphs + AlphaFold3 Introduction

**Notebooks:** `06_structural_ml_gnns/01_`, `06_structural_ml_gnns/02_`, `07_alphafold3_core/00_`, `07_alphafold3_core/01_`

| Day | Task |
|-----|------|
| Mon | Work through 06/01 (protein as a graph, message passing). |
| Tue | Work through 06/02 (equivariance — why rotating a protein should not change predictions). |
| Wed | Read 07/00 (zero-to-hero AlphaFold3 on-ramp). This is mostly explanatory — read it like a textbook. |
| Thu | Start 07/01 (Pairformer architecture). Read the architecture overview cells. |
| Fri | Work through the triangle attention section of 07/01. Draw the attention pattern on paper. |
| Sat | Work through the outer product mean section. |
| Sun | Attempt the Pairformer exercise. Partial credit is fine. |

**By end of Week 8, you can:**
- Explain what message passing in a GNN does
- Define E(3)-equivariance in plain English
- Describe the high-level purpose of the Pairformer in AlphaFold3

---

### Week 9 — AlphaFold3 Deep Dive + Practical Problems

**Notebooks:** `07_alphafold3_core/02_` through `07_alphafold3_core/05_`, `08_practical_problems/01_` through `08_practical_problems/05_`

| Day | Task |
|-----|------|
| Mon | Work through 07/02 (FAPE loss — how AlphaFold3 measures structural accuracy). |
| Tue | Work through 07/03 (diffusion model for structure generation). |
| Wed | Work through 07/04 and 07/05 (training loop, confidence metrics). |
| Thu | Work through 08/01 and 08/02 (combined HackerRank + Rosalind problems). |
| Fri | Work through 08/03 and 08/04. |
| Sat | Work through 08/05. |
| Sun | Pick one problem from Week 9 that challenged you and solve it again from scratch. |

**By end of Week 9, you can:**
- Explain what FAPE loss measures
- Describe the diffusion process for protein structure generation
- Solve a set of practical bioinformatics coding problems under time pressure

---

### Week 10 — Advanced Topics + Capstone

**Notebooks:** Modules 09-16 (one per day), then `17_capstone_project/`

| Day | Task |
|-----|------|
| Mon | 09/01 (ML teaching — bias-variance, learning curves) + 10/01 (OpenFold code walkthrough) |
| Tue | 10/02 (LoRA fine-tuning capstone) + 11/01 (membrane proteins) |
| Wed | 12/01 (generative models) + 13/01 (Bayesian methods) |
| Thu | 14/01 (reinforcement learning for drug design) + 15/01 (self-supervised learning) |
| Fri | 16/01 (MLOps and deployment) |
| Sat | Read all markdown cells of 17/00 (EGFR capstone). Understand the end-to-end pipeline. |
| Sun | Run the capstone notebook. Celebrate. |

**By end of Week 10, you can:**
Everything in the Motivation section below.

---

## 5. "I'm Stuck" Troubleshooting Guide

Do not panic when things break. Every programmer, at every level, spends a significant fraction of their time debugging. Here are the most common problems you will encounter and exactly how to fix them.

---

**Error: `ModuleNotFoundError: No module named 'torch'`** (or any other package)

This means a package is not installed. Fix:
```bash
pip install -r requirements.txt
```
If that does not work, try installing the specific package:
```bash
pip install torch
```
If you are in a Jupyter notebook and pip is not working, try:
```python
import subprocess
subprocess.run(["pip", "install", "torch"])
```

---

**Error: `CUDA not available` or GPU-related warnings**

This means your computer does not have an NVIDIA GPU (or the CUDA driver is not set up). This is fine for Weeks 1-6. The notebooks will run on CPU, just more slowly.

For Weeks 7-10, if training is too slow on CPU, switch to Google Colab (free GPU) or see `CLOUD_SETUP.md` in this repository for instructions on using a cloud VM.

You can suppress the warning by running this at the top of your notebook:
```python
import torch
device = torch.device('cpu')  # explicitly use CPU
```

---

**Error: `MemoryError` or notebook crashes mid-run**

Your computer ran out of RAM. Solutions in order of ease:
1. Reduce `batch_size` in the training cell (try cutting it in half)
2. Restart the kernel and re-run from the beginning
3. Switch to Google Colab (which has more RAM than most laptops)

---

**A concept is unclear after reading the notebook**

Look up the concept in `GLOSSARY.md` first — every major term is defined there.

Then try these resources by topic:

| Topic | Best Resource |
|-------|---------------|
| Python basics | https://docs.python.org/3/tutorial/ |
| NumPy / pandas | https://pandas.pydata.org/docs/getting_started/ |
| Linear algebra | 3Blue1Brown "Essence of Linear Algebra" on YouTube |
| Neural networks | 3Blue1Brown "Neural Networks" series on YouTube |
| Transformers | "The Illustrated Transformer" by Jay Alammar (Google it) |
| Protein structure | "Introduction to Protein Structure" by Branden & Tooze (check library) |
| AlphaFold | The original AlphaFold2 Nature paper (free on PubMed) |
| Sequence alignment | Rosalind.info exercises with explanations |

---

**An exercise feels impossible**

This is completely normal. Here is the exact process to follow:

1. Re-read the problem statement slowly. Write down in plain English what you are trying to compute.
2. Look at the first hint in the notebook (most exercises have 2-3 hints).
3. Write pseudocode — English steps, not Python — before writing any code.
4. Implement the pseudocode one line at a time. Print intermediate values.
5. If still stuck after 30 minutes, look at the second hint.
6. If still stuck after another 30 minutes: stop, sleep on it. Seriously. The brain consolidates during sleep, and you will often wake up with the answer.
7. If still stuck the next day: post to the Rosalind forum or Stack Overflow with your specific error and what you have tried.

The measure of a good programmer is not solving exercises immediately. It is solving them eventually, by being systematic and persistent.

---

**My notebook runs but produces wrong results**

This is a logic error, not a Python error. Debugging strategy:
1. Print the shape of every tensor/array at each step: `print(x.shape)`
2. Print the min and max values: `print(x.min(), x.max())`
3. Run on a tiny example you can verify by hand (e.g., a 3x3 matrix instead of 100x100)
4. Add `assert` statements to check invariants: `assert scores.shape == (batch_size, num_classes)`

---

## 6. Study Session Template

Every 2-hour session should follow this structure. The exact timing is a guideline — adjust based on how the material flows.

```
0:00 — 0:10  WARM UP
             Review the mastery check from your last session.
             Try to answer Q1-Q3 without looking at your notes.
             Write down anything you could not remember — that is today's focus.

0:10 — 0:50  READ
             Read all markdown cells of the new notebook from top to bottom.
             Do not run any code yet.
             Highlight (or write down) every term you do not recognize.
             Look up those terms in GLOSSARY.md.

0:50 — 1:30  RUN AND MODIFY
             Run each code cell one at a time.
             After running each cell, ask: "What would happen if I changed X?"
             Change one value. Re-run. Observe the difference.
             Examples of good modifications:
               - Change the learning rate from 0.001 to 0.1. What happens to training?
               - Change the number of attention heads. Does it still work?
               - Feed a different protein sequence. What changes?

1:30 — 1:50  ATTEMPT
             Work on the exercise at the end of the notebook.
             Partial completion is fine.
             Your goal is not to finish — it is to identify where you get stuck.
             That sticking point is the most valuable information.

1:50 — 2:00  CLOSE
             Attempt mastery check questions 1-3 only.
             Write down in one sentence: "Today I learned that ___"
             Write down in one sentence: "I am still unclear about ___"
             That second sentence is the first thing you look up next session.
```

Consistency beats intensity. Two focused hours every day will take you further than one 12-hour marathon on the weekend.

---

## 7. What You Will Be Able to Say After 10 Weeks

These are not vague promises. These are specific, concrete things you will be able to say truthfully in a technical interview or a research meeting.

**On algorithms and mathematics:**
- "I implemented Needleman-Wunsch from scratch, including the traceback step, and used it to align SARS-CoV-2 spike protein sequences."
- "I built a Kabsch algorithm implementation that finds the optimal rotation matrix to align two protein structures, and I understand the SVD-based derivation."
- "I can explain why FAPE loss is used instead of RMSD for training AlphaFold, and what makes it frame-invariant."

**On deep learning:**
- "I implemented triangle attention, including the triangle multiplicative update, and can explain why pairwise representations need triangular symmetry."
- "I fine-tuned ESM-2 protein language model embeddings for mutation effect prediction using LoRA — reducing trainable parameters by 97% while retaining >95% of performance."
- "I implemented a diffusion model for protein backbone generation using DDPM, including the forward noising process and learned denoising network."

**On engineering:**
- "I wrote a GNN-based protein structure predictor with message passing over a k-nearest-neighbor residue graph, with E(3)-equivariant updates."
- "I built an end-to-end ML pipeline: PDB parsing → feature extraction → model training → structure evaluation — integrated in a single reproducible notebook."
- "I understand the AlphaFold3 training loop at the code level, including gradient accumulation, BF16 mixed precision, and the confidence head training objective."

**On the big picture:**
- "I can explain the central dogma of molecular biology (DNA → RNA → protein), and I understand where each bioinformatics tool fits in that pipeline."
- "I can explain why protein structure prediction matters for drug discovery, and how AlphaFold3's ability to model protein-ligand interactions changes the drug design workflow."
- "I can describe the differences between AlphaFold2, AlphaFold3, OpenFold, ESMFold, and Boltz-2, and explain the architectural choices that distinguish them."

**You are building toward a role at a company like computational biology ML teams, structural biology research labs, or any structural biology ML lab.** The people who get those roles are not necessarily the smartest people in the room. They are the ones who showed up consistently, built things from scratch, and can explain what they built to someone else. This roadmap gives you exactly that.

Start today. Open notebook 00/00. Run Cell 1.
