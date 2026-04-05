---
name: Bug Report
about: Report a broken cell, import error, or incorrect output in a notebook
title: "[BUG] <module>/<notebook> — short description"
labels: bug
assignees: ''
---

## Which notebook?

<!-- Provide the module directory and notebook filename. Example: 07_alphafold3_core/02_pairformer.ipynb -->

**Module / Notebook:**

---

## Which cell is broken?

<!-- Describe the cell: its position (e.g., "Cell 7"), the function name, or paste a short excerpt of the cell header comment. -->

**Cell location or description:**

---

## Error message

<!-- Paste the full error traceback here. Do not paraphrase — the exact text helps maintainers reproduce the issue. -->

```
(paste traceback here)
```

---

## What you expected to happen

<!-- What should the cell have done if it were working correctly? -->

---

## Steps to reproduce

1.
2.
3.

<!-- If the error only appears after running certain earlier cells, list the steps in order. -->

---

## Environment

| Field | Value |
|---|---|
| Python version | (e.g., 3.10.12) |
| OS | (e.g., Ubuntu 22.04 / macOS 14 / Windows 11) |
| Hardware | (CPU only / NVIDIA RTX 3090 / Google Colab T4) |
| PyTorch version | (e.g., 2.1.0) |
| Key package versions | (e.g., biopython 1.81, transformers 4.38) |

<!-- To get Python and package versions quickly: python --version && pip show torch biopython transformers -->

---

## Additional context

<!-- Anything else that might help: did it ever work before? Did you modify any cells? Are you using a virtual environment or conda? -->

---

## Reproducible on Google Colab?

- [ ] Yes, also fails on Colab
- [ ] No, works on Colab (local environment issue)
- [ ] Not tested on Colab
