# Cloud GPU Setup Guide

**For students without local GPUs** — run the heavy notebooks (Modules 07, 10, 12) for free.

---

## Quick Decision Table

| Notebook | GPU Memory Needed | Best Free Option | Paid Option |
|----------|------------------|------------------|-------------|
| 07/01–07/04 (Pairformer, AF3 concepts) | CPU only | Any Colab | — |
| 07/05 (AF3 training loop) | 4–8 GB | Colab T4 | Lightning AI L4 |
| 10/01 (OpenFold fine-tuning) | 16 GB+ | Colab A100 Pro | Lambda Labs A100 |
| 10/02 (ΔΔG capstone) | 8–16 GB | Colab T4 | Vast.ai RTX 4090 |
| 12/01 (DDPM protein design) | 4–8 GB | Colab T4 | — |
| 15/01 (ESM-2 embeddings) | 8 GB | Colab T4 | — |
| 17/00 (Capstone) | CPU only | Any Colab | — |

---

## Option 1: Google Colab (Free, Recommended to Start)

### One-Click Setup for Any Notebook

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click `File → Open notebook → GitHub`
3. Paste your repo URL (or upload the `.ipynb` directly)
4. Click `Runtime → Change runtime type → T4 GPU`
5. Run this setup cell at the top:

```python
# Paste this as the first cell in any heavy notebook
!pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118 -q
!pip install biopython numpy pandas matplotlib seaborn scikit-learn -q
!pip install fair-esm -q  # for Module 15 (ESM-2)

import torch
print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU only'}")
print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB"
      if torch.cuda.is_available() else "")
```

### Colab GPU Tiers

| Tier | GPU | VRAM | Session Limit | Cost |
|------|-----|------|---------------|------|
| Free | T4 | 15 GB | ~4-12 hrs | Free |
| Colab Pro ($10/mo) | L4 / A100 | 22–40 GB | 24 hrs | $10/month |
| Colab Pro+ ($50/mo) | A100 80GB | 80 GB | No limit | $50/month |

**Free tier is enough for Modules 07, 12, 15. Use Pro for Module 10 (OpenFold fine-tuning).**

### Saving Your Work (Critical — Colab Disconnects!)

```python
# Mount Google Drive and save checkpoints there
from google.colab import drive
drive.mount('/content/drive')

# In your training loop, save every 50 steps:
checkpoint_path = '/content/drive/MyDrive/hackerrank_checkpoints/module10_step{step}.pt'
torch.save({'model': model.state_dict(), 'step': step}, checkpoint_path.format(step=step))
```

---

## Option 2: Kaggle Notebooks (Free, 30 hrs/week GPU)

Kaggle gives **30 GPU hours/week** with P100 (16 GB VRAM) — more predictable than Colab.

