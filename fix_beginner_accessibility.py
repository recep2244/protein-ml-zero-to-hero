"""
fix_beginner_accessibility.py
Harvard ML professor-grade beginner accessibility fixes for 4 notebooks.

Fix 1: Insert domain-specific "Concepts for Beginners" glossary cell after TL;DR cell.
Fix 2: Add docstrings to all undocumented functions and classes.
Fix 3: Insert brief explanation markdown cells before large (>12 line) code cells
       that have no preceding markdown cell.

Preserves nbformat=4, nbformat_minor=5, 8-char hex cell IDs.
Validates JSON after each notebook write.
Does NOT change existing code logic.
"""

import json
import re
import uuid
import copy

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_cell_id():
    """Return a fresh 8-character lowercase hex cell ID (nbformat 4.5 spec)."""
    return uuid.uuid4().hex[:8]


def md_cell(source: str) -> dict:
    """Create a markdown cell dict with a fresh ID."""
    return {
        "cell_type": "markdown",
        "id": make_cell_id(),
        "metadata": {},
        "source": source,
    }


def _indent(text: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.split("\n"))


# ---------------------------------------------------------------------------
# Fix 1 — "Concepts for Beginners" glossary cells
# ---------------------------------------------------------------------------

BEGINNERS_CELLS = {
    "10/01": """\
## Protein Structure Finetuning — Concepts for Beginners

| Term | Plain English |
|------|--------------|
| **LoRA (Low-Rank Adaptation)** | Instead of retraining all weights, inject two small matrices A and B; output = frozen_weight·x + (B·A)·x * scale — only A and B train |
| **rank r** | Controls how many parameters LoRA adds; rank 4 adds 8× fewer params than rank 64 |
| **frozen weights** | Model parameters that don't change during finetuning — only LoRA A/B matrices are updated |
| **Pairformer** | AF3's core module: takes a (L,L) pair matrix and (L,) single matrix, refines both with triangle attention |
| **deltadeltaG (ΔΔG)** | Free energy change upon mutation: ΔΔG = ΔG_mutant − ΔG_wildtype; negative = stabilizing |
| **SKEMPI** | Database of ~7,000 measured binding affinity changes for protein mutations — used as training labels |
| **TCR-pMHC** | T-cell receptor binding to peptide-MHC complex; key cancer immunotherapy target modelled as multi-chain input |
| **head-only finetuning** | Only train the prediction head (last layer) — fastest, but lowest accuracy on new domains |
| **full finetuning** | Train all layers — best accuracy but risks catastrophic forgetting and needs lots of data |
| **train/val split** | Divide data: 80% to learn from, 20% to check generalisation — never train on validation examples |
| **Pearson r** | Correlation coefficient: +1 = perfect agreement, 0 = no relationship, −1 = opposite — used to evaluate ΔΔG prediction |
| **scaffold** | The protein backbone structure that a binding site or function is built on |""",

    "15/01": """\
## Self-Supervised Learning — Concepts for Beginners

| Term | Plain English |
|------|--------------|
| **Self-supervised learning** | Training without human labels: create labels automatically from the data itself (e.g. mask tokens, predict them back) |
| **Masked Language Modelling (MLM)** | Randomly hide 15% of amino acids, train model to predict them — ESM-2 pretraining task |
| **Contrastive learning** | Train by comparing: pull representations of similar inputs together, push different ones apart |
| **NT-Xent loss** | Contrastive loss: correct pair should have highest similarity among all 2N-2 negatives in the batch |
| **SimCLR** | Contrastive framework: augment each sample twice, treat both views as the positive pair |
| **BYOL** | Self-supervised method using teacher/student networks — no negative pairs needed |
| **projection head** | Small MLP applied after the encoder; the contrastive loss operates on its output, not the encoder's |
| **ESM-2** | Meta's protein language model — pretrained on 250M protein sequences using MLM; learns evolutionary patterns |
| **Linear probe** | Freeze the pretrained encoder, train only a small linear classifier on top — tests representation quality |
| **augmentation** | Creating modified views of the same input (e.g. random subsequence crop, noise) — positive pairs for contrastive learning |
| **temperature τ** | Controls sharpness of the softmax in NT-Xent; lower temperature = more aggressive contrast |
| **Q3 accuracy** | 3-class secondary structure accuracy (Helix/Sheet/Coil) — standard benchmark for protein representations |""",

    "12/01": """\
## Diffusion Models — Concepts for Beginners

| Term | Plain English |
|------|--------------|
| **diffusion (forward process)** | Gradually add Gaussian noise to data over T steps until it becomes pure noise — a Markov chain |
| **denoising (reverse process)** | Neural network learns to undo noise one step at a time — "what was the cleaner version of this?" |
| **DDPM** | Denoising Diffusion Probabilistic Model — the standard framework (Ho et al. 2020) |
| **noise schedule β_t** | Controls how much noise is added at each step; starts small, grows to completely corrupt the signal |
| **ᾱ_t (alpha bar)** | Cumulative noise product: x_t = √ᾱ_t · x₀ + √(1-ᾱ_t) · ε — lets you jump to any noise level directly |
| **ε-prediction** | Model predicts the noise ε that was added, not the clean signal directly — more stable to train |
| **score function** | Gradient of log-probability: ∇_x log p(x) — points toward higher-density regions; used in score-based models |
| **UNet** | Common architecture for diffusion: encodes then decodes with skip connections — predicts noise at each resolution |
| **denoising trajectory** | The sequence of intermediate structures from noise to final protein structure |
| **classifier-free guidance** | Train with/without condition labels, combine both at inference to control generation strength |
| **RFdiffusion** | ProteinMPNN + diffusion — generates protein backbone structures from scratch (Watson et al. 2023) |
| **inpainting** | Generate a new region of structure while keeping the rest fixed — used for protein loop design |""",

    "14/01": """\
## Reinforcement Learning — Concepts for Beginners

| Term | Plain English |
|------|--------------|
| **agent** | The learner that takes actions (e.g. mutates a protein) and receives rewards |
| **environment** | Everything the agent interacts with — in protein design: the sequence + scoring function |
| **state** | Current situation the agent observes (e.g. current protein sequence) |
| **action** | What the agent does (e.g. substitute amino acid at position 5 with Leucine) |
| **reward** | Scalar feedback signal: +high for better stability, −penalty for invalid mutations |
| **policy π** | Agent's strategy: given a state, which action to take — what the neural network learns |
| **Q-value** | Expected total future reward from taking action a in state s: Q(s,a) |
| **DQN** | Deep Q-Network: uses a neural network to approximate Q(s,a) for all actions |
| **PPO (Proximal Policy Optimization)** | Policy gradient method with a "clip" trick to prevent too-large updates — most reliable RL algorithm |
| **GFlowNet** | Generates diverse objects proportional to a reward function — better than greedy RL for exploring sequence space |
| **episode** | One complete protein design trajectory from start sequence to final designed sequence |
| **exploration vs exploitation** | ε-greedy: with probability ε take a random action (explore), otherwise take the best known action (exploit) |
| **Bellman equation** | Q(s,a) = r + γ·max_a'Q(s',a') — recursively defines optimal Q-values using future rewards |
| **replay buffer** | Stored (state, action, reward, next_state) tuples — DQN samples batches from this to break correlations |""",
}


