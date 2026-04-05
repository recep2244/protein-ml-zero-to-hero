# Module 14 — Reinforcement Learning for Protein Design
This module teaches RL as a language for sequential biological optimization — from Q-learning fundamentals through DQN, PPO, GFlowNets, and Bayesian optimization applied to directed evolution and drug design.

## What You'll Learn
- Formulate protein sequence optimization as a Markov Decision Process (state, action, reward)
- Implement Q-learning and deep Q-networks (DQN) with experience replay and target networks
- Understand and implement REINFORCE (policy gradient) and Proximal Policy Optimization (PPO)
- Explain why PPO stabilizes policy updates via clipped surrogate objectives
- Understand GFlowNets as a distinct generative framework for diversity-aware exploration
- Apply Bayesian optimization for protein engineering loops when function evaluations are expensive
- Design reward functions for multi-objective optimization (stability + activity + novelty)

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| PyTorch training loops and neural networks | `05_deep_learning_finetuning/01_dl_and_finetuning.ipynb` |
| Diffusion models and generative model intuition | `12_generative_models/01_diffusion_protein_design.ipynb` |
| Bayesian optimization and Gaussian processes | `13_bayesian_methods/01_bayesian_ml_uncertainty.ipynb` |
| Basic probability and Markov chains | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_rl_protein_design.ipynb` | MDP formulation, Q-learning, DQN, REINFORCE, PPO, GFlowNets, multi-objective reward design, Bayesian optimization for drug design | ~8h |

## After This Module You Can
- Formulate a directed evolution campaign as an MDP with appropriate state and reward definitions
- Implement a DQN agent for discrete sequence optimization with experience replay
- Explain PPO's clipped surrogate objective and why it prevents destructive policy updates
- Describe how GFlowNets generate diverse high-reward sequences and contrast them with standard RL
- Spot reward hacking in a protein design loop and redesign the reward function to prevent it

## Key Concepts Introduced
- **MDP (Markov Decision Process)**: Formal framework for sequential decision-making: state S, action A, transition T, reward R, discount gamma.
- **DQN (Deep Q-Network)**: Value-based RL algorithm using a neural network to approximate Q(s,a) with experience replay and target networks for stability.
- **PPO (Proximal Policy Optimization)**: Policy gradient method using a clipped surrogate objective to prevent large policy updates, offering stable on-policy learning.
- **GFlowNet**: Generative model trained to sample objects (sequences, structures) proportional to a reward function, naturally encouraging diverse rather than mode-seeking generation.
- **Reward hacking**: Failure mode where an RL agent achieves high reward by exploiting loopholes in the reward function rather than genuinely solving the intended task.
- **Multi-objective RL**: Optimization of policies under multiple competing reward signals (stability, binding affinity, solubility) using Pareto front or scalarization approaches.

## Next Module
→ [Module 15 — Self-Supervised Learning](../15_self_supervised_learning/README.md)

## Difficulty: ⭐⭐⭐⭐ (1–5 stars)
## Estimated Time: 8–12 hours
