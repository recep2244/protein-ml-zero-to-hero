# Module 05 — Deep Learning & Fine-Tuning
This module is the deep learning engine room of the curriculum — CNNs, sequence models, Transformers, LoRA fine-tuning, and training diagnostics — everything needed before tackling AlphaFold3 and GNNs.

## What You'll Learn
- Build and train Convolutional Neural Networks (CNNs) for biological sequence and image classification
- Implement EarlyStopping, learning rate schedulers, and gradient clipping for robust training
- Understand and visualize attention mechanisms and the Transformer architecture
- Fine-tune pretrained models using LoRA (Low-Rank Adaptation) with minimal trainable parameters
- Design BiLSTM and RNN architectures for sequence labeling (secondary structure prediction)
- Diagnose training problems: gradient flow visualization, loss curves, overfitting/underfitting
- Apply fine-tuning best practices: learning rate warm-up, layer freezing, discriminative learning rates

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PyTorch tensors, autograd, `nn.Module` | `00_python_ml_basics/06_pytorch_fundamentals.ipynb` |
| Backpropagation and gradient descent math | `00_python_ml_basics/08_mathematical_foundations.ipynb` |
| Scikit-learn evaluation metrics | `00_python_ml_basics/02_ml_fundamentals.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_dl_and_finetuning.ipynb` | CNNs, Transformers, attention, LoRA, EarlyStopping, gradient flow, fine-tuning strategies | ~8h |
| 2 | `02_sequence_models_rnn_lstm.ipynb` | RNNs, LSTMs, BiLSTMs, CRFs, secondary structure prediction, vanishing gradients | ~6h |

## After This Module You Can
- Train a CNN or Transformer on a biological sequence classification task end-to-end
- Apply LoRA to fine-tune a pretrained model using fewer than 1% of the original parameters
- Diagnose and fix common training failures (vanishing gradients, learning rate too high/low, overfit)
- Build a BiLSTM for per-residue sequence labeling with correct padding and masking
- Explain the Transformer's self-attention mechanism mathematically and implement a minimal version

## Key Concepts Introduced
- **LoRA (Low-Rank Adaptation)**: Fine-tuning technique that injects trainable low-rank matrices into frozen weight layers, drastically reducing parameter count.
- **EarlyStopping**: Training callback that halts optimization when validation loss stops improving, preventing overfitting.
- **Self-attention**: Mechanism that computes a weighted sum of value vectors using query-key dot-product scores, enabling long-range dependencies.
- **Vanishing gradient**: Problem where gradients shrink exponentially through deep networks, preventing early layer learning; addressed by LSTMs and residual connections.
- **BiLSTM**: Bidirectional LSTM that processes sequences in both forward and backward directions, doubling context at each position.
- **Gradient clipping**: Technique that caps gradient norms during backprop to prevent exploding gradients in RNNs.

## Next Module
→ [Module 06 — Structural ML & GNNs](../06_structural_ml_gnns/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 14–18 hours