def find_tldr_cell_index(cells):
    """Return index of the cell containing TL;DR (the insertion point is after it)."""
    for i, c in enumerate(cells):
        src = "".join(c["source"])
        if "TL;DR" in src or "tl;dr" in src.lower():
            return i
    return 0  # fall back to inserting after cell 0


def apply_fix1(nb: dict, notebook_key: str) -> int:
    """Insert the Concepts for Beginners cell after the TL;DR cell.
    Returns number of cells inserted."""
    cells = nb["cells"]
    tldr_idx = find_tldr_cell_index(cells)
    insert_at = tldr_idx + 1

    # Check we haven't already inserted it
    if insert_at < len(cells):
        src = "".join(cells[insert_at]["source"])
        if "Concepts for Beginners" in src:
            print(f"  Fix 1: already present at cell {insert_at}, skipping.")
            return 0

    new_cell = md_cell(BEGINNERS_CELLS[notebook_key])
    cells.insert(insert_at, new_cell)
    print(f"  Fix 1: inserted Concepts for Beginners cell at position {insert_at}.")
    return 1


# ---------------------------------------------------------------------------
# Fix 2 — Add docstrings to undocumented functions / classes
# ---------------------------------------------------------------------------

# Each entry: (notebook_key, cell_index_after_fix1_offset, match_pattern, docstring_lines)
# We will apply these by scanning cells for the pattern and inserting the docstring.
# Format: list of (notebook_key, def_or_class_line_pattern, docstring_body, indent_spaces)