1. Go to [kaggle.com/code](https://kaggle.com/code) → New Notebook
2. Settings → Accelerator → GPU P100
3. Upload your notebook or paste code
4. Click Save Version → Run All

```python
# Kaggle setup cell
import subprocess
subprocess.run(['pip', 'install', 'fair-esm', 'biopython', '-q'])
import torch
print(f"GPU: {torch.cuda.get_device_name(0)}")  # P100
```

**Best for:** Module 10 (16 GB P100 handles small OpenFold fine-tuning), Module 07/05 (training loop).

---

## Option 3: Lightning AI (Free Tier, Jupyter-like Interface)

[lightning.ai](https://lightning.ai) gives 22 GPU hours/month free with an L4 (22 GB VRAM).

1. Create free account at lightning.ai
2. New Studio → Select `L4 GPU`
3. Upload notebooks from your local machine (drag + drop)
4. Install dependencies in a terminal tab:
   ```bash
   pip install torch biopython fair-esm
   ```

**Best for:** Module 10 — L4 GPU has enough memory for small OpenFold fine-tuning without Colab Pro.

---

## Option 4: Vast.ai (Cheapest Paid Option, ~$0.20/hr for RTX 4090)

For serious training runs (Module 10 full fine-tuning, real ESM-2):

1. Go to [vast.ai](https://vast.ai) → create account, deposit $10
2. Search for: `RTX 4090` or `A100 40GB`, price < $0.50/hr
3. Select instance → Connect via Jupyter or SSH
4. Setup:
   ```bash
   pip install torch torchvision biopython fair-esm openmm MDAnalysis
   git clone <your-repo>
   cd hackerrank
   jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
   ```

**Cost estimate for this curriculum:**
- Module 10/02 (ΔΔG fine-tuning, 500 steps): ~15 min on A100 = $0.12
- Module 07/05 (AF3 training loop, 300 steps): ~5 min on T4 = free on Colab

---

## Option 5: Lambda Labs (Best for A100 at Research Scale)

[lambdalabs.com/service/gpu-cloud](https://lambdalabs.com/service/gpu-cloud) — A100 80GB at $1.10/hr.

Used by researchers fine-tuning actual OpenFold checkpoints (Module 10 advanced).

```bash
# Lambda Labs persistent storage setup
mkdir -p /home/ubuntu/hackerrank
cd /home/ubuntu/hackerrank
git clone <your-repo> .
pip install -r requirements.txt
# Download OpenFold checkpoint (4 GB):
wget https://openfold.s3.amazonaws.com/base_training/finetuning_ptm_2.pt
```

---

## Module-Specific Colab Starter Cells

### Module 07/05 — AF3 Training Loop

```python
# ── Cell 1: GPU check ──
import torch
assert torch.cuda.is_available(), "Enable GPU: Runtime → Change runtime type → T4 GPU"
print(f"GPU: {torch.cuda.get_device_name(0)}, VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f} GB")

# ── Cell 2: BF16 check (needed for AF3 training loop) ──
x = torch.ones(1, device='cuda', dtype=torch.bfloat16)
print(f"BF16 supported: {x.dtype == torch.bfloat16}")

# ── Cell 3: Memory management ──
torch.cuda.empty_cache()
import gc; gc.collect()
print(f"Free VRAM: {(torch.cuda.get_device_properties(0).total_memory - torch.cuda.memory_allocated()) / 1e9:.1f} GB")
```

### Module 10/01 — OpenFold Fine-Tuning

```python
# ── Cell 1: Install OpenFold (takes 5 min) ──
!pip install git+https://github.com/aqlaboratory/openfold.git -q
# OR use Boltz (lighter, easier):
!pip install boltz -q

# ── Cell 2: Download a small checkpoint for practice ──
import urllib.request
# ESM-2 150M (small, fits in 4GB VRAM)
!python -c "import esm; model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()"

# ── Cell 3: Mixed precision setup ──
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
# Usage in training loop:
# with autocast():
#     loss = model(x)
# scaler.scale(loss).backward()
# scaler.step(optimizer)
# scaler.update()
```

### Module 12/01 — DDPM Protein Design

```python
# ── Cell 1: Setup ──
import torch, numpy as np, matplotlib.pyplot as plt
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using: {device}")

# ── Cell 2: Memory tip for diffusion ──
# If you get OOM during sampling, reduce batch size or use chunked sampling:
# Instead of sampling all timesteps at once:
#   for t in reversed(range(T)):
#       with torch.no_grad():  # ← critical: no grad needed during sampling
#           x = p_sample(model, x, t)
#       torch.cuda.empty_cache()  # ← free cache after each step if tight on VRAM
```

### Module 15/01 — ESM-2 Embeddings

```python
# ── Cell 1: Install fair-esm ──
!pip install fair-esm -q

# ── Cell 2: Load ESM-2 (pick size based on VRAM) ──
import esm, torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'

vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9 if torch.cuda.is_available() else 0
if vram_gb >= 40:
    model, alphabet = esm.pretrained.esm2_t48_15B_UR50D()   # 15B params, 40GB+
elif vram_gb >= 16:
    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()   # 650M params, 16GB
elif vram_gb >= 8:
    model, alphabet = esm.pretrained.esm2_t12_35M_UR50D()    # 35M params, 8GB
else:
    model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()      # 8M params, CPU-friendly

model = model.to(device).eval()
print(f"Loaded ESM-2 on {device}")
```

---

## Troubleshooting Common Issues

| Error | Cause | Fix |
|-------|-------|-----|
| `CUDA out of memory` | Batch too large | Halve batch size; add `torch.cuda.empty_cache()` |
| `RuntimeError: Expected BF16` | T4 doesn't support BF16 | Use `fp16` on T4, `bf16` only on A100/L4 |
| `Session crashed after using all RAM` | CPU RAM exhausted | Restart runtime; don't load full dataset into memory |
| `pip install takes forever on Colab` | Cold start | Add `--quiet` flag; use pre-built wheels |
| Colab disconnects mid-training | Idle timeout | Add a keep-alive JS snippet or use Colab Pro |
| `ImportError: No module named 'openfold'` | openfold not installed | Use Boltz as lighter alternative |

### Colab Keep-Alive (paste in browser console)

```javascript
// Prevents Colab from disconnecting due to idle timeout
// Open: View → Developer Tools → Console → paste this
function ClickConnect(){
  console.log("Keeping alive...");
  document.querySelector("#top-toolbar > colab-connect-button")
    .shadowRoot.querySelector("#connect").click()
}
setInterval(ClickConnect, 60000)
```

---

## Free Resource Checklist Before Starting Heavy Notebooks

- [ ] Google account created (for Colab + Drive)
- [ ] Kaggle account created (for 30 hr/week GPU backup)
- [ ] Lightning AI account created (22 hr/month free L4)
- [ ] 5 GB free space on Google Drive (for checkpoints)
- [ ] Colab runtime type set to GPU before running (Runtime → Change runtime type)
- [ ] `torch.cuda.is_available()` returns `True` before running training cells

---

*Total cost to complete the full curriculum on cloud GPUs: $0 (free tiers) to ~$5 (if you run Module 10 full fine-tuning on paid GPU).*
