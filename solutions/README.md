# solutions/ — Exercise Solutions

This folder contains worked solutions to the exercises found throughout the curriculum.

---

## Philosophy

**Try the exercise yourself first.**

Struggle is the learning mechanism. Reading a solution without attempting the problem yourself is the equivalent of watching someone else do push-ups and expecting to get stronger. The research on learning consistently shows that even an unsuccessful attempt at a problem dramatically improves retention of the solution when you do see it.

**The 30-minute rule:** Spend at least 30 minutes genuinely attempting an exercise before opening the solution. If you are completely stuck after 30 minutes, look at the solution, understand it, close it, and then rewrite it from memory.

---

## How Solutions Are Organized

Solutions mirror the curriculum module structure exactly:

```
solutions/
├── README.md                        ← this file
├── module_00_python_ml_basics/
│   ├── 00_python_review_solution.ipynb
│   ├── 01_numpy_solution.ipynb
│   └── ...
├── module_01_sequence_analysis/
│   ├── 01_needleman_wunsch_solution.ipynb
│   └── ...
├── module_02_genomics/
│   └── ...
├── module_03_structural_biology/
│   └── ...
├── module_04_ml_for_omics/
│   └── ...
├── module_05_deep_learning/
│   └── ...
├── module_06_structural_ml_gnns/
│   └── ...
├── module_07_alphafold3_core/
│   └── ...
├── module_08_practical_problems/
│   └── ...
├── module_09_ml_teaching/
│   └── ...
├── module_10_openfold3_finetuning/
│   └── ...
└── ...
```

Each solution notebook has the same structure as the original notebook, with the `# EXERCISE:` cells filled in and marked `# SOLUTION:`.

---

## Solutions Are Added Over Time

Not all modules have solutions yet. Solutions are added as the curriculum matures and as contributors submit them. The table below tracks the current state:

| Module | Solution Status |
|---|---|
| 00 — Python & ML Basics | Partial |
| 01 — Sequence Analysis | Partial |
| 02 — Genomics | Not yet available |
| 03 — Structural Biology | Not yet available |
| 04 — ML for Omics | Not yet available |
| 05 — Deep Learning | Not yet available |
| 06 — Structural ML + GNNs | Not yet available |
| 07 — AlphaFold3 Core | Not yet available |
| 08 — Practical Problems | Partial |
| 09 — ML Teaching | Not yet available |
| 10 — Fine-Tuning (Capstone) | Not yet available |
| 11–17 | Not yet available |

---

## How to Contribute Solutions

1. Fork the repository and create a branch named `solution/module-XX-notebook-name`.
2. Copy the original notebook from the module directory into the corresponding `solutions/module_XX_*/` directory.
3. Rename the file to `original_name_solution.ipynb`.
4. Fill in the `# EXERCISE:` cells with a working solution.
5. Add a brief comment above your solution explaining the key insight or approach.
6. Run the solution notebook top-to-bottom from a clean kernel to confirm it completes without errors.
7. Open a PR. The PR description should state which exercise it solves and briefly explain your approach.

**Multiple valid solutions are welcome.** If a better or more idiomatic solution exists for an already-solved exercise, open a PR with your alternative. Solutions can include a "Alternative approach" section.

---

## A Note on HackerRank Problems

For Module 08 (Practical Problems), solutions are intentionally withheld from the public repository for problems that are also live HackerRank assessments. These solutions are available in a separate private repository for verified learners. See `STUDY_PLAN.md` for details on how to request access.