DOCSTRINGS = {
    # -----------------------------------------------------------------------
    # 10/01 — Protein Structure Finetuning
    # -----------------------------------------------------------------------
    "10/01": [
        # Cell 8: MiniPairformer.__init__ and forward
        (
            r"^\s{4}def __init__\(self, c_z=64, c_s=128, n_heads=4\):",
            "Initialise MiniPairformer.\n\n"
            "Args:\n"
            "    c_z (int): pair representation channel dimension.\n"
            "    c_s (int): single representation channel dimension.\n"
            "    n_heads (int): number of attention heads in triangle attention.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, z, s\):\s*$",
            "Run one forward pass through all Pairformer blocks.\n\n"
            "Args:\n"
            "    z (Tensor): pair representation of shape (B, L, L, c_z).\n"
            "    s (Tensor): single representation of shape (B, L, c_s).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: updated (z, s) tensors.",
            8,
        ),
        # Cell 11: LoRALayer.__init__ and forward
        (
            r"^\s{4}def __init__\(self, d_in, d_out, rank=4, alpha=16, dropout=0\.0\):",
            "Initialise a LoRA adapter layer.\n\n"
            "Adds trainable low-rank matrices A and B to a frozen linear projection.\n"
            "Effective output: W·x + (B·A·x)·(alpha/rank).\n\n"
            "Args:\n"
            "    d_in (int): input feature dimension.\n"
            "    d_out (int): output feature dimension.\n"
            "    rank (int): LoRA rank r — controls adapter parameter count.\n"
            "    alpha (float): scaling factor; effective scale = alpha/rank.\n"
            "    dropout (float): dropout probability applied to A·x.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Apply the frozen linear weight plus the LoRA low-rank correction.\n\n"
            "Args:\n"
            "    x (Tensor): input tensor of shape (..., d_in).\n\n"
            "Returns:\n"
            "    Tensor: output of shape (..., d_out).",
            8,
        ),
        # Cell 14: DDGPredictor.__init__
        (
            r"^\s{4}def __init__\(self, c_s=128, c_z=64\):",
            "Initialise the ΔΔG prediction head.\n\n"
            "Args:\n"
            "    c_s (int): single representation dimension from Pairformer.\n"
            "    c_z (int): pair representation dimension from Pairformer.",
            8,
        ),
        # Cell 16: ToyPairformer class + methods + mode functions
        (
            r"^class ToyPairformer\(nn\.Module\):\s*$",
            "Minimal Pairformer for demonstration and finetuning experiments.\n\n"
            "Stacks n_blocks of triangle self-attention on the pair representation\n"
            "and a 2-layer transition on the single representation.\n\n"
            "Args:\n"
            "    c_z (int): pair representation channel dimension (default 128).\n"
            "    c_s (int): single representation channel dimension (default 256).\n"
            "    n_blocks (int): number of stacked Pairformer blocks (default 4).",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, c_z=128, c_s=256, n_blocks=4\):",
            "Build projection layers and stack n_blocks attention+transition blocks.\n\n"
            "Args:\n"
            "    c_z (int): pair representation channel dimension.\n"
            "    c_s (int): single representation channel dimension.\n"
            "    n_blocks (int): depth of the Pairformer stack.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, z, s\):\s*$",
            "Run the full Pairformer forward pass.\n\n"
            "Args:\n"
            "    z (Tensor): pair representation of shape (B, L, L, c_z).\n"
            "    s (Tensor): single representation of shape (B, L, c_s).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: refined (z, s) tensors, same shapes as input.",
            8,
        ),
        (
            r"^def head_only_mode\(model\):",
            "Freeze all Pairformer parameters; only the ΔΔG prediction head trains.\n\n"
            "This is the fastest finetuning strategy but gives the lowest accuracy\n"
            "when the new task distribution differs significantly from pretraining.\n\n"
            "Args:\n"
            "    model: ToyPairformer instance whose backbone parameters are frozen.",
            0,
        ),
        (
            r"^def full_finetune_mode\(model\):",
            "Unfreeze all model parameters for end-to-end finetuning.\n\n"
            "Gives the highest accuracy but risks catastrophic forgetting of\n"
            "pretraining knowledge and requires more labelled data to converge.\n\n"
            "Args:\n"
            "    model: ToyPairformer instance — all parameters set requires_grad=True.",
            0,
        ),
        (
            r"^def lora_mode\(model, rank=4\):",
            "Replace all nn.Linear layers with LoRA adapters; freeze base weights.\n\n"
            "Only the low-rank A and B matrices (and bias) are trained, drastically\n"
            "reducing the number of trainable parameters while preserving capacity.\n\n"
            "Args:\n"
            "    model: ToyPairformer instance to inject LoRA adapters into.\n"
            "    rank (int): LoRA rank r (default 4). Higher rank = more parameters.",
            0,
        ),
        # Cell 20: LoRAModel class
        (
            r"^class LoRAModel\(nn\.Module\):",
            "Toy model demonstrating LoRA checkpointing.\n\n"
            "Contains a single LoRA-adapted linear layer to illustrate how adapter\n"
            "weights are saved and reloaded independently of the frozen base model.",
            0,
        ),
        (
            r"^\s{4}def __init__\(self\):\s*$",
            "Initialise with a single LoRA-adapted linear layer (in=10, out=5, rank=4).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Apply the LoRA-adapted linear transformation.\n\n"
            "Args:\n"
            "    x (Tensor): input of shape (..., 10).\n\n"
            "Returns:\n"
            "    Tensor: output of shape (..., 5).",
            8,
        ),
        # Cell 24: compute_rmsd
        (
            r"^def compute_rmsd\(pred, true\):",
            "Compute root-mean-square deviation between predicted and true coordinates.\n\n"
            "Args:\n"
            "    pred (Tensor): predicted coordinates of shape (N, 3).\n"
            "    true (Tensor): ground-truth coordinates of shape (N, 3).\n\n"
            "Returns:\n"
            "    float: RMSD in the same units as the input coordinates.",
            0,
        ),
        # Cell 35: LoRALinear.__init__, forward, n_trainable; ToyProteinModel.__init__, forward; gen_ddg_data
        (
            r"^\s{4}def __init__\(self, in_features, out_features, rank, alpha=16, dropout=0\.0\):",
            "Initialise LoRA-adapted linear layer.\n\n"
            "Args:\n"
            "    in_features (int): input dimension.\n"
            "    out_features (int): output dimension.\n"
            "    rank (int): LoRA rank r.\n"
            "    alpha (float): scaling constant; effective scale = alpha/rank.\n"
            "    dropout (float): dropout applied before the B projection.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Apply frozen weight plus scaled LoRA correction.\n\n"
            "Args:\n"
            "    x (Tensor): input of shape (..., in_features).\n\n"
            "Returns:\n"
            "    Tensor: output of shape (..., out_features).",
            8,
        ),
        (
            r"^\s{4}def n_trainable\(self\):",
            "Return the number of trainable (LoRA adapter) parameters in this layer.",
            8,
        ),
        (
            r"^\s{4}def __init__\(self, rank=4, d_model=128\):",
            "Initialise toy protein model with LoRA-adapted projection layers.\n\n"
            "Args:\n"
            "    rank (int): LoRA rank applied to all linear layers.\n"
            "    d_model (int): hidden representation dimension.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Forward pass through LoRA-adapted projection layers.\n\n"
            "Args:\n"
            "    x (Tensor): input features of shape (batch, d_model).\n\n"
            "Returns:\n"
            "    Tensor: output predictions of shape (batch, 1).",
            8,
        ),
        (
            r"^def gen_ddg_data\(n=400, seq_len=20\):",
            "Generate synthetic ΔΔG mutation data for rank-ablation experiments.\n\n"
            "Args:\n"
            "    n (int): number of synthetic mutations to generate.\n"
            "    seq_len (int): sequence length (determines feature dimension).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: (X features of shape (n, seq_len), y labels of shape (n, 1)).",
            0,
        ),
        # Cell 39 (debug exercise): LoRALayer in debug cell
        (
            r"^\s{4}def __init__\(self, in_dim, out_dim, r\):",
            "Initialise the LoRA adapter (debug exercise version).\n\n"
            "Args:\n"
            "    in_dim (int): input feature dimension.\n"
            "    out_dim (int): output feature dimension.\n"
            "    r (int): LoRA rank.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Apply LoRA adapted linear transformation.\n\n"
            "Args:\n"
            "    x (Tensor): input tensor of shape (..., in_dim).\n\n"
            "Returns:\n"
            "    Tensor: output tensor of shape (..., out_dim).",
            8,
        ),
    ],

    # -----------------------------------------------------------------------
    # 15/01 — Self-Supervised Learning
    # -----------------------------------------------------------------------
    "15/01": [
        # Cell 5: MaskedLM.__init__, forward, apply_mask
        (
            r"^\s{4}def __init__\(self, vocab_size=21, d_model=128, n_heads=4, n_layers=3\):",
            "Initialise the Masked Language Model encoder.\n\n"
            "Args:\n"
            "    vocab_size (int): protein alphabet size + mask token (default 21).\n"
            "    d_model (int): embedding and transformer hidden dimension.\n"
            "    n_heads (int): number of self-attention heads.\n"
            "    n_layers (int): number of transformer encoder layers.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, tokens, mask_positions=None\):",
            "Encode tokens and optionally predict masked positions.\n\n"
            "Args:\n"
            "    tokens (Tensor): integer amino-acid indices of shape (B, L).\n"
            "    mask_positions (Tensor | None): boolean mask of shape (B, L);\n"
            "        if provided, returns logits only at masked positions.\n\n"
            "Returns:\n"
            "    Tensor: logits of shape (B, L, vocab_size) for masked positions.",
            8,
        ),
        (
            r"^def apply_mask\(tokens, mask_token_id=20, vocab_size=20, mask_prob=0\.15\):",
            "Apply BERT-style masking to a token sequence.\n\n"
            "Randomly replaces mask_prob fraction of tokens with mask_token_id.\n\n"
            "Args:\n"
            "    tokens (Tensor): integer amino-acid indices of shape (B, L).\n"
            "    mask_token_id (int): ID of the [MASK] token (default 20).\n"
            "    vocab_size (int): alphabet size, used to generate random replacements.\n"
            "    mask_prob (float): fraction of positions to mask (default 0.15).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: (masked_tokens, boolean mask of shape (B, L)).",
            0,
        ),
        # Cell 6: SimCLREncoder.__init__, forward
        (
            r"^\s{4}def __init__\(self, vocab_size=21, d_model=64, proj_dim=32\):",
            "Initialise SimCLR encoder + projection head.\n\n"
            "Args:\n"
            "    vocab_size (int): size of the amino-acid vocabulary (default 21).\n"
            "    d_model (int): encoder embedding dimension.\n"
            "    proj_dim (int): projection head output dimension for NT-Xent loss.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):\s*$",
            "Encode an augmented view and project to the contrastive space.\n\n"
            "Args:\n"
            "    x (Tensor): token indices of shape (B, L).\n\n"
            "Returns:\n"
            "    Tensor: L2-normalised projection embeddings of shape (B, proj_dim).",
            8,
        ),
        # Cell 7: BYOL.__init__, update_target, forward; SimpleEncoder.__init__, forward
        (
            r"^\s{4}def __init__\(self, encoder, proj_dim=32, pred_dim=32\):",
            "Initialise BYOL online and target networks.\n\n"
            "The target network is an exponential moving average (EMA) of the online\n"
            "network — no negative pairs required.\n\n"
            "Args:\n"
            "    encoder (nn.Module): backbone encoder module.\n"
            "    proj_dim (int): projector output dimension.\n"
            "    pred_dim (int): predictor output dimension (online network only).",
            8,
        ),
        (
            r"^\s{4}def update_target\(self, momentum=0\.996\):",
            "Update target network weights via exponential moving average.\n\n"
            "θ_target ← momentum · θ_target + (1 − momentum) · θ_online\n\n"
            "Args:\n"
            "    momentum (float): EMA decay rate (default 0.996).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x1, x2\):\s*$",
            "Compute BYOL loss between two augmented views.\n\n"
            "The online network predicts the target network's representation.\n"
            "Loss = 2 − 2 · cosine_similarity(prediction, target_projection).\n\n"
            "Args:\n"
            "    x1 (Tensor): first augmented view, shape (B, L).\n"
            "    x2 (Tensor): second augmented view, shape (B, L).\n\n"
            "Returns:\n"
            "    Tensor: scalar BYOL loss.",
            8,
        ),
        (
            r"^class SimpleEncoder\(nn\.Module\):",
            "Minimal encoder for BYOL demonstration.\n\n"
            "Embeds integer tokens and mean-pools to produce a fixed-size vector.",
            0,
        ),
        (
            r"^\s{4}def __init__\(self\):\s*$",
            "Initialise embedding layer (vocab_size=21, embed_dim=16).",
            8,
        ),
        # Cell 8: ESM2Lite class + methods
        (
            r"^class ESM2Lite\(nn\.Module\):",
            "Minimal ESM-2 style protein language model.\n\n"
            "Implements a lightweight transformer encoder with the same interface\n"
            "as Meta's ESM-2, suitable for teaching and rapid prototyping.\n\n"
            "Args:\n"
            "    vocab_size (int): protein alphabet size (default 30 for ESM-2 tokeniser).\n"
            "    d_model (int): embedding and transformer hidden dimension (default 64).\n"
            "    n_heads (int): number of self-attention heads (default 4).\n"
            "    n_layers (int): number of transformer encoder layers (default 3).",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, vocab_size=30, d_model=64, n_heads=4, n_layers=3\):",
            "Build token embedding, positional encoding, and transformer encoder stack.\n\n"
            "Args:\n"
            "    vocab_size (int): protein alphabet size.\n"
            "    d_model (int): model embedding dimension.\n"
            "    n_heads (int): number of multi-head attention heads.\n"
            "    n_layers (int): depth of the transformer encoder.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, tokens\):",
            "Encode a batch of protein sequences into residue-level embeddings.\n\n"
            "Args:\n"
            "    tokens (Tensor): integer amino-acid indices of shape (B, L).\n\n"
            "Returns:\n"
            "    Tensor: contextual residue embeddings of shape (B, L, d_model).",
            8,
        ),
        # Cell 9: ESM2FineTuned.__init__, forward
        (
            r"^\s{4}def __init__\(self, d_model=128, n_classes=3, freeze_backbone=True\):",
            "Initialise ESM-2 backbone with a downstream classification head.\n\n"
            "Args:\n"
            "    d_model (int): ESM-2 hidden dimension.\n"
            "    n_classes (int): number of output classes (3 for Q3 secondary structure).\n"
            "    freeze_backbone (bool): if True, ESM-2 weights are frozen (linear probe mode).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, tokens\):\s*$",
            "Run ESM-2 encoding and apply the classification head.\n\n"
            "Args:\n"
            "    tokens (Tensor): amino-acid token indices of shape (B, L).\n\n"
            "Returns:\n"
            "    Tensor: per-residue class logits of shape (B, L, n_classes).",
            8,
        ),
        # Cell 16: ESM2LinearProbe.__init__, forward; ESM2LoRAHead.__init__, forward; train_epoch, eval_epoch
        (
            r"^\s{4}def __init__\(self, esm_dim=ESM2_DIM, num_classes=NUM_CLASSES\):",
            "Initialise the linear probe head.\n\n"
            "Args:\n"
            "    esm_dim (int): ESM-2 embedding dimension.\n"
            "    num_classes (int): number of secondary structure classes (default 3).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):  # x: \(L, esm_dim\)",
            "Apply linear classification to each residue embedding.\n\n"
            "Args:\n"
            "    x (Tensor): residue embeddings of shape (L, esm_dim).\n\n"
            "Returns:\n"
            "    Tensor: class logits of shape (L, num_classes).",
            8,
        ),
        (
            r"^\s{4}def __init__\(self, esm_dim=ESM2_DIM, bottleneck=64, num_classes=NUM_CLASSES, dropout=0\.1\):",
            "Initialise the LoRA-style bottleneck head.\n\n"
            "Uses a down-project → ReLU → up-project architecture to reduce\n"
            "the number of task-specific trainable parameters.\n\n"
            "Args:\n"
            "    esm_dim (int): ESM-2 embedding dimension.\n"
            "    bottleneck (int): inner bottleneck dimension.\n"
            "    num_classes (int): number of output classes.\n"
            "    dropout (float): dropout rate applied before the output projection.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x\):  # x: \(L, esm_dim\)",
            "Apply bottleneck head to residue embeddings.\n\n"
            "Args:\n"
            "    x (Tensor): residue embeddings of shape (L, esm_dim).\n\n"
            "Returns:\n"
            "    Tensor: class logits of shape (L, num_classes).",
            8,
        ),
        (
            r"^def train_epoch\(model, data, optimizer, criterion\):",
            "Run one training epoch over the secondary structure dataset.\n\n"
            "Args:\n"
            "    model (nn.Module): ESM2LinearProbe or ESM2LoRAHead.\n"
            "    data (list): list of (embedding, label) pairs.\n"
            "    optimizer: PyTorch optimiser.\n"
            "    criterion: loss function (CrossEntropyLoss).\n\n"
            "Returns:\n"
            "    float: mean training loss for the epoch.",
            0,
        ),
        (
            r"^def eval_epoch\(model, data, criterion\):",
            "Evaluate the model on a held-out dataset split.\n\n"
            "Args:\n"
            "    model (nn.Module): ESM2LinearProbe or ESM2LoRAHead.\n"
            "    data (list): list of (embedding, label) pairs.\n"
            "    criterion: loss function (CrossEntropyLoss).\n\n"
            "Returns:\n"
            "    Tuple[float, float]: (mean loss, Q3 per-residue accuracy).",
            0,
        ),
        # Cell 22 (debug): nt_xent_loss, Encoder, Projector
        (
            r"^def nt_xent_loss\(z, temperature\):",
            "NT-Xent loss for contrastive learning (debug exercise version).\n\n"
            "Args:\n"
            "    z (Tensor): stacked projections of shape (2*B, proj_dim) — first B are\n"
            "        original views, next B are augmented views.\n"
            "    temperature (float): softmax temperature τ.\n\n"
            "Returns:\n"
            "    Tensor: scalar NT-Xent loss.",
            0,
        ),
        (
            r"^class Encoder\(nn\.Module\):",
            "Minimal encoder backbone for the debug exercise (identity normalisation).",
            0,
        ),
        (
            r"^class Projector\(nn\.Module\):",
            "Single linear projection head for the debug exercise.",
            0,
        ),
    ],

    # -----------------------------------------------------------------------
    # 12/01 — Diffusion Models
    # -----------------------------------------------------------------------
    "12/01": [
        # Cell 6: DDPMForward.__init__
        (
            r"^class DDPMForward:",
            "DDPM forward (noising) process as a pure Python class.\n\n"
            "Implements the Markov chain q(x_t | x_{t-1}) = N(x_t; √(1-β_t)·x_{t-1}, β_t·I)\n"
            "and the closed-form jump q(x_t | x_0) = N(x_t; √ᾱ_t·x_0, (1-ᾱ_t)·I).",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, T=1000, beta_start=1e-4, beta_end=0\.02\):",
            "Set up the noise schedule.\n\n"
            "Args:\n"
            "    T (int): total number of diffusion timesteps (default 1000).\n"
            "    beta_start (float): initial noise level β_1 (default 1e-4).\n"
            "    beta_end (float): final noise level β_T (default 0.02).",
            8,
        ),
        # Cell 9: NoisePredictor.__init__, forward; DDPMTrainer.__init__, loss
        (
            r"^\s{4}def __init__\(self, data_dim=2, time_embed_dim=32, hidden=128\):",
            "Build the UNet-style noise prediction network.\n\n"
            "Args:\n"
            "    data_dim (int): dimensionality of the data space (default 2 for toy 2D).\n"
            "    time_embed_dim (int): sinusoidal time embedding dimension (default 32).\n"
            "    hidden (int): hidden layer width for the MLP backbone (default 128).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x, t\):\s*$",
            "Predict the noise added to x at timestep t.\n\n"
            "Args:\n"
            "    x (Tensor): noisy data of shape (B, data_dim).\n"
            "    t (Tensor): integer timestep indices of shape (B,).\n\n"
            "Returns:\n"
            "    Tensor: predicted noise ε of shape (B, data_dim).",
            8,
        ),
        (
            r"^class DDPMTrainer:",
            "Wraps the forward process and computes the DDPM training loss.\n\n"
            "The loss is E[||ε − ε_θ(x_t, t)||²] — mean squared error between\n"
            "the true noise and the model's noise prediction.",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, T=1000\):\s*$",
            "Initialise trainer and precompute ᾱ_t schedule.\n\n"
            "Args:\n"
            "    T (int): total number of diffusion timesteps.",
            8,
        ),
        (
            r"^\s{4}def loss\(self, model, x0\):",
            "Compute one DDPM training step loss.\n\n"
            "Samples random timestep t and noise ε, forms x_t, then asks model to\n"
            "predict ε.  Returns MSE between predicted and true noise.\n\n"
            "Args:\n"
            "    model (nn.Module): noise prediction network ε_θ.\n"
            "    x0 (Tensor): clean data batch of shape (B, data_dim).\n\n"
            "Returns:\n"
            "    Tensor: scalar MSE loss.",
            8,
        ),
        # Cell 12: FrameTranslationDiffusion.__init__
        (
            r"^\s{4}def __init__\(self, T=200, c_z=64\):",
            "Initialise protein backbone diffusion module.\n\n"
            "Args:\n"
            "    T (int): number of diffusion timesteps for backbone coordinates.\n"
            "    c_z (int): pair representation dimension from the structure encoder.",
            8,
        ),
        # Cell 15: DDIMSampler.__init__
        (
            r"^\s{4}def __init__\(self, alpha_bar, n_steps=50\):",
            "Set up DDIM deterministic sampler.\n\n"
            "Args:\n"
            "    alpha_bar (Tensor): precomputed ᾱ_t schedule of shape (T,).\n"
            "    n_steps (int): number of DDIM denoising steps (<<T, default 50).",
            8,
        ),
        # Cell 17: FlowMatchingModel.__init__, forward
        (
            r"^\s{4}def __init__\(self, data_dim=2, hidden=128\):",
            "Build the flow-matching vector field network.\n\n"
            "Args:\n"
            "    data_dim (int): dimensionality of the data space (default 2).\n"
            "    hidden (int): hidden layer width (default 128).",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x, t\):\s*$",
            "Predict the vector field u_t(x) at position x and time t.\n\n"
            "Args:\n"
            "    x (Tensor): current sample position of shape (B, data_dim).\n"
            "    t (Tensor): continuous time values in [0, 1] of shape (B, 1).\n\n"
            "Returns:\n"
            "    Tensor: vector field prediction of shape (B, data_dim).",
            8,
        ),
        # Cell 21: make_protein_shapes, q_sample, NoisePredictor.__init__, forward
        (
            r"^def make_protein_shapes\(n=500, n_residues=20\):",
            "Create synthetic 2D 'protein' coordinate data for DDPM demonstration.\n\n"
            "Generates simple geometric shapes (circles and line segments) as stand-ins\n"
            "for protein backbone coordinates — avoids needing real PDB data.\n\n"
            "Args:\n"
            "    n (int): number of synthetic protein samples to generate.\n"
            "    n_residues (int): number of 2D coordinate points per sample.\n\n"
            "Returns:\n"
            "    Tensor: coordinate array of shape (n, n_residues, 2).",
            0,
        ),
        (
            r"^def q_sample\(x0, t\):",
            "Forward diffusion: add noise level t to clean coordinates x0.\n\n"
            "Uses the closed-form equation:\n"
            "    x_t = sqrt(ᾱ_t) · x0 + sqrt(1 − ᾱ_t) · ε,  ε ~ N(0, I)\n\n"
            "Args:\n"
            "    x0 (Tensor): clean data of shape (B, n_residues, 2).\n"
            "    t (Tensor): integer timestep indices of shape (B,).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: (noisy x_t, noise ε), both shape (B, n_residues, 2).",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, n_res=20, coord_dim=2, hidden=128, t_dim=32\):",
            "Build the UNet-style noise predictor for protein coordinate diffusion.\n\n"
            "Conditions on the continuous noise level via a sinusoidal time embedding\n"
            "concatenated with the flattened coordinate input.\n\n"
            "Args:\n"
            "    n_res (int): number of residues (spatial positions).\n"
            "    coord_dim (int): coordinate dimensionality per residue (2 for toy).\n"
            "    hidden (int): hidden layer width.\n"
            "    t_dim (int): sinusoidal time embedding dimension.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, x_t, t\):\s*$",
            "Predict noise in noisy coordinates x_t at timestep t.\n\n"
            "Args:\n"
            "    x_t (Tensor): noisy coordinates of shape (B, n_res, coord_dim).\n"
            "    t (Tensor): integer timestep indices of shape (B,).\n\n"
            "Returns:\n"
            "    Tensor: predicted noise of shape (B, n_res, coord_dim).",
            8,
        ),
        # Cell 22: p_sample, sample
        (
            r"^def p_sample\(x_t, t_val\):",
            "One reverse diffusion step: predict and remove noise at timestep t_val.\n\n"
            "Implements the ε-prediction formulation:\n"
            "    x_{t-1} = (1/√α_t) · (x_t − β_t/√(1−ᾱ_t) · ε_θ(x_t, t)) + σ_t·z\n\n"
            "Args:\n"
            "    x_t (Tensor): noisy sample at timestep t_val, shape (B, n_res, 2).\n"
            "    t_val (int): current integer timestep (counts down from T to 0).\n\n"
            "Returns:\n"
            "    Tensor: denoised sample x_{t-1} of shape (B, n_res, 2).",
            0,
        ),
        (
            r"^def sample\(n_samples=8\):",
            "Full reverse diffusion: generate protein coordinates from pure Gaussian noise.\n\n"
            "Starts from x_T ~ N(0, I) and applies p_sample T times, producing\n"
            "a batch of final protein-like coordinate arrays.\n\n"
            "Args:\n"
            "    n_samples (int): number of structures to generate (default 8).\n\n"
            "Returns:\n"
            "    Tensor: generated coordinates of shape (n_samples, n_res, 2).",
            0,
        ),
    ],

    # -----------------------------------------------------------------------
    # 14/01 — Reinforcement Learning
    # -----------------------------------------------------------------------
    "14/01": [
        # Cell 6: ProteinDesignMDP.__init__, reset, step, _compute_reward
        (
            r"^\s{4}def __init__\(self, target_length=20\):",
            "Initialise the protein design MDP environment.\n\n"
            "Args:\n"
            "    target_length (int): number of amino acids in the target sequence.",
            8,
        ),
        (
            r"^\s{4}def reset\(self\):\s*$",
            "Reset the environment to an empty sequence and return the initial state.\n\n"
            "Returns:\n"
            "    list: empty sequence (starting state for a new episode).",
            8,
        ),
        (
            r"^\s{4}def step\(self, action\):",
            "Append amino acid 'action' to the current sequence and compute reward.\n\n"
            "Args:\n"
            "    action (int): amino acid index (0–19 for standard 20 amino acids).\n\n"
            "Returns:\n"
            "    Tuple[list, float, bool]: (next_state, reward, done).\n"
            "    done is True when the sequence reaches target_length.",
            8,
        ),
        (
            r"^\s{4}def _compute_reward\(self\):",
            "Compute a simple proxy reward based on the current partial sequence.\n\n"
            "Positive reward for hydrophobic residues at even positions,\n"
            "negative reward for charged residues at odd positions (toy rule).\n\n"
            "Returns:\n"
            "    float: scalar reward signal for the current sequence state.",
            8,
        ),
        # Cell 9: DQN.__init__, forward; ReplayBuffer; encode_state
        (
            r"^\s{4}def __init__\(self, state_dim=20\*10, n_actions=20, hidden=128\):",
            "Build the Deep Q-Network MLP.\n\n"
            "Args:\n"
            "    state_dim (int): flattened one-hot state dimension (default 20*10=200).\n"
            "    n_actions (int): number of possible actions (20 amino acids).\n"
            "    hidden (int): hidden layer width.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, state\):\s*$",
            "Compute Q-values for all actions given the current state encoding.\n\n"
            "Args:\n"
            "    state (Tensor): encoded state of shape (B, state_dim).\n\n"
            "Returns:\n"
            "    Tensor: Q-value estimates of shape (B, n_actions).",
            8,
        ),
        (
            r"^class ReplayBuffer:",
            "Experience replay buffer for DQN training.\n\n"
            "Stores (state, action, reward, next_state, done) tuples and samples\n"
            "random mini-batches to break temporal correlations during training.",
            0,
        ),
        (
            r"^\s{4}def __init__\(self, capacity=10000\):",
            "Initialise the replay buffer.\n\n"
            "Args:\n"
            "    capacity (int): maximum number of transitions to store (FIFO).",
            8,
        ),
        (
            r"^\s{4}def push\(self, s, a, r, s_next, done\):",
            "Store a single transition in the buffer.\n\n"
            "Args:\n"
            "    s: current state.\n"
            "    a (int): action taken.\n"
            "    r (float): reward received.\n"
            "    s_next: next state.\n"
            "    done (bool): whether the episode ended.",
            8,
        ),
        (
            r"^\s{4}def sample\(self, batch_size\):",
            "Sample a random mini-batch of transitions.\n\n"
            "Args:\n"
            "    batch_size (int): number of transitions to sample.\n\n"
            "Returns:\n"
            "    list: random sample of (s, a, r, s_next, done) tuples.",
            8,
        ),
        (
            r"^\s{4}def __len__\(self\):",
            "Return the current number of stored transitions.",
            8,
        ),
        (
            r"^def encode_state\(seq, L=10, n_aa=20\):",
            "One-hot encode the current partial protein sequence as a state vector.\n\n"
            "Args:\n"
            "    seq (list): current amino acid index sequence.\n"
            "    L (int): maximum sequence length (pads/truncates to this length).\n"
            "    n_aa (int): amino acid vocabulary size (default 20).\n\n"
            "Returns:\n"
            "    Tensor: flattened one-hot encoding of shape (L * n_aa,).",
            0,
        ),
        # Cell 11: PolicyNetwork.__init__, forward, get_action
        (
            r"^\s{4}def __init__\(self, state_dim=400, n_actions=20, hidden=128\):",
            "Build the REINFORCE policy network.\n\n"
            "Args:\n"
            "    state_dim (int): encoded state dimension.\n"
            "    n_actions (int): number of actions (amino acids).\n"
            "    hidden (int): hidden layer width.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, state\):\s*$",
            "Compute action probability distribution for the given state.\n\n"
            "Args:\n"
            "    state (Tensor): encoded state of shape (B, state_dim).\n\n"
            "Returns:\n"
            "    Tensor: action log-probabilities of shape (B, n_actions) via log_softmax.",
            8,
        ),
        (
            r"^\s{4}def get_action\(self, state\):",
            "Sample one action from the policy distribution.\n\n"
            "Args:\n"
            "    state (Tensor): encoded state of shape (state_dim,).\n\n"
            "Returns:\n"
            "    Tuple[int, Tensor]: (sampled action index, log_prob of that action).",
            8,
        ),
        # Cell 13: ActorCritic.__init__, forward; ppo_loss
        (
            r"^\s{4}def __init__\(self, state_dim=400, n_actions=20, hidden=128\):",
            "Build the actor-critic network for PPO.\n\n"
            "Shared MLP trunk with two heads:\n"
            "  - actor: action logits → policy distribution\n"
            "  - critic: scalar state value estimate V(s)\n\n"
            "Args:\n"
            "    state_dim (int): encoded state input dimension.\n"
            "    n_actions (int): number of discrete actions.\n"
            "    hidden (int): shared trunk hidden width.",
            8,
        ),
        (
            r"^\s{4}def forward\(self, state\):\s*$",
            "Compute action log-probs and value estimate for the given state.\n\n"
            "Args:\n"
            "    state (Tensor): encoded state of shape (B, state_dim).\n\n"
            "Returns:\n"
            "    Tuple[Tensor, Tensor]: (log_probs of shape (B, n_actions), values of shape (B, 1)).",
            8,
        ),
        (
            r"^def ppo_loss\(old_log_probs, log_probs, advantages, values, returns,",
            "Compute the PPO clipped surrogate loss.\n\n"
            "Combines policy loss (clipped importance-weight ratio) and value loss.\n"
            "The clip_eps parameter prevents too-large policy updates per iteration.\n\n"
            "Args:\n"
            "    old_log_probs (Tensor): log-probs from the behaviour policy.\n"
            "    log_probs (Tensor): log-probs from the current policy.\n"
            "    advantages (Tensor): advantage estimates A(s,a).\n"
            "    values (Tensor): critic value predictions V(s).\n"
            "    returns (Tensor): discounted return targets.\n"
            "    clip_eps (float): PPO clipping threshold (default 0.2).\n\n"
            "Returns:\n"
            "    Tensor: scalar combined PPO loss.",
            0,
        ),
        # Cell 15: GFlowNetTB.__init__
        (
            r"^\s{4}def __init__\(self, L=5, hidden=64\):",
            "Initialise the GFlowNet trajectory balance model.\n\n"
            "Args:\n"
            "    L (int): sequence length (number of steps in the trajectory).\n"
            "    hidden (int): hidden dimension for the forward policy network.",
            8,
        ),
        # Cell 23: random_sequence
        (
            r"^def random_sequence\(\):",
            "Sample a random protein sequence of length SEQ_LEN.\n\n"
            "Returns:\n"
            "    str: random sequence of uppercase amino acid letters.",
            0,
        ),
    ],
}


