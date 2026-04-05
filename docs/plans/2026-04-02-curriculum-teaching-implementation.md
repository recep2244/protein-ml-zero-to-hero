# Curriculum Teaching Improvement Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a consistent teaching layer across the curriculum so beginners can capture the core ideas without losing access to the advanced material.

**Architecture:** Update root and module docs manually, then apply a scripted notebook pass that injects standardized beginner scaffolding and mastery-check cells tailored by module. Finish with verification that all notebooks still parse and that the root docs reflect the real repository inventory.

**Tech Stack:** Markdown, Jupyter notebook JSON, Python for safe bulk notebook transformation, repo-wide verification scripts

---

### Task 1: Strengthen root learning-path docs

**Files:**
- Modify: `README.md`
- Modify: `ZERO_TO_HERO.md`
- Modify: `RESOURCES.md`
- Modify: `STUDY_PLAN.md`
- Modify: `CLAUDE.md`

**Step 1:** Add explicit zero-to-core, advanced, and conceptual-only paths.

**Step 2:** Add stronger canonical resource recommendations and clearer package/compute expectations.

**Step 3:** Reconcile all counts and module listings with the actual tree.

### Task 2: Upgrade advanced module README files

**Files:**
- Modify: `08_practical_problems/README.md`
- Modify: `11_membrane_protein_dynamics/README.md`
- Modify: `12_generative_models/README.md`
- Modify: `13_bayesian_methods/README.md`
- Modify: `14_reinforcement_learning/README.md`
- Modify: `15_self_supervised_learning/README.md`
- Modify: `16_mlops_deployment/README.md`

**Step 1:** Add beginner-facing framing, what to skip on first pass, and module-specific teaching advice.

**Step 2:** Add stronger resource recommendations and role expectations.

### Task 3: Apply notebook-level teaching scaffolding

**Files:**
- Modify: all `*.ipynb`

**Step 1:** Insert a “Beginner Teaching Frame” cell after the title cell.

**Step 2:** Insert a “Mastery Check” cell near the end if missing.

**Step 3:** Insert a short “Canonical Resource Upgrade” cell for the notebook domain when missing.

### Task 4: Verify the transformed curriculum

**Files:**
- Verify: all `*.ipynb`
- Verify: all `*.md`

**Step 1:** Run syntax parsing across all notebook code cells.

**Step 2:** Recheck root-doc inventory coverage and local markdown links.

**Step 3:** Report what remains unverified at runtime.
