# Zero to Hero — Complete Learning Path
## From Absolute Beginner to Protein ML Researcher

This guide maps the exact path from zero background to hero level. Every resource listed is **free**. Estimated total time: 6–18 months depending on your pace.

---

## Read This First

If you are truly starting from zero, do **not** measure success by whether you can reproduce every advanced notebook in this repository.

A realistic definition of success is:
- by the end of the **Beginner** stage, you can write Python, use NumPy/Pandas, and build correct ML pipelines
- by the end of the **Intermediate** stage, you can explain the core bioinformatics and deep-learning concepts in your own words
- by the end of the **Advanced** stage, you can read the AF3-style and protein-model notebooks conceptually, even if you still need to revisit implementation details later

For most students, modules `11-16` should be treated as **advanced electives** on the first pass.

---

## The Four Levels

| Level | Description | Time | You Can Do |
|-------|-------------|------|-----------|
| **Zero** | No coding, no math, no ML | — | Nothing yet |
| **Beginner** | Python + basic ML | 0–3 months | Run sklearn pipelines, parse FASTA files |
| **Intermediate** | Deep learning + bioinformatics | 3–8 months | Train CNNs, implement alignment algorithms, use ESM2 |
| **Advanced** | Transformers + structural biology | 8–14 months | Fine-tune protein LMs, implement Pairformer, run RFdiffusion |
| **Hero** | Research-level | 14–18 months | Design novel architectures, contribute to AlphaFold, publish |

---

## LEVEL 0 -> BEGINNER (Months 1–3)

### Week 1–2: Python Basics
**Goal:** Write Python programs that read files, process strings, use lists/dicts