def add_docstring_to_source(source_lines: list, pattern: str, docstring_body: str, indent_spaces: int) -> list:
    """
    Find the first line matching `pattern`, check whether the next non-empty line
    is already a docstring.  If not, insert a docstring after the def/class line.
    Returns the (potentially modified) list of lines.
    """
    pad = " " * indent_spaces
    compiled = re.compile(pattern)
    new_lines = list(source_lines)
    i = 0
    while i < len(new_lines):
        line = new_lines[i]
        if compiled.match(line):
            # Find next non-empty line
            j = i + 1
            while j < len(new_lines) and new_lines[j].strip() == "":
                j += 1
            # If it's already a docstring, skip
            if j < len(new_lines) and ('"""' in new_lines[j] or "'''" in new_lines[j]):
                i += 1
                continue
            # Insert the docstring
            formatted = f'{pad}"""{docstring_body}"""'
            new_lines.insert(i + 1, formatted)
            return new_lines  # only insert once per call
        i += 1
    return new_lines


def apply_fix2(nb: dict, notebook_key: str) -> int:
    """Add docstrings to all undocumented functions/classes.
    Returns number of docstrings inserted."""
    entries = DOCSTRINGS.get(notebook_key, [])
    total_inserted = 0
    cells = nb["cells"]
    for pattern, docstring_body, indent_spaces in entries:
        for cell in cells:
            if cell["cell_type"] != "code":
                continue
            source = "".join(cell["source"])
            lines = source.split("\n")
            new_lines = add_docstring_to_source(lines, pattern, docstring_body, indent_spaces)
            if new_lines != lines:
                cell["source"] = "\n".join(new_lines)
                total_inserted += 1
    print(f"  Fix 2: inserted {total_inserted} docstrings.")
    return total_inserted


