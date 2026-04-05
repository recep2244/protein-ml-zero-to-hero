# How to Become an Independent Learner in Bioinformatics ML
## A Guide Written for MIT, Stanford, and Harvard-Level Rigor

This guide is for students who want to stop being curriculum-followers and become
researchers — people who can encounter an unknown problem and figure it out alone.

---

## Part 1: The Mental Model

### What Independent Learning Actually Means

At MIT, Stanford, and Harvard, the best students don't just complete assignments.
They ask: *"What is the deepest question hiding inside this problem?"*

For this curriculum, that deepest question is:
> **"Given a biological sequence or structure, can I predict function — and do I understand
> the math, biology, and code well enough to improve the prediction?"**

Every notebook in this curriculum is a step toward answering that question.
Independent learning means you can take ANY new paper in this space (e.g., ESM-3, RFdiffusion,
Boltz-2) and understand it within a week — without a teacher.

### The 4 Levels of Understanding

Use this rubric before and after every notebook:

| Level | You Can... | Example for Triangle Attention |
|-------|-----------|-------------------------------|
| 1 — Name | Say what it is | "Triangle attention is in AlphaFold" |
| 2 — Explain | Describe it correctly to a peer | "It updates edge (i,k) using all paths through j" |
| 3 — Implement | Write it from scratch | `z[i,k] += sum_j attn(z[i,j],z[j,k]) * v(z[j,k])` |
| 4 — Critique | Know when it fails, what alternatives exist | "Scales O(N³); chunking fixes memory but not compute; linear attention is an alternative" |

**Target:** Level 3 for core topics (AF3, GNNs, fine-tuning). Level 2 for supporting topics.
Level 4 for your specialization area.

---

## Part 2: Finding Answers When You're Stuck

### Decision Tree: "I Don't Understand X"

```
Is X a math concept (attention, FAPE, NB distribution)?
├── Yes → Check: Stanford CS229 notes, Harvard AM207, MIT 18.065 lecture notes
│         Then: Wikipedia (for formal definition), then a worked example in Python

Is X a biology concept (protein structure, RNA-seq, variant)?
├── Yes → Check: MIT 7.91J OCW lecture slides (free)
│         Then: StatQuest YouTube (Josh Starmer; explains everything visually)
│         Then: iBiology.org (free video courses from top researchers)

Is X a coding/PyTorch error?
├── Yes → Step 1: Read the FULL traceback (last 3 lines are the cause)
│         Step 2: Paste exact error + 5 lines of context into Google
│         Step 3: Check PyTorch Discuss forum (discuss.pytorch.org)
│         Step 4: Check GitHub Issues for the specific library
│         Step 5: Write a minimal reproducer (< 20 lines) before asking for help

Is X a paper you can't understand?
└── Yes → Read in this order:
           (1) Abstract → (2) Figures (each with caption) → (3) Results summary
           → (4) Methods Algorithm boxes → (5) full Methods → (6) Supplement
           Never read linearly from title to end.
```

### The Best Free Resources by Topic