| Resource | Type | Time | Link |
|----------|------|------|------|
| CS50P (Harvard) | Video course | 20h | [cs50.harvard.edu/python](https://cs50.harvard.edu/python/) |
| Automate the Boring Stuff | Free book | 15h | [automatetheboringstuff.com](https://automatetheboringstuff.com/) |
| Kaggle Python Course | Interactive | 5h | [kaggle.com/learn/python](https://www.kaggle.com/learn/python) |
| Python Official Tutorial | Docs | 8h | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |

**Milestone:** Can you write a Python script that reads a FASTA file and counts nucleotides? Go to Week 3

---

### Week 3–4: Math Foundations
**Goal:** Understand vectors, matrices, derivatives, probability

| Resource | Type | Time | Link |
|----------|------|------|------|
| 3Blue1Brown Linear Algebra | YouTube | 4h | [Essence of Linear Algebra playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) |
| 3Blue1Brown Calculus | YouTube | 3h | [Essence of Calculus playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) |
| Harvard Stat 110 | Course notes + video | 12h+ | [stat110.hsites.harvard.edu](https://stat110.hsites.harvard.edu/) |
| Khan Academy Statistics | Interactive | 10h | [khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability) |
| **This curriculum:** 00/08 Math Foundations | Notebook | 12h | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

**Milestone:** Can you explain what a matrix eigenvector is and derive the chain rule? Go to Month 2

---

### Month 2: NumPy, Pandas, and Data Science
**Goal:** Work with data programmatically, make plots, understand ML pipelines

| Resource | Type | Time | Link |
|----------|------|------|------|
| Kaggle Pandas Course | Interactive | 4h | [kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas) |
| Kaggle Data Visualization | Interactive | 4h | [kaggle.com/learn/data-visualization](https://www.kaggle.com/learn/data-visualization) |
| NumPy Documentation | Docs | 5h | [numpy.org/learn](https://numpy.org/learn/) |
| **This curriculum:** 00/01 Python Core | Notebook | 8h | `00_python_ml_basics/01_python_core_for_bioinformatics.ipynb` |

---

### Month 3: Machine Learning Fundamentals
**Goal:** Train, evaluate, and tune ML models; understand overfitting and cross-validation

| Resource | Type | Time | Link |
|----------|------|------|------|
| scikit-learn MOOC (Inria) | Course | 15h | [inria.github.io/scikit-learn-mooc](https://inria.github.io/scikit-learn-mooc/) |
| Andrew Ng ML Specialization | Course (audit free) | 60h | [coursera.org/specializations/machine-learning-introduction](https://www.coursera.org/specializations/machine-learning-introduction) |
| Kaggle Intro to ML | Interactive | 3h | [kaggle.com/learn/intro-to-machine-learning](https://www.kaggle.com/learn/intro-to-machine-learning) |
| StatQuest ML playlist | YouTube | 20h | [StatQuest channel](https://www.youtube.com/c/joshstarmer) |
| **This curriculum:** 00/02 ML Fundamentals | Notebook | 10h | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| **This curriculum:** 09/01 Model Diagnostics | Notebook | 8h | `09_ml_teaching_essentials/01_model_diagnostics.ipynb` |

**Milestone:** Can you train a classifier on the Titanic dataset, tune hyperparameters, and report AUC-ROC? You are BEGINNER level.

---

## BEGINNER -> INTERMEDIATE (Months 3–8)

### Month 4: PyTorch and Deep Learning
**Goal:** Implement neural networks from scratch, understand backpropagation

| Resource | Type | Time | Link |
|----------|------|------|------|
| Neural Networks: Zero to Hero (Karpathy) | YouTube | 20h | [youtube.com/playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) |
| fast.ai Practical Deep Learning Part 1 | Course (free) | 30h | [course.fast.ai](https://course.fast.ai/) |
| PyTorch Official Tutorials | Docs | 8h | [pytorch.org/tutorials](https://pytorch.org/tutorials/) |
| MIT 6.S191 Deep Learning | Course (free) | 20h | [introtodeeplearning.com](https://introtodeeplearning.com/) |
| **This curriculum:** 00/06 PyTorch Fundamentals | Notebook | 12h | `00_python_ml_basics/06_pytorch_fundamentals.ipynb` |
| **This curriculum:** 05/01 Deep Learning | Notebook | 15h | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |

Teaching advice:
- First pass: focus on tensors, gradients, training loops, and overfitting vs generalization.
- Do not let transformers or LoRA distract you before you are comfortable with a small MLP or CNN.

---

### Month 5: Bioinformatics Sequence Analysis
**Goal:** Implement alignment algorithms, solve Rosalind problems, understand genomics

| Resource | Type | Time | Link |
|----------|------|------|------|
| Rosalind.info | Interactive | 30h | [rosalind.info](https://rosalind.info/problems/list-view/) — solve problems in order |
| Bioinformatics Algorithms (free) | Book | 20h | [bioinformaticsalgorithms.org](https://www.bioinformaticsalgorithms.org/) |
| Ben Langmead Johns Hopkins lectures | YouTube | 15h | [youtube.com/c/BenLangmead](https://www.youtube.com/c/BenLangmead) |
| **This curriculum:** 01/01 Alignment | Notebook | 10h | `01_sequence_analysis/01_alignment_algorithms.ipynb` |
| **This curriculum:** 01/07 HMMs | Notebook | 15h | `01_sequence_analysis/07_hidden_markov_models.ipynb` |
| **This curriculum:** 08/01–08/05 Practice | Notebooks | 20h | `08_practical_problems/` all 5 notebooks |

---

### Month 6: Structural Biology + GNNs
**Goal:** Parse protein structures, implement GNNs, understand contact maps

| Resource | Type | Time | Link |
|----------|------|------|------|
| RCSB PDB-101 | Guided tutorials | 8h | [pdb101.rcsb.org/learn/guide-to-understanding-pdb-data](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data) |
| PDB-101 Structural Biology tutorials | Web | 10h | [pdb101.rcsb.org](https://pdb101.rcsb.org/) |
| CS224W Stanford GNN Course | YouTube | 20h | [youtube.com/playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn) |
| Graph Representation Learning (Hamilton) | Free book | 15h | [cs.mcgill.ca/~wlh/grl_book](https://www.cs.mcgill.ca/~wlh/grl_book/) |
| **This curriculum:** 03/01 Structural Biology | Notebook | 12h | `03_protein_structural_biology/01_structure_analysis.ipynb` |
| **This curriculum:** 06/01 Structure ML | Notebook | 15h | `06_structural_ml_gnns/01_structure_ml.ipynb` |
| **This curriculum:** 06/02 GNN Deep Dive | Notebook | 20h | `06_structural_ml_gnns/02_gnn_deep_dive.ipynb` |

---

### Month 7–8: Classical ML + Statistics Deep Dive
**Goal:** Master SVMs, Gaussian Processes, XGBoost, Bayesian methods

| Resource | Type | Time | Link |
|----------|------|------|------|
| Elements of Statistical Learning (free PDF) | Book | 30h | [hastie.su.domains/ElemStatLearn](https://hastie.su.domains/ElemStatLearn/) |
| Probabilistic ML (Murphy, free PDF) | Book | 20h | [probml.github.io/pml-book](https://probml.github.io/pml-book/) |
| StatQuest Bayesian stats | YouTube | 8h | [StatQuest Bayesian playlist](https://www.youtube.com/c/joshstarmer) |
| **This curriculum:** 00/09 Classical ML Advanced | Notebook | 12h | `00_python_ml_basics/09_classical_ml_advanced.ipynb` |
| **This curriculum:** 13/01 Bayesian Methods | Notebook | 12h | `13_bayesian_methods/01_bayesian_ml_uncertainty.ipynb` |

**Milestone:** Can you implement SVM from the dual formulation, run GP-BO on a toy protein fitness landscape, and explain UMAP vs t-SNE? You are INTERMEDIATE level.

---

## INTERMEDIATE -> ADVANCED (Months 8–14)

### Month 9: Transformers and Protein Language Models
**Goal:** Implement attention from scratch, fine-tune ESM2 with LoRA

| Resource | Type | Time | Link |
|----------|------|------|------|
| Attention Is All You Need | Paper | 3h | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) |
| Illustrated Transformer (Jay Alammar) | Blog | 3h | [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) |
| Stanford CS224N NLP with DL | Course (free) | 40h | [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/) |
| Hugging Face NLP Course | Interactive | 20h | [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course/chapter1/1) |
| LoRA Paper (Hu 2021) | Paper | 2h | [arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685) |
| **This curriculum:** 05/01 DL & Fine-tuning | Notebook | 15h | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| **This curriculum:** 15/01 Self-Supervised Learning | Notebook | 15h | `15_self_supervised_learning/01_contrastive_ssl.ipynb` |

Teaching advice:
- First pass: understand attention, masking, embeddings, and why unlabeled sequence data matters.
- Second pass: study the implementation details of SSL losses and transformer blocks.

---

### Month 10: AlphaFold3 Architecture
**Goal:** Understand and implement Pairformer, FAPE loss, triangle attention

| Resource | Type | Time | Link |
|----------|------|------|------|
| AlphaFold2 paper (Jumper 2021) | Paper | 5h | [nature.com/articles/s41586-021-03819-2](https://www.nature.com/articles/s41586-021-03819-2) |
| AlphaFold3 paper (Abramson 2024) | Paper | 5h | [nature.com/articles/s41586-024-07487-w](https://www.nature.com/articles/s41586-024-07487-w) |
| AF2 explained — Yannic Kilcher | YouTube | 2h | [youtube.com/watch?v=nGVFbPKrRWQ](https://www.youtube.com/watch?v=nGVFbPKrRWQ) |
| OpenFold codebase | GitHub | 10h | [github.com/aqlaboratory/openfold](https://github.com/aqlaboratory/openfold) |
| **This curriculum:** 07/01–07/04 AF3 Core | Notebooks | 40h | `07_alphafold3_core/` all 4 notebooks |

Teaching advice:
- Beginners should treat this as a **conceptual first pass**.
- It is enough on day one to explain what Pairformer, FAPE, PAE, and diffusion are doing at a high level.
- Come back for tensor-level implementation only after the core path feels easy.

---

### Month 11: Generative Models for Protein Design
**Goal:** Implement DDPM, understand RFdiffusion, design proteins with diffusion

| Resource | Type | Time | Link |
|----------|------|------|------|
| Lilian Weng Diffusion Blog | Blog | 3h | [lilianweng.github.io/posts/2021-07-11-diffusion-models](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) |
| DDPM paper (Ho 2020) | Paper | 3h | [arxiv.org/abs/2006.11239](https://arxiv.org/abs/2006.11239) |
| RFdiffusion paper (Watson 2023) | Paper | 3h | [nature.com/articles/s41586-023-06415-8](https://www.nature.com/articles/s41586-023-06415-8) |
| Annotated Diffusion (HuggingFace) | Blog + code | 5h | [huggingface.co/blog/annotated-diffusion](https://huggingface.co/blog/annotated-diffusion) |
| **This curriculum:** 12/01 Diffusion Models | Notebook | 15h | `12_generative_models/01_diffusion_protein_design.ipynb` |

---

### Month 12: Reinforcement Learning for Design
**Goal:** Learn how sequential decision-making and reward-driven search apply to protein optimization

| Resource | Type | Time | Link |
|----------|------|------|------|
| Sutton & Barto RL book | Book | 20h | [incompleteideas.net/book](http://incompleteideas.net/book/the-book-2nd.html) |
| David Silver RL Course | Video course | 20h | [youtube.com/playlist](https://www.youtube.com/playlist?list=PLqYmG7hTraZBKeNJ-JE_eyJHZ7XgBoAyb) |
| OpenAI Spinning Up | Docs + code | 8h | [spinningup.openai.com](https://spinningup.openai.com/en/latest/) |
| **This curriculum:** 14/01 Reinforcement Learning | Notebook | 15h | `14_reinforcement_learning/01_rl_protein_design.ipynb` |

---

### Month 13: MLOps and Deployment
**Goal:** Learn how to ship, serve, and monitor the models you trained in earlier modules

| Resource | Type | Time | Link |
|----------|------|------|------|
| Made With ML | Course | 12h | [madewithml.com](https://madewithml.com/) |
| Full Stack Deep Learning | Course | 15h | [fullstackdeeplearning.com](https://fullstackdeeplearning.com/) |
| FastAPI Tutorial | Docs | 4h | [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/) |
| **This curriculum:** 16/01 MLOps for Protein ML | Notebook | 15h | `16_mlops_deployment/01_mlops_for_protein_ml.ipynb` |

---

### Month 14–15: Capstone Projects
**Goal:** Build something real — fine-tune, evaluate, publish or deploy

| Resource | Type | Time | Link |
|----------|------|------|------|
| HuggingFace PEFT docs | Docs | 5h | [huggingface.co/docs/peft](https://huggingface.co/docs/peft) |
| ProteinGym benchmark | Dataset | 5h | [github.com/OATML-Markslab/ProteinGym](https://github.com/OATML-Markslab/ProteinGym) |
| Novozymes Enzyme Stability | Kaggle | 20h | [kaggle.com/c/novozymes-enzyme-stability-prediction](https://www.kaggle.com/c/novozymes-enzyme-stability-prediction) |
| **This curriculum:** 10/01 Fine-tuning Capstone | Notebook | 25h | `10_openfold3_finetuning/01_protein_structure_finetuning.ipynb` |
| **This curriculum:** 11/01 Membrane Proteins | Notebook | 25h | `11_membrane_protein_dynamics/01_membrane_protein_dynamics.ipynb` |

**Milestone:** Can you fine-tune ESM2 with LoRA on a protein fitness task, evaluate on ProteinGym, and get competitive Spearman correlation? You are ADVANCED level.

---

## ADVANCED -> HERO (Months 14–18)

### Read Papers Like Breathing
**Goal:** Stay current with the field, read and re-implement papers weekly

| Habit | Frequency | Resource |
|-------|-----------|---------|
| Read 1 new paper | Weekly | [Papers With Code — Proteins](https://paperswithcode.com/task/protein-structure-prediction) |
| Reproduce 1 paper | Monthly | Pick from top venues: NeurIPS, ICML, Nature Methods |
| Contribute to open source | Monthly | OpenFold, Boltz, ProteinMPNN |
| Write blog post | Monthly | Distill.pub style, or personal blog |

**Must-read papers for hero level:**
- ESM2 (Lin 2023, Science) — protein language model
- ProteinMPNN (Dauparas 2022, Science) — inverse folding
- FrameDiff (Yim 2023) — SE(3) backbone diffusion
- Chroma (Ingraham 2023) — conditional protein design
- ESM3 (Hayes 2024) — multimodal protein model

### Top Conferences to Follow
| Conference | Focus | Top Papers |
|------------|-------|-----------|
| NeurIPS | General ML | Protein applications every year |
| ICML | General ML | Equivariant GNNs, protein generation |
| ICLR | Representation learning | Language models, attention |
| Nature Methods | Computational biology | AlphaFold, protein design |
| RECOMB | Computational genomics | Sequence analysis, genome assembly |
| ISMB | Bioinformatics | All areas of computational biology |

### Building Your Portfolio
1. **Kaggle:** Achieve Gold on Novozymes Enzyme Stability + CAFA-5
2. **GitHub:** Reproduce 3 key papers with clean code
3. **HuggingFace:** Release a fine-tuned protein model with a demo Space
4. **Blog:** Write 5 technical posts explaining ML concepts to biologists
5. **Research:** Submit to a workshop (ICML CompBio, NeurIPS ML4Molecules)

**Milestone:** Can you implement a novel architecture, run experiments comparing to baselines, and write a coherent methods section? You are HERO level.

---

## Free Books — The Essential Library

All of these are legally free online:

| Book | Topic | Level | Link |
|------|-------|-------|------|
| Mathematics for ML (Deisenroth) | Math | Beginner | [mml-book.github.io](https://mml-book.github.io/) |
| Deep Learning (Goodfellow) | DL Theory | Intermediate | [deeplearningbook.org](https://www.deeplearningbook.org/) |
| Probabilistic ML (Murphy) | Bayesian ML | Intermediate | [probml.github.io/pml-book](https://probml.github.io/pml-book/) |
| Elements of Statistical Learning | Classical ML | Intermediate | [hastie.su.domains/ElemStatLearn](https://hastie.su.domains/ElemStatLearn/) |
| Introduction to Statistical Learning (ISLR2) | Applied ML | Beginner | [statlearning.com](https://www.statlearning.com/) |
| Biological Sequence Analysis (Durbin) | Bioinformatics | Intermediate | PDF available from publishers |
| Bioinformatics Algorithms (Compeau) | Algorithms | Beginner | [bioinformaticsalgorithms.org](https://www.bioinformaticsalgorithms.org/) |
| Graph Representation Learning (Hamilton) | GNNs | Intermediate | [cs.mcgill.ca/~wlh/grl_book](https://www.cs.mcgill.ca/~wlh/grl_book/) |
| Gaussian Processes for ML (Rasmussen) | Bayesian | Advanced | [gaussianprocess.org/gpml](http://www.gaussianprocess.org/gpml/) |
| Convex Optimization (Boyd) | Optimization | Advanced | [stanford.edu/~boyd/cvxbook](https://stanford.edu/~boyd/cvxbook/) |

---

## YouTube Channels — Essential Subscriptions

| Channel | Focus | Level | Best Playlist |
|---------|-------|-------|---------------|
| 3Blue1Brown | Math visualization | Beginner | Linear Algebra, Calculus, Neural Networks |
| StatQuest (Josh Starmer) | ML concepts | Beginner | Machine Learning, Statistics |
| Andrej Karpathy | DL implementation | Intermediate | Zero to Hero series |
| Yannic Kilcher | Paper walkthroughs | Advanced | AlphaFold, GPT, RLHF papers |
| Ari Seff | DL theory | Intermediate | Diffusion, VAEs |
| Philipp Hennig | Probabilistic ML | Advanced | Tubingen ML lectures |
| Ben Langmead | Bioinformatics | Intermediate | Alignment, sequencing |
| CS231N Stanford | Computer Vision | Intermediate | Full course |
| CS224W Stanford | GNNs | Intermediate | Full course |
| MIT 6.S191 | DL applications | Beginner | Full course |

---

## Practice Platforms

| Platform | Focus | Why Use It |
|----------|-------|-----------|
| [Rosalind.info](https://rosalind.info) | Bioinformatics algorithms | 284 problems, immediate feedback |
| [HackerRank](https://hackerrank.com) | Python, algorithms, ML | Certification recognized by employers |
| [Kaggle](https://kaggle.com) | Applied ML | Real datasets, competitions, notebooks |
| [LeetCode](https://leetcode.com) | Algorithms (coding interviews) | DSA problems for ML engineering roles |
| [Kaggle Learn](https://kaggle.com/learn) | Courses | Free, interactive, certificate |
| [fast.ai](https://course.fast.ai) | Practical DL | Top-down, learn by building |

---

## Weekly Schedule Template

For someone studying 10–15 hours/week:

| Day | Activity | Time |
|-----|----------|------|
| Monday | Read 1 paper / blog post | 1.5h |
| Tuesday | Work through curriculum notebook | 2h |
| Wednesday | Rosalind / HackerRank problems | 1.5h |
| Thursday | Kaggle — work on a competition or course | 2h |
| Friday | Implement from scratch (no copying) | 2h |
| Saturday | Review, debug, clean up code | 2h |
| Sunday | Write notes / blog post draft | 1h |

---

## Skill Checkpoints

Use these to assess your level honestly:

### Beginner Checkpoint
- [ ] Parse a FASTA file and compute GC content without looking up syntax
- [ ] Implement k-fold cross-validation from scratch (no sklearn)
- [ ] Train a logistic regression on a genomics dataset and report AUC-ROC
- [ ] Solve 20 HackerRank Python problems

### Intermediate Checkpoint
- [ ] Implement Needleman-Wunsch alignment with traceback (no BioPython)
- [ ] Train a 2-layer MLP in PyTorch from scratch and visualize gradient flow
- [ ] Build a protein contact graph and apply message passing
- [ ] Solve 50 Rosalind problems
- [ ] Implement Forward + Viterbi algorithms for an HMM

### Advanced Checkpoint
- [ ] Fine-tune ESM2 with LoRA on a protein fitness task (evaluate on ProteinGym)
- [ ] Implement triangle attention from scratch, verify output shapes for N=32
- [ ] Run RFdiffusion to design a protein binder, evaluate with ESMFold
- [ ] Get top-25% on Novozymes Kaggle competition
- [ ] Read and understand 80% of an AlphaFold3 methods section

### Hero Checkpoint
- [ ] Implement Pairformer from scratch in PyTorch, train on contact prediction
- [ ] Submit a paper / workshop abstract on protein ML
- [ ] Release a HuggingFace model that others actually use
- [ ] Explain FAPE loss, SE(3) diffusion, and LoRA rank theory in a whiteboard interview