# ---------------------------------------------------------------------------
# Fix 3 — Explanation markdown cells before large code blocks
# ---------------------------------------------------------------------------

# Maps: notebook_key -> list of (cell_index_in_original, explanation_markdown)
# We identify cells by their first-line comment / preview so insertion is
# robust to index shifts caused by Fix 1 + Fix 2.

EXPLANATIONS = {
    "10/01": [
        (
            # Cell 33 — protein-level data splitting
            r"# CRITICAL: Protein-level data splitting",
            """\
## Protein-Level Data Splitting — Why Random Splits Fail

When predicting mutation effects (ΔΔG), a random 80/20 split leaks information: \
mutations from the *same protein* appear in both train and test, making the model \
look better than it really is on new proteins.

**The fix:** split by protein complex — all mutations from a given protein go \
entirely into either train or test, never both.  This tests true generalisation.

The code below demonstrates both the naive (wrong) and correct splitting strategies, \
then shows the accuracy gap between them.""",
        ),
        (
            # Cell 34 — ESM-2 loading and embedding
            r"# ESM-2 LOADING AND PROTEIN EMBEDDING",
            """\
## Loading ESM-2 and Embedding Protein Sequences

ESM-2 is a protein language model pretrained on 250 million sequences.  It maps a \
raw amino-acid string like `"MKTIIALSYIFCLVFA"` into a rich numerical embedding \
that captures evolutionary context, secondary structure propensity, and functional \
residue patterns — all without any structure data.

**What the code does:**
1. Loads a small ESM-2 checkpoint (`esm2_t6_8M_UR50D` — 8 M parameters).
2. Tokenises each sequence.
3. Runs a forward pass to extract per-residue embeddings.
4. Mean-pools over positions to get one fixed-size vector per protein.

These vectors become the input features for the ΔΔG regression head.""",
        ),
        (
            # Cell 35 — LoRA rank ablation
            r"# LoRA RANK ABLATION",
            """\
## LoRA Rank Ablation — Choosing the Right Rank

LoRA rank `r` is the most important hyperparameter in adapter-based finetuning.

| rank | extra params | typical use case |
|------|-------------|-----------------|
| 1–2  | minimal     | extreme memory constraints |
| 4    | small       | most protein tasks (recommended default) |
| 8–16 | moderate    | multi-task or low-resource settings |
| 32+  | large       | approaching full-finetune quality |

**What the code does:** trains the same model with ranks 1, 2, 4, 8, 16 and plots \
Pearson r vs. parameter count so you can see the diminishing returns curve.""",
        ),
    ],

    "15/01": [
        (
            # Cell 6 — SimCLR
            r"# SimCLR: Simple Contrastive Learning",
            """\
## SimCLR — Contrastive Representation Learning

SimCLR learns embeddings by pulling together two augmented views of the *same* \
sequence while pushing apart representations of different sequences — no labels needed.

**Key components:**
- **Encoder** — shared transformer backbone processes both views.
- **Projection head** — small MLP applied *on top* of the encoder; the contrastive \
loss is computed in this projected space, not the encoder space.
- **NT-Xent loss** — for each sample in a batch of B, the correct positive pair must \
rank highest among 2(B-1) negatives.

**Intuition:** after training, sequences with similar function cluster together in the \
encoder space even though no functional labels were used.""",
        ),
        (
            # Cell 7 — BYOL
            r"# BYOL: Bootstrap Your Own Latent",
            """\
## BYOL — No Negative Pairs Required

BYOL solves a practical problem with SimCLR: you need large batch sizes to have \
enough negatives.  BYOL avoids negatives entirely by using two networks:

- **Online network** — trained normally via gradient descent.
- **Target network** — an exponential moving average (EMA) of the online network; \
  its weights are updated with `θ_target ← m·θ_target + (1−m)·θ_online`.

The online network learns to *predict* the target network's representation of a \
different augmented view.  This asymmetry (predictor + stop-gradient) prevents \
collapse without needing negative samples.""",
        ),
        (
            # Cell 8 — ESM2 architecture
            r"# ESM2 architecture and downstream fine-tuning",
            """\
## ESM-2 Architecture Overview

ESM-2 is a standard transformer encoder applied directly to amino-acid sequences.  \
The key architectural choices:

| Component | Detail |
|-----------|--------|
| Tokeniser | 33 amino-acid tokens + special tokens |
| Positional encoding | Rotary (RoPE) embeddings |
| Attention | Standard multi-head self-attention |
| Depth | 6 layers (8M), 12 layers (35M), 33 layers (650M), 48 layers (15B) |

**Why it works:** protein sequences have long-range co-evolutionary constraints \
(residues far apart in sequence contact each other in 3D space).  Transformer \
attention can capture these directly, unlike CNNs or RNNs.""",
        ),
        (
            # Cell 9 — Downstream fine-tuning
            r"# Downstream fine-tuning: ESM2 \+ classification head",
            """\
## Downstream Fine-Tuning — Adapting ESM-2 to a New Task

After pretraining, ESM-2 embeddings can be adapted to labelled tasks in two modes:

**Linear probe (frozen backbone):**
```
ESM-2 (frozen) → mean pool → Linear(d_model, n_classes) → CrossEntropy
```
Fast, memory-efficient, but limited if the task is very different from pretraining.

**Full fine-tuning:**
```
ESM-2 (trainable) → per-residue → Linear(d_model, n_classes) → CrossEntropy
```
Best accuracy, but risks catastrophic forgetting and needs more data.

The code below shows both modes on a secondary structure (Q3) prediction task.""",
        ),
        (
            # Cell 10 — SSL comparison
            r"# SSL comparison: MLM vs SimCLR vs BYOL",
            """\
## SSL Methods — Side-by-Side Comparison

Before running the comparison code, here is a quick reference:

| Method | Labels? | Key Idea | Protein Use Case |
|--------|---------|----------|-----------------|
| MLM | No | Predict masked amino acids | ESM-2 pretraining |
| SimCLR | No | Contrastive augmented views | Representation learning with large batches |
| BYOL | No | Online predicts target EMA | Representation learning, small batches |

All three are evaluated on the same downstream task (secondary structure Q3) \
via a frozen linear probe — this isolates representation quality from task-specific capacity.""",
        ),
        (
            # Cell 16 — ESM2 fine-tuning section
            r"# ── ESM-2 fine-tuning: frozen backbone \+ linear head",
            """\
## ESM-2 Fine-Tuning — Linear Probe vs LoRA Head

This section compares two parameter-efficient strategies for adapting frozen ESM-2 \
embeddings to secondary structure prediction:

**Linear probe:** a single `Linear(esm_dim, 3)` layer trained on top of frozen \
mean-pooled embeddings.  Extremely fast; a strong baseline.

**LoRA-style bottleneck head:** `Linear(esm_dim, 64) → ReLU → Linear(64, 3)`.  \
More expressive with only a small parameter overhead.

Neither strategy modifies the ESM-2 backbone weights — they differ only in the \
complexity of the task-specific head.""",
        ),
    ],

    "12/01": [
        (
            # Cell 22 — Reverse process sampling
            r"# REVERSE PROCESS: Sample new protein structures from noise",
            """\
## Reverse Diffusion — Generating Protein Structures from Noise

After the model is trained to predict noise (ε-prediction), generation works by \
running the reverse Markov chain from pure Gaussian noise back to clean data:

```
x_T ~ N(0, I)
for t = T, T-1, ..., 1:
    ε_pred = model(x_t, t)
    x_{t-1} = (x_t - β_t/√(1-ᾱ_t) · ε_pred) / √α_t  + σ_t · z
```

**Key insight:** the model never sees the final answer during training — it only \
learns to remove a *small* amount of noise at each step.  Stacking T such steps \
turns pure noise into a realistic protein-like coordinate cloud.

The code below runs this loop and visualises the denoising trajectory.""",
        ),
    ],

    # 14/01 has no large code cells without preceding markdown (confirmed above)
    "14/01": [],
}


