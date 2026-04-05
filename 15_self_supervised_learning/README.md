# Module 15 — Self-Supervised Learning for Proteins
This module covers the pre-training paradigm that powers ESM2, ProteinBERT, and every modern protein foundation model — masked language modeling, SimCLR, BYOL, and the full SSL-to-fine-tune pipeline for label-scarce biological tasks.

## What You'll Learn
- Implement BERT-style masked language modeling for protein sequences with correct 80/10/10 masking rules
- Build a simplified ESM2 architecture (Pre-LN Transformer, RoPE, masked LM head)
- Implement NT-Xent (SimCLR) contrastive loss with temperature scaling from scratch
- Build a SimCLR training loop with sequence augmentations and projection head
- Understand BYOL's online/target network design and why it works without negative pairs
- Load and use ESM2 via HuggingFace to extract per-residue embeddings
- Compare linear probe vs full fine-tune vs LoRA on low-data downstream tasks

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PyTorch `nn.Module` and training loops | `00_python_ml_basics/06_pytorch_fundamentals.ipynb` |
| Transformer architecture and self-attention | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| HMM and sequence model background (helpful) | `01_sequence_analysis/07_hidden_markov_models.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_contrastive_ssl.ipynb` | Masked LM tokenization, ProteinTransformer, NT-Xent loss, SimCLR, BYOL, ESM2 interface, linear probe vs fine-tune comparison | ~8h |

## After This Module You Can
- Pre-train a simplified protein language model on unlabeled sequences using masked LM
- Implement SimCLR contrastive learning for protein sequences and evaluate embedding quality with kNN accuracy
- Explain why BYOL does not need negative pairs and how EMA target networks prevent representation collapse
- Extract per-residue ESM2 embeddings from HuggingFace and use them as features for any downstream task
- Choose appropriately between linear probe, LoRA, and full fine-tuning based on dataset size

## Key Concepts Introduced
- **Masked Language Modeling (MLM)**: Self-supervised objective where 15% of input tokens are masked and the model predicts them; learns rich contextual representations without labels.
- **NT-Xent loss**: Normalized temperature-scaled cross-entropy loss used in SimCLR; pulls representations of augmented views of the same sequence together while pushing others apart.
- **SimCLR**: Contrastive self-supervised learning framework using data augmentations, a projection head, and NT-Xent loss; requires large batch sizes for negative pairs.
- **BYOL (Bootstrap Your Own Latent)**: Non-contrastive SSL framework using online and target networks with EMA updates and a predictor asymmetry to avoid representation collapse without negatives.
- **ESM2**: Meta's protein language model trained on 250M UniRef sequences with masked LM; the current standard protein foundation model for embedding and fine-tuning.
- **Linear probe**: Evaluation protocol that freezes pretrained features and trains only a linear classifier on top; measures representation quality without full fine-tuning cost.
- **RoPE (Rotary Position Embedding)**: Position encoding scheme that encodes relative positions via rotation of query/key vectors; used in ESM2 and modern LLMs.

## Next Module
→ [Module 16 — MLOps & Deployment](../16_mlops_deployment/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
