# Contributing to the Bioinformatics ML Curriculum

Thank you for wanting to improve this curriculum. Whether you are fixing a typo, reporting a broken cell, or suggesting a new resource, every contribution helps make this project better for everyone — including beginners who are just finding their footing in bioinformatics and ML.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Reporting a Bug in a Notebook](#reporting-a-bug-in-a-notebook)
3. [Suggesting a New Notebook or Resource](#suggesting-a-new-notebook-or-resource)
4. [Fixing a Typo or Improving an Explanation](#fixing-a-typo-or-improving-an-explanation)
5. [Notebook Code Style](#notebook-code-style)
6. [How to Test Your Changes](#how-to-test-your-changes)
7. [Pull Request Checklist](#pull-request-checklist)

---

## Code of Conduct

This project is beginner-friendly by design. Please:

- Use welcoming, patient language — many contributors are learning both bioinformatics and Python at the same time.
- Assume good intent when someone asks a basic question.
- Never mock or dismiss "obvious" errors. What is obvious to an expert is not obvious to someone on day one.
- Give constructive, specific feedback on PRs rather than general criticism.
- Credit sources and prior work when you build on them.

Maintainers reserve the right to remove comments or close issues that are dismissive, aggressive, or off-topic.

---

## Reporting a Bug in a Notebook

Use the **Bug Report** issue template (`.github/ISSUE_TEMPLATE/bug_report.md`). Here is what to include:

**Step-by-step process:**

1. Open the issue tracker on GitHub and click **New Issue**.
2. Select the "Bug Report" template.
3. Fill in:
   - The module and notebook number (e.g., `07_alphafold3_core/02_pairformer.ipynb`)
   - The cell number or a short excerpt of the cell that fails
   - The exact error message (copy-paste from the traceback, not a paraphrase)
   - What you expected to happen
   - Your environment: Python version, OS, whether you are running on CPU or GPU
4. If the bug is reproducible on Google Colab, mention that — it helps maintainers triage quickly.

**Good bug report example:**

> **Notebook:** `06_structural_ml_gnns/01_protein_gnns.ipynb`
> **Cell:** Cell 14 — `collate_graphs` function definition
> **Error:** `AttributeError: 'NoneType' object has no attribute 'edge_index'`
> **Expected:** The DataLoader should batch graphs without error.
> **Environment:** Python 3.10, Ubuntu 22.04, CPU only, torch 2.1.0

---

## Suggesting a New Notebook or Resource

Use the **Resource Suggestion** issue template. Before submitting:

- Check `RESOURCES.md` to confirm the resource is not already listed.
- Check `CURRICULUM.md` to see if the topic is already covered.
- Briefly explain why the suggested resource is better than or complementary to what exists.

For a brand-new notebook suggestion, describe:
- The learning objective ("After this notebook, learners will be able to...")
- Which module it belongs to
- Whether you are willing to draft it

---

## Fixing a Typo or Improving an Explanation

For small fixes (typos, wording, broken links in Markdown cells):

1. Fork the repository and create a branch named `fix/description-of-fix`.
2. Make the change directly in the `.ipynb` file using a text editor or Jupyter.
3. Do not re-run cells just to fix a typo — keep existing outputs intact.
4. Open a PR with a clear title like `Fix typo in 05/01 TL;DR cell`.

For larger explanation improvements (rewriting a confusing section, adding a diagram, restructuring a cell sequence), open an issue first to discuss the approach before writing code.

---

## Notebook Code Style

All notebooks in this curriculum follow a consistent structure. Please match it when contributing.

### Cell Order (per notebook)

1. **TL;DR cell** — Plain-English Markdown explaining what this notebook covers and what the learner will be able to do. Required. Must be the first cell.
2. **Imports cell** — All `import` statements in one cell, grouped: stdlib, then third-party, then local.
3. **Section cells** — Use `## 1. Section Title` Markdown headings. Number sections sequentially.
4. **Exercise cells** — Mark with a comment `# EXERCISE:` at the top of the cell. Follow with `# SOLUTION:` in the next cell (collapsed by default using `# ---`).
5. **Interview Questions section** — For modules 05–10, include a final section `## 6. Advanced Interview Preparation` with at least 5 questions.

### Naming Conventions

- Variables: `snake_case`
- Classes: `PascalCase`
- Constants: `ALL_CAPS`
- Functions that return tensors: suffix `_tensor` (e.g., `embed_sequence_tensor`)
- Avoid single-letter variables except loop indices (`i`, `j`) and math notation (`x`, `W`)

### Cell Formatting

- Limit code cells to ~40 lines. Split longer logic into helper functions.
- Add a one-line comment at the top of each code cell describing what it does.
- Use f-strings for all print statements.
- NumPy arrays: use `np.float32` unless there is a specific reason for `float64`.
- PyTorch tensors: always specify `dtype` and `device` explicitly when creating new tensors.

### Markdown Cells

- Use plain English. Write as if explaining to a smart colleague who is new to the specific topic.
- Include the "why" before the "how".
- Math equations: use LaTeX in Markdown cells (`$...$` inline, `$$...$$` display).

---

## How to Test Your Changes

Before submitting a PR, verify the following:

1. **Run the notebook top-to-bottom from a clean kernel.**
   In Jupyter: Kernel > Restart & Run All. The notebook must complete without errors.

2. **Check that all imports are available in `requirements.txt`.**
   If you added a new dependency, add it to `requirements.txt` with a minimum version pin.

3. **Validate the notebook JSON.**
   ```bash
   python -c "import json; json.load(open('path/to/notebook.ipynb'))"
   ```
   A corrupted `.ipynb` file will fail silently in some editors but break CI.

4. **Check that the TL;DR cell exists and is the first cell.**

5. **Test on a CPU-only machine if possible**, since not all contributors have GPUs. If a cell genuinely requires a GPU, mark it clearly:
   ```python
   # NOTE: This cell requires a CUDA GPU. On CPU it will take ~10x longer.
   ```

---

## Pull Request Checklist

Before opening a PR, confirm all of the following:

- [ ] Branch is named descriptively (`fix/broken-import-06-01`, `feat/add-bayesian-notebook`, `docs/improve-pairformer-explanation`)
- [ ] Notebook runs top-to-bottom from a clean kernel without errors
- [ ] All new imports are in `requirements.txt`
- [ ] Notebook JSON is valid (`python -c "import json; json.load(open(...))"`)
- [ ] TL;DR cell is present and is the first cell
- [ ] Code follows the style guide above (snake_case, section numbering, cell length)
- [ ] No large binary files or dataset files are committed (use `data/` and add to `.gitignore`)
- [ ] PR description explains: what changed, why, and how to test it
- [ ] If fixing a bug: the original issue number is referenced in the PR description (`Closes #123`)

Thank you for contributing.
