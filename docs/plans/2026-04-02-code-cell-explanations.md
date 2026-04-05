# Code Cell Explanations Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add beginner-friendly `#` explanation comments to every substantive notebook code cell so students understand what each cell is doing biologically and computationally.

**Architecture:** Use a single scripted notebook rewrite to prepend a short three-line comment block to each non-empty code cell. The script should be idempotent, preserve notebook structure, skip already-injected explanations, and generate comments using notebook/module-aware heuristics plus cell-content keyword detection.

**Tech Stack:** Python, JSON notebook editing, AST syntax verification

---

### Task 1: Create the rewrite strategy

**Files:**
- Modify: `/home/recep/Desktop/Machine_Learning/projects/hackerrank/docs/plans/2026-04-02-code-cell-explanations.md`

**Step 1: Define the explanation format**

Use a fixed three-line comment header:

```python
# Biological context: ...
# Python/ML mechanics: ...
# Why it matters: ...
```

**Step 2: Define insertion rules**

Apply to all non-empty code cells. Do not duplicate headers if the cell already begins with the injected format.

**Step 3: Define heuristic sources**

Use:
- notebook path and module name
- notebook filename keywords
- code keywords such as `import`, `fit`, `predict`, `DataLoader`, `nn.Module`, `train_test_split`, `networkx`, `torch_geometric`, `bayes`, `diffusion`, `reward`, `mlflow`, `fastapi`

**Step 4: Commit**

```bash
git add docs/plans/2026-04-02-code-cell-explanations.md
git commit -m "docs: add plan for notebook code-cell explanations"
```

### Task 2: Run the notebook rewrite

**Files:**
- Modify: `/home/recep/Desktop/Machine_Learning/projects/hackerrank/**/*.ipynb`

**Step 1: Write the rewrite script**

The script should:
- iterate over every `.ipynb`
- load JSON safely
- inspect each code cell
- generate a concise explanation block
- prepend the block
- preserve metadata and output structure

**Step 2: Run the script**

Run the Python script from the repo root.

Expected: all notebook files updated in place with no JSON corruption.

**Step 3: Spot-check representative modules**

Check examples from:
- module 00 basics
- module 04 or 05 ML/deep learning
- module 07 structural modeling
- module 14-16 advanced modules

**Step 4: Commit**

```bash
git add .
git commit -m "docs: annotate notebook code cells with teaching comments"
```

### Task 3: Verify notebook integrity

**Files:**
- Verify: `/home/recep/Desktop/Machine_Learning/projects/hackerrank/**/*.ipynb`

**Step 1: Run syntax verification**

Run a repo-wide parse check over all notebook code cells.

Expected: zero syntax errors.

**Step 2: Check idempotency markers**

Confirm the injected header appears once at the top of annotated cells, not multiple times.

**Step 3: Sample-check content quality**

Inspect a few rewritten cells to ensure the comments are biologically meaningful and not generic filler.

**Step 4: Commit**

```bash
git add .
git commit -m "chore: verify notebook explanation pass"
```

Plan complete and saved to `docs/plans/2026-04-02-code-cell-explanations.md`. Two execution options:

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

This session is proceeding with the work directly because you already approved implementation.