def find_cell_index_by_pattern(cells: list, pattern: str) -> int:
    """Return the index of the first code cell whose source starts with the given regex pattern."""
    compiled = re.compile(pattern)
    for i, c in enumerate(cells):
        if c["cell_type"] == "code":
            src = "".join(c["source"])
            first_line = src.split("\n")[0] if src else ""
            if compiled.search(first_line) or compiled.search(src[:120]):
                return i
    return -1


def apply_fix3(nb: dict, notebook_key: str) -> int:
    """Insert explanation markdown cells before large code blocks that lack one.
    Returns number of cells inserted."""
    entries = EXPLANATIONS.get(notebook_key, [])
    cells = nb["cells"]
    inserted = 0

    # Process in reverse order so earlier insertions don't shift later indices
    placements = []
    for pattern, explanation in entries:
        idx = find_cell_index_by_pattern(cells, pattern)
        if idx == -1:
            print(f"  Fix 3: WARNING — could not find cell matching {pattern!r}")
            continue
        # Check preceding cell isn't already a markdown explanation we inserted
        if idx > 0 and cells[idx - 1]["cell_type"] == "markdown":
            prev_src = "".join(cells[idx - 1]["source"])
            # If the preceding markdown already covers this (same first heading), skip
            first_heading = explanation.split("\n")[0]
            if first_heading in prev_src:
                print(f"  Fix 3: explanation already present before cell {idx}, skipping.")
                continue
        placements.append((idx, explanation))

    # Sort descending by index for safe reverse insertion
    placements.sort(key=lambda x: x[0], reverse=True)
    for idx, explanation in placements:
        new_cell = md_cell(explanation)
        cells.insert(idx, new_cell)
        inserted += 1
        print(f"  Fix 3: inserted explanation before code cell (now at {idx+1}).")

    return inserted


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