#### Mathematics
| Topic | Best Free Resource | Level |
|-------|-------------------|-------|
| Linear algebra | [MIT 18.06 (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Foundations |
| Probability | [Harvard STAT110 (Blitzstein)](https://stat110.net/) — free videos + book | Foundations |
| Optimization | [Stanford EE364a Convex Opt](https://web.stanford.edu/class/ee364a/) — Boyd notes | Intermediate |
| Information theory | [MIT 6.441 Lecture Notes](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/) | Advanced |

#### Machine Learning
| Topic | Best Free Resource | Level |
|-------|-------------------|-------|
| Classical ML | [Stanford CS229 notes (Ng)](https://cs229.stanford.edu/) — gold standard | Foundations |
| Deep learning | [MIT 6.S191 (annual)](https://introtodeeplearning.com/) — best video lectures | Foundations |
| NLP/Transformers | [Stanford CS224n](https://web.stanford.edu/class/cs224n/) | Intermediate |
| GNNs | [Stanford CS224W](https://web.stanford.edu/class/cs224w/) | Intermediate |
| Bayesian ML | [Harvard AM207](https://am207.github.io/2018fall/) | Advanced |
| RL | [Stanford CS234](https://web.stanford.edu/class/cs234/) | Intermediate |
| Generative models | [MIT 6.S192](https://mit-deep-learning.com/) | Advanced |

#### Bioinformatics
| Topic | Best Free Resource | Level |
|-------|-------------------|-------|
| Sequence analysis | [MIT 7.91J (OCW)](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) | All levels |
| Computational biology | [Bioinformatics Algorithms (free online)](https://www.bioinformaticsalgorithms.org/) | Intermediate |
| Structural biology | [iBiology Protein Structure](https://www.ibiology.org/biochemistry/protein-structure/) | Foundations |
| RNA-seq | [StatQuest RNA-seq series](https://www.youtube.com/playlist?list=PLblh5JKOoLUKMmxlpHx3Ntk36e6Q3dOec) | Intermediate |
| Drug discovery ML | [MIT 6.874](https://mit6874.github.io/) | Advanced |

#### AlphaFold Specifically
| Resource | Time | What You Get |
|----------|------|-------------|
| [Jumper EMBL lecture](https://www.youtube.com/watch?v=gg7WjuFs8F4) | 1 hour | The creator explains AF2 architecture |
| [AF3 Nature paper](https://www.nature.com/articles/s41586-024-07487-w) | 3 hours | Methods sections 1-6 map to notebook modules |
| [Yannic Kilcher AF2](https://www.youtube.com/watch?v=nGVFbPKB3iE) | 1.5 hours | Best paper walkthrough |
| [Boltz-1 technical report](https://www.biorxiv.org/content/10.1101/2024.11.19.624167v1) | 2 hours | More accessible AF3 description |
| [OpenFold GitHub](https://github.com/aqlaboratory/openfold) | Ongoing | Read actual production code |

---

## Part 3: How to Read a Research Paper

### The Harvard Medical School Method (adapted for ML papers)

**Pass 1 — 5 minutes:**
1. Read the title. Write down what you *predict* the paper will show.
2. Read the abstract. Update your prediction.
3. Look at all figures. For each figure, read only the caption.
4. Read the conclusions.
> Goal: Decide if this paper is worth 1-3 hours of your time.

**Pass 2 — 45 minutes:**
1. Read the Introduction (what problem? what gap? what did they do?)
2. Read the Results section (what did they find? what evidence do they provide?)
3. For every figure: understand the axes, the error bars, the statistical test used.
> Goal: Can you explain the main result to a peer without looking at the paper?

**Pass 3 — 2 hours (for papers you will implement):**
1. Read every Methods section carefully.
2. For every algorithm box: trace through it with N=3 as a concrete example.
3. Find the released code. Does the code match the methods description?
4. Check the supplement for derivations and hyperparameters.
> Goal: You can reproduce Figure 1 from scratch.

### How to Identify a Paper's Contribution
Ask: "What would be false if this paper didn't exist?"
- For AF3: Without AF3, we couldn't predict protein-ligand complexes accurately. TRUE → real contribution.
- For a paper claiming "our method is better on benchmark X": check if the benchmark is the right one for the use case. Many papers overfit to benchmarks.

### Red Flags in ML Papers
- No ablation study (which component actually helps?)
- Comparison to old baselines only
- Metrics that don't correlate with real-world performance
- No error bars / statistical tests
- "We use the same hyperparameters as the baseline" — often means they tuned theirs but not baseline's

---

## Part 4: How to Debug

### The Scientific Method for Code Bugs

**Step 1: Observe precisely.** What EXACTLY fails?
```
Bad: "my model doesn't train"
Good: "loss is 4.2 at step 1, increases to 6.8 at step 100, should decrease"
```

**Step 2: Form a hypothesis.** What single thing might cause this?
```
Hypothesis: "learning rate is too high, causing loss oscillation"
```

**Step 3: Design a test.** What would prove or disprove your hypothesis?
```
Test: run with lr = 1e-5 instead of 1e-3; check if loss now decreases
```

**Step 4: Run the test and read the result.** If wrong, form a new hypothesis.

### Common Bugs by Category

**Loss doesn't decrease:**
- Wrong sign on loss (forgot to `minimize` not `maximize`)
- Gradient not attached (tensor detached from graph; check `requires_grad`)
- LR too high (try 10x lower)
- Batch normalization in eval mode during training

**NaN loss:**
- Log of zero: add `eps=1e-8` to `log(x + eps)`
- Division by zero: check sequence lengths, batch sizes
- Exploding gradients: add gradient clipping `torch.nn.utils.clip_grad_norm_(params, 1.0)`

**Wrong shapes:**
```python
# Always print shapes when debugging
print(f"x: {x.shape}, y: {y.shape}")  # add after every operation until you find the mismatch
```

**Evaluation metrics look too good:**
- Data leakage: check that your test set was truly held out before ALL preprocessing
- Wrong metric: are you measuring what you think you're measuring?
- Train-test distribution shift: are the test cases structurally different from train?

### Debugging Bioinformatics Code Specifically

| Error | Likely Cause |
|-------|-------------|
| `KeyError: 'CA'` in PDB parsing | Missing C-alpha atom in structure; filter incomplete residues |
| Alignment score is negative | Gap penalty too large; check scoring matrix sign convention |
| RNA-seq DE: 0 significant genes | Batch effect; check PCA first |
| pLDDT all zeros | Ran AF3 in template-only mode; check input format |
| CUDA out of memory | Sequence too long; reduce `max_length` or enable gradient checkpointing |

---

## Part 5: How to Use GitHub Effectively

```bash
# Clone and explore a new codebase in 15 minutes
git clone https://github.com/aqlaboratory/openfold
cd openfold

# 1. Read the README (always)
cat README.md | head -100

# 2. Find the entry point
grep -r "def forward\|def main\|if __name__" . --include="*.py" | grep -v test | head -20

# 3. Map the architecture
find . -name "*.py" | xargs grep "class.*Module\|class.*nn.Module" | grep -v test

# 4. Find how a concept is used
grep -rn "triangle_attention\|TriangleAttention" . --include="*.py"

# 5. Understand what changed recently
git log --oneline | head -20
git show HEAD  # see most recent change

# 6. Run the tests to verify your environment
pytest tests/ -v -k "not slow"
```

### Reading a Pull Request
When a new feature is added to OpenFold or Boltz:
1. Read the PR description — what problem does it solve?
2. Read the changed files (`Files changed` tab)
3. Understand: what was the code before? What is it after? Why?
4. Check if tests were added. If not, that's a quality concern.

---

## Part 6: Building Intuition (The MIT Approach)

MIT's approach to teaching: *"Build intuition first, formalism second."*

For every ML concept, complete this sequence:

### 1. Toy Example First
Before reading the full derivation of FAPE loss, compute it by hand for 2 residues:
```python
# 2 residues, each with a local frame
pred_coord = torch.tensor([[1.0, 0.0, 0.0]])   # predicted atom position
true_coord = torch.tensor([[1.1, 0.0, 0.0]])   # true atom position
R = torch.eye(3)   # identity frame
t = torch.zeros(3)

# FAPE for this trivial case: distance in local frame = 0.1 Angstrom
local_diff = (pred_coord - t) @ R - (true_coord - t) @ R
fape = local_diff.norm()  # = 0.1
print(f"FAPE = {fape:.2f} A")  # should be 0.10
```

### 2. Scale Up Incrementally
N=2, then N=10, then N=100. Where does it break? That's where the interesting engineering is.

### 3. Break It Deliberately
What happens to FAPE if all predicted frames are identical? (collapses to global RMSD)
What happens to triangle attention if N=1? (degenerate case — no triangle)
Deliberately breaking things builds deep intuition faster than reading.

### 4. Reimplement From Scratch
The ultimate test: close the notebook, open a blank file, and reimplement from memory.
You'll discover exactly what you didn't understand.

---

## Part 7: The Independent Learner's Weekly Practice

### Daily (20 minutes)
- **5 min**: Read one paragraph of a primary paper (AF3, Boltz, ESM-3)
- **10 min**: Implement one small function from scratch, test on 3 cases
- **5 min**: Write one Anki card or notebook entry: concept → definition + example

### Weekly (2 hours)
- Solve 2 Rosalind problems (rosalind.info) — keeps algorithmic thinking sharp
- Read one GitHub PR in OpenFold/Boltz — understand what changed and why
- Pick one "interview question" from any notebook and answer it without looking

### Monthly (half-day)
- Reproduce one figure from a paper using only the Methods section
- Attempt CASP target predictions when CASP is running
- Compare your implementation to the official one on a benchmark

### The Highest-Value Practice
> Reproduce one published result completely from scratch — starting from raw data,
> through all preprocessing, to the final reported metric.
> Do this once per month. It is the most effective way to reach expert level.

---

## Part 8: Knowledge Calibration Rubric

Before and after each module, score yourself 1-5 on these questions:

| Module Topic | Q1: Can I explain it? | Q2: Can I implement? | Q3: Can I debug? | Q4: Do I know failure modes? |
|---|---|---|---|---|
| NW/SW Alignment | /5 | /5 | /5 | /5 |
| HMMs (Baum-Welch) | /5 | /5 | /5 | /5 |
| GNNs (message passing) | /5 | /5 | /5 | /5 |
| AF3 Architecture | /5 | /5 | /5 | /5 |
| Triangle Attention | /5 | /5 | /5 | /5 |
| FAPE Loss | /5 | /5 | /5 | /5 |
| Diffusion (DDPM) | /5 | /5 | /5 | /5 |
| LoRA Fine-tuning | /5 | /5 | /5 | /5 |
| Bayesian Uncertainty | /5 | /5 | /5 | /5 |

**Score < 3 anywhere**: Revisit that module before advancing.
**Score 3-4 everywhere**: You're ready for the fine-tuning capstone.
**Score 4-5 on AF3 + Fine-tuning**: You're ready for a technical interview at computational biology ML teams.

---

## Part 9: Domain-Specific Pitfalls (From 10 Years of Teaching)

| Module | Common Mistake | Correct Approach |
|--------|---------------|-----------------|
| 01 Alignment | 0-indexed positions when algorithm is 1-indexed | Always print indices with positions; unit test on known examples |
| 01 HMMs | Forgetting to work in log-space → underflow | Use `log_sum_exp` trick; NumPy gives -inf for log(0) |
| 02 RNA-seq | Random sample split for DE analysis | Keep ALL replicates; DE analysis uses all samples |
| 02 Variants | Testing on same population as training | Use independent cohort; HWE test as QC step |
| 03 Structure | RMSD before superposition | Always superpose (minimize RMSD); report RMSD after Kabsch alignment |
| 06 GNNs | Not testing SE(3) equivariance | Rotate input 90°; check output rotates consistently |
| 07 AF3 | Trusting low-pLDDT coordinates | Filter pLDDT < 50 regions; treat as disordered |
| 07 AF3 | Running AF3 on signal peptide | Remove signal peptide before prediction; it's cleaved in the real protein |
| 10 Fine-tuning | Random split on SKEMPI | GroupShuffleSplit by protein complex; prevents data leakage |
| 10 Fine-tuning | Full fine-tuning on < 500 examples | Use LoRA (r ≤ 8); freeze backbone; only train task head |
| 13 Bayesian | Not calibrating uncertainty estimates | Always check reliability diagram on holdout set |
| All modules | Not predicting before running | Write expected output BEFORE running any cell |
| All modules | Copying code without understanding | Close the notebook; reimplement from memory |

---

## Part 10: Preparing for Technical Interviews

### What computational biology ML teams / structural biology research labs Interviewers Actually Test

Based on public interview reports and the job descriptions:

**Round 1 (1 hour coding):**
- Implement a neural network module from scratch in PyTorch
- Debug a broken training loop (they give you code with 3 bugs)
- Write unit tests for an ML function

**Round 2 (1 hour ML theory):**
- Explain a paper you've read recently (you choose which)
- Derive the ELBO for a VAE
- When would you use GP regression instead of a neural network?

**Round 3 (1 hour systems/application):**
- Design an ML pipeline for predicting protein-ligand binding affinity
- How would you scale this to 1M compounds?
- What data would you need? What baseline would you start with?

### The Interview Preparation Checklist

- [ ] Can implement attention mechanism from scratch in < 20 minutes
- [ ] Can explain why triangle attention enforces geometric consistency
- [ ] Can explain FAPE loss and why it's better than RMSD for training
- [ ] Can explain the diffusion process (forward + reverse, both equations)
- [ ] Can implement LoRA from scratch and explain the rank tradeoff
- [ ] Can name 3 failure modes of protein structure prediction
- [ ] Can explain GroupShuffleSplit and why it matters for SKEMPI
- [ ] Have read the AF3 paper Methods sections 1-4
- [ ] Have run a fine-tuning experiment end-to-end
- [ ] Have reproduced at least one figure from a published paper

---

## Appendix: Free Textbooks Worth Your Time

| Book | Authors | Free At | Covers |
|------|---------|---------|--------|
| Deep Learning | Goodfellow et al. | deeplearningbook.org | Foundations through advanced |
| Probabilistic ML Vol 1 & 2 | Kevin Murphy | probml.github.io | Best modern ML textbook |
| Elements of Statistical Learning | Hastie et al. | hastie.su.domains | Classical ML theory |
| Biological Sequence Analysis | Durbin et al. | cambridge.org | HMMs, alignment, phylogeny |
| Bioinformatics Algorithms | Compeau & Pevzner | bioinformaticsalgorithms.org | Every Rosalind algorithm |
| An Introduction to Bioinformatics | Tisdall | Archive.org | Practical computational biology |
| Understanding Machine Learning | Shalev-Shwartz | cs.huji.ac.il | Theory: PAC, VC dimension |
| Gaussian Processes for ML | Rasmussen & Williams | gaussianprocess.org | GPs from scratch |