NOTEBOOKS = [
    (
        "/home/recep/Desktop/Machine_Learning/projects/hackerrank/10_openfold3_finetuning/01_protein_structure_finetuning.ipynb",
        "10/01",
    ),
    (
        "/home/recep/Desktop/Machine_Learning/projects/hackerrank/15_self_supervised_learning/01_contrastive_ssl.ipynb",
        "15/01",
    ),
    (
        "/home/recep/Desktop/Machine_Learning/projects/hackerrank/12_generative_models/01_diffusion_protein_design.ipynb",
        "12/01",
    ),
    (
        "/home/recep/Desktop/Machine_Learning/projects/hackerrank/14_reinforcement_learning/01_rl_protein_design.ipynb",
        "14/01",
    ),
]


def process_notebook(path: str, notebook_key: str):
    print(f"\n{'='*60}")
    print(f"Processing {notebook_key}: {path}")
    print(f"{'='*60}")

    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    original_cell_count = len(nb["cells"])
    print(f"  Original cell count: {original_cell_count}")

    # Normalise source fields: nbformat can store source as list or string
    for cell in nb["cells"]:
        if isinstance(cell["source"], list):
            cell["source"] = "".join(cell["source"])

    n1 = apply_fix1(nb, notebook_key)
    n2 = apply_fix2(nb, notebook_key)
    n3 = apply_fix3(nb, notebook_key)

    # Validate that all cell IDs are unique 8-char hex
    ids_seen = set()
    for cell in nb["cells"]:
        cid = cell.get("id", "")
        if not cid or not re.match(r"^[0-9a-f]{8}$", cid):
            cell["id"] = make_cell_id()
        elif cid in ids_seen:
            cell["id"] = make_cell_id()
        ids_seen.add(cell["id"])

    # Ensure nbformat_minor is 5 (required for cell IDs)
    nb["nbformat"] = 4
    nb["nbformat_minor"] = 5

    # Validate JSON serialisability before writing
    serialised = json.dumps(nb, ensure_ascii=False, indent=1)
    json.loads(serialised)  # will raise if invalid

    with open(path, "w", encoding="utf-8") as f:
        f.write(serialised)

    final_cell_count = len(nb["cells"])
    total_new = n1 + n3
    print(f"  Final cell count: {final_cell_count} (+{total_new} cells inserted)")
    print(f"  JSON validation: PASSED")
    return {"fix1": n1, "fix2": n2, "fix3": n3}


if __name__ == "__main__":
    summary = {}
    for path, key in NOTEBOOKS:
        result = process_notebook(path, key)
        summary[key] = result

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for key, counts in summary.items():
        print(f"  {key}: Fix1={counts['fix1']} cells, Fix2={counts['fix2']} docstrings, Fix3={counts['fix3']} cells")
    print("\nAll notebooks updated and validated successfully.")
