# Curriculum — Topic Map by Notebook

A detailed breakdown of every topic covered, with difficulty ratings and prerequisites.
The current repository contains 39 notebooks across 17 modules.

**Difficulty scale**: ⭐ Beginner | ⭐⭐ Intermediate | ⭐⭐⭐ Advanced | ⭐⭐⭐⭐ Expert

---

## Module 0 — Python & ML Basics

### 01_python_core_for_bioinformatics ⭐
**Goal**: Write Python fluently for biology data

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| DNA strings | Complement, reverse complement, translation | `rc = dna.translate(...)[::-1]` |
| k-mers | Sliding window, frequency counting | `Counter(seq[i:i+k] for i in range(...))` |
| FASTA parser | File format, generator-based streaming | `def parse_fasta(text)` |
| OOP | Classes, dataclasses, `__repr__` | `class SequenceRecord` |
| Regex | Pattern matching on sequences | `re.findall(r'ATG...', seq)` |
| NumPy basics | Arrays, vectorized operations, broadcasting | `np.array`, `np.sum`, slicing |

**After this notebook**: You can parse any biological sequence file and manipulate DNA/protein strings efficiently.

---

### 02_ml_fundamentals ⭐⭐
**Goal**: Build correct ML pipelines for biology tasks

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Data leakage | Why split BEFORE any preprocessing | `train_test_split(stratify=y)` |
| Pipeline | Scaler + model bundled together | `Pipeline([('scaler', ...), ('clf', ...)])` |
| Cross-validation | StratifiedKFold, leave-one-out | `cross_val_score(cv=StratifiedKFold(5))` |
| Metrics | Accuracy, F1, AUC-ROC, PR-AUC, MCC | `classification_report(y_true, y_pred)` |
| Feature selection | SelectKBest, RFECV, univariate tests | Within pipeline, not before split |
| Imbalanced data | class_weight, SMOTE, PR-AUC | `class_weight='balanced'` |
| Hyperparameter tuning | GridSearchCV, RandomizedSearchCV | `GridSearchCV(pipeline, param_grid)` |

---

### 03_hackerrank_all_modules ⭐⭐
**Goal**: Pass HackerRank Python + ML certifications

Covers all HackerRank assessment domains: Python, Statistics, ML Basic/Intermediate, Data Structures.

---

### 04_hackerrank_python_track ⭐
**Goal**: Python HackerRank problems solved with explanations

All Easy + Medium problems from HackerRank's Python track with time complexity analysis.

---

### 05_hackerrank_statistics_ml_tracks ⭐⭐
**Goal**: Statistics and ML track problems

Probability, distributions, hypothesis testing, regression, classification problems.

---

### 06_pytorch_fundamentals ⭐⭐
**Goal**: Learn modern PyTorch by building and training neural nets directly

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Tensor ops | Shapes, broadcasting, indexing, dtype/device movement | `torch.tensor`, `reshape`, `to(device)` |
| Autograd | Computational graphs and gradients | `loss.backward()` |
| Modules | `nn.Module`, parameters, forward pass design | `class MLP(nn.Module)` |
| Optimization | SGD/Adam training loops | `optimizer.step()` |
| Data loading | Batching, shuffling, dataset wrappers | `DataLoader(dataset, batch_size=...)` |
| Regularization | Dropout, weight decay, early stopping intuition | Training-loop variants |

---

### 07_tensorflow_keras ⭐⭐
**Goal**: Build the same core DL intuition in TensorFlow / Keras

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Keras APIs | Sequential vs Functional models | `tf.keras.Sequential([...])` |
| Layers | Dense, Conv, normalization, dropout | `tf.keras.layers.Dense(...)` |
| Input pipelines | Streaming, preprocessing, batching | `tf.data.Dataset.from_tensor_slices(...)` |
| Training control | Callbacks, checkpoints, LR schedules | `ModelCheckpoint`, `EarlyStopping` |
| Fine-tuning | Frozen backbone + task-specific head | `layer.trainable = False` |

---

### 08_mathematical_foundations ⭐⭐
**Goal**: Cover the math needed for the later ML and protein-model notebooks

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Linear algebra | Vectors, matrices, eigenvalues, SVD | `np.linalg.svd(X)` |
| Calculus | Derivatives, gradients, chain rule | Manual derivative checks |
| Probability | Distributions, expectation, variance | Simulation-based estimators |
| Optimization | Loss landscapes, convexity intuition | Gradient descent demos |
| Statistics | Sampling error, confidence intervals | Bootstrap / Monte Carlo examples |

---

### 09_classical_ml_advanced ⭐⭐⭐
**Goal**: Extend beyond baseline sklearn models into higher-signal classical ML methods

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Support vector machines | Margin maximization, kernels | `SVC(kernel='rbf')` |
| Gaussian processes | Posterior mean + uncertainty | `GaussianProcessRegressor(...)` |
| Gradient boosting / XGBoost | Strong tabular baselines | `XGBClassifier(...)` |
| UMAP | Nonlinear manifold visualization | `umap.UMAP(...).fit_transform(X)` |
| Model comparison | Bias, variance, calibration, runtime tradeoffs | Side-by-side benchmark code |

---

## Module 1 — Sequence Analysis

### 01_alignment_algorithms ⭐⭐
**Goal**: Implement classic sequence alignment from scratch

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Edit distance | Levenshtein DP table | `dp[i][j] = min(insert, delete, substitute)` |
| Needleman-Wunsch | Global alignment with gap penalty | `needleman_wunsch(s1, s2, match, gap)` |
| Smith-Waterman | Local alignment (best substring match) | `smith_waterman(s1, s2)` |
| Traceback | Recovering the alignment from DP table | `def traceback(dp, s1, s2)` |
| BLOSUM62 | Substitution matrix for protein alignment | Pre-loaded, used in scoring |
| Semi-global | For read-to-reference alignment | `semiglobal_align(read, reference)` |
| Algorithm selection | When to use global vs local | Decision guide + interview tips |

---

### 02_rosalind_complete ⭐⭐
**Goal**: 50+ classic Rosalind bioinformatics problems

Complete coverage of Rosalind.info problem categories:
- DNA/RNA/Protein string problems
- Probability problems
- Combinatorics (Fibonacci, Mendelian genetics)
- Graph problems (Hamiltonian path, overlap graphs)

---

### 03_rosalind_combinatorics_strings ⭐⭐
**Goal**: Combinatorics and advanced string problems

Motif finding, restriction enzyme sites, protein inference, base composition across positions.

---

### 04_rosalind_alignment_advanced ⭐⭐⭐
**Goal**: Advanced alignment variants

| Topic | Concept |
|-------|---------|
| Fitting alignment | Find best substring in reference matching query |
| Overlap alignment | End-to-end for sequence assembly |
| Profile alignment | Align sequence to conservation profile |
| Affine gap penalty | Open + extend penalty (biological reality) |

---

### 05_rosalind_phylogeny ⭐⭐⭐
**Goal**: Evolutionary tree construction

| Topic | Concept |
|-------|---------|
| Distance matrix | Pairwise sequence divergence |
| UPGMA | Unweighted pair group method with arithmetic mean |
| Neighbor joining | More accurate tree construction |
| Parsimony | Maximum parsimony tree scoring |

---

### 06_rosalind_assembly_massspec ⭐⭐⭐
**Goal**: Genome assembly and mass spectrometry

| Topic | Concept |
|-------|---------|
| De Bruijn graph | k-mer overlap graph for assembly |
| Eulerian path | Traversal algorithm for assembly |
| Peptide mass spectrum | Converting mass list to amino acid sequence |
| Spectral convolution | Finding mass differences in spectra |

---

### 07_hidden_markov_models ⭐⭐⭐
**Goal**: Use HMMs for biological sequence modeling

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Hidden states | Latent biological regimes behind observed symbols | State diagrams + toy models |
| Forward algorithm | Efficient marginal likelihood computation | `forward(obs, A, B, pi)` |
| Backward algorithm | Reverse dynamic program for posteriors | `backward(obs, A, B)` |
| Viterbi decoding | Most likely hidden-state path | `viterbi(obs, A, B, pi)` |
| Posterior decoding | State probabilities at each position | `posterior_decode(...)` |
| Bioinformatics usage | CpG islands, transmembrane segments, profile HMM intuition | HMM case studies |

---

## Module 2 — Genomics & Gene Analysis

### 01_genomics_core ⭐⭐
**Goal**: Implement the central dogma computationally

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Central dogma | DNA → mRNA → Protein | `translate(transcribe(dna))` |
| Codon table | All 64 codons → amino acids | Complete lookup dict |
| ORF finding | 6 reading frames, start/stop codons | `find_orfs(seq, all_frames=True)` |
| Variant effects | Synonymous vs nonsynonymous mutations | `predict_variant(codon, pos, alt)` |
| Jukes-Cantor | Phylogenetic distance with multiple hit correction | `jc_distance(p)` |
| CpG islands | Methylation context in genomics | `find_cpg_islands(seq, window)` |

---

## Module 3 — Protein Structural Biology

### 01_structure_analysis ⭐⭐⭐
**Goal**: Work with 3D protein structures

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| PDB format | Fixed-width columns, ATOM records | `parse_pdb(text)` → list of atoms |
| RMSD | Average distance between corresponding atoms | `rmsd(coords1, coords2)` |
| Kabsch algorithm | Optimal rotation matrix to minimize RMSD | `kabsch_superposition(P, Q)` |
| TM-score | Length-normalized fold similarity | `tm_score(pred, true)` |
| Dihedral angles | Phi/psi backbone angles, Ramachandran | `dihedral(a, b, c, d)` |
| Contact map | Binary matrix: close residue pairs | `contact_map(ca_coords, threshold=8.0)` |
| B-factor | Crystallographic temperature factor (disorder) | Parsed from PDB |

---

## Module 4 — ML for Omics Data

### 01_ml_for_omics ⭐⭐⭐
**Goal**: Correctly apply ML to high-dimensional biology data

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| RNA-seq data | Gene expression matrix (samples × genes) | Load + preprocess synthetic data |
| Variance filter | Remove near-constant genes | `VarianceThreshold(threshold=0.1)` |
| PCA | Dimensionality reduction + batch effect visualization | `PCA(n_components=50)` |
| p >> n problem | Why gene selection must be inside CV | Correct pipeline structure |
| Class imbalance | Rare subtypes, weighted loss, SMOTE | `class_weight='balanced'` |
| Multi-class metrics | Macro F1, per-class AUC, confusion matrix | Full report function |
| Clustering | K-means + elbow method for unsupervised subtypes | `KMeans(n_clusters=k)` |
| Survival analysis | Cox proportional hazards concepts | Kaplan-Meier plotting |

---

## Module 5 — Deep Learning & Fine-Tuning

### 01_dl_and_finetuning ⭐⭐⭐
**Goal**: Build and fine-tune deep learning models for biology

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| 1D CNN | Sliding filter detects sequence motifs | `nn.Conv1d(4, 128, kernel_size=9)` |
| Attention mechanism | Query-key-value dot product attention | `attn = softmax(QK^T / sqrt(d)) V` |
| Transformer block | Multi-head attention + FFN + residual | Full block implementation |
| Transfer learning | Freeze base model, train head | `param.requires_grad = False` |
| Differential LR | Lower LR for pre-trained layers | `optimizer = Adam([{'params': head, 'lr': 1e-3}, ...])` |
| LoRA | Low-rank weight update matrices | `LoRALinear(rank=8)` from scratch |
| ESM-2 fine-tuning | Protein language model → function prediction | HuggingFace integration |

---

## Module 6 — Structural ML & GNNs

### 01_structure_ml ⭐⭐⭐⭐
**Goal**: Build graph neural networks for protein structure

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Protein graph | Nodes = residues, edges = contacts | `build_protein_graph(ca_coords, aa_types)` |
| Node features | AA type, secondary structure, depth | One-hot + continuous features |
| Edge features | Distance, relative orientation | Radial basis function encoding |
| Message passing | Collect → Aggregate → Update | `MessagePassingLayer` from scratch |
| Global pooling | Residue embeddings → protein embedding | Mean + attention pooling |
| SE(3) invariance | Features unchanged under rotation/translation | Distance-based features |
| Protein function prediction | Binary + multi-label GO terms | Full GNN pipeline |

---

### 02_gnn_deep_dive ⭐⭐⭐⭐
**Goal**: Go beyond one message-passing layer into the modern GNN toolbox

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| GCN | Neighborhood averaging with learned projections | `GCNLayer` |
| GAT | Attention-weighted neighbor aggregation | `GATLayer` |
| GIN | Injective neighborhood updates for expressivity | `GINLayer` |
| EGNN | Coordinate-updating equivariant message passing | `EGNNLayer` |
| PyG workflow | Dataset loaders, batching, graph utilities | `Data`, `DataLoader` |
| Over-smoothing | Why deep GNNs collapse and how to mitigate it | Diagnostic experiments |
| Graph transformers | Attention with graph structure bias | Transformer-style graph block |

---

## Module 7 — AlphaFold 3 Core

### 01_af3_architecture ⭐⭐⭐⭐
**Goal**: Implement AF3's core algorithmic innovations

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Backbone frames | N-CA-C → Gram-Schmidt → (R, t) | `make_backbone_frame(n, ca, c)` |
| FAPE loss | Frame-aligned point error, clamped at 10Å | `fape_loss(pred_frames, true_frames, ...)` |
| Triangle attention (start) | i-j pair attends to all k, bias from i-k | `TriangleAttentionStartingNode` |
| Triangle attention (end) | Transpose input, same as start | `TriangleAttentionEndingNode` |
| Triangle multiplicative | sum_k a[i,k] * b[j,k] without softmax | `TriangleMultiplicativeUpdate` |
| Outer product mean | MSA → pair repr: mean_s(a_si ⊗ b_sj) | `OuterProductMean` |
| Pairformer block | All 4 triangle ops + pair transition + single update | `PairformerBlock` |
| lDDT / pLDDT | 50-bin logits → confidence per residue | `compute_lddt_per_residue` |
| Recycling loop | N forward passes, gradient only on last | `MockAF3Model` with `no_grad()` |

---

### 02_af3_data_pipeline ⭐⭐⭐⭐
**Goal**: Build AF3's input featurization from raw data

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| mmCIF parsing | Atom records, chain IDs, residue numbering | `parse_mmcif(cif_text)` |
| Atom14 | 14-slot per-residue atom representation | `build_atom14_mask(residue_type)` |
| MSA featurization | (S, N, 23): 21 one-hot + deletion features | `featurize_msa(sequences)` |
| Multi-molecule tokenization | Protein + DNA + RNA + ligand tokens | `BioMoleculeTokenizer` |
| Diffusion noise | LogNormal(−1.2, 1.5) sigma schedule | `af3_noise_schedule(n_samples)` |
| Forward diffusion | x_noisy = x_true + sigma × epsilon | `forward_diffusion(x, sigma)` |
| Spatial cropping | N nearest residues to random center | `spatial_crop(coords, chains)` |
| Interface cropping | 50% prob: crop at inter-chain contacts | `interface_crop(coords, chains)` |
| Violation loss | Bond length + steric clash penalty | `bond_length_violation`, `steric_clash_penalty` |

---

### 03_af3_evaluation ⭐⭐⭐⭐
**Goal**: Compute all AF3 confidence and accuracy metrics

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| PAE computation | Frame-aligned position error per (i,j) pair | `compute_pae_from_structures` |
| Domain detection | Connected components from PAE < threshold | `pae_to_domains(pae_matrix)` |
| pTM score | Predicted TM-score from PAE diagonal | `compute_ptm(pae_matrix)` |
| ipTM score | Interface-focused TM-score | `compute_iptm(pae, chain_a, chain_b)` |
| AF3 ranking | 0.8 × ipTM + 0.2 × pTM | `af3_ranking_score(iptm, ptm)` |
| DockQ | Fnat + iRMSD + LRMSD composite | `dockq_score(pred_A, pred_B, true_A, true_B)` |
| SE(3) invariance | Features unchanged under rotation+translation | `verify_invariance(coords, feat_fn)` |
| Invariant pair features | (N,N,32) tensor, invariant to rigid motions | `compute_invariant_pair_features(coords)` |

---

### 04_af3_fullscale_and_ccd ⭐⭐⭐⭐
**Goal**: Production-scale AF3 with GPU optimization + ligand handling

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Memory analysis | Pair repr GB at different N values | `estimate_pairformer_memory(N)` |
| Chunked triangle attn | O(N²×c) instead of O(N³) | `ChunkedTriangleAttentionStartingNode` |
| Gradient checkpointing | Recompute activations in backward | `checkpoint(self._pair_ops, z)` |
| Mixed precision | bfloat16 vs float16, GradScaler | `torch.autocast` + `GradScaler` |
| Full Pairformer | 48 blocks, d_pair=128, d_single=384 | `FullScalePairformer` |
| CCD parsing | mmCIF → atom names, bonds, SMILES | `parse_ccd_entry(cif_text)` |
| Atom graph | CCD → node/edge feature tensors | `ccd_to_atom_graph(entry)` |
| Ligand embedder | Message-passing GNN for ligand tokens | `LigandAtomEmbedder` |
| Unified tokens | Protein residues + ligand atoms → one sequence | `UnifiedTokenSequence` |
| lDDT-PLI | Protein-ligand interface confidence | `compute_lddt_pli(pred_prot, pred_lig, ...)` |

---

## Module 8 — Practical Problems

### 01_strings_dna, 02_dynamic_programming, 03_graphs_assembly, 04_statistics_ml_practical, 05_alignment_phylogeny ⭐⭐-⭐⭐⭐
**Goal**: Turn the theory modules into timed-practice problem solving

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| String manipulation | Interview-style DNA/RNA sequence tasks | Sliding windows, parsing, transforms |
| Dynamic programming | Recurrence relations and alignment tables | Iterative DP solutions |
| Graphs and assembly | BFS/DFS/Dijkstra + De Bruijn ideas | Graph traversal helpers |
| Statistics and ML practice | Probability, regression, quick diagnostics | Compact notebook solutions |
| Alignment and phylogeny | Integrated bioinformatics capstone drills | Multi-step combined solutions |

---

## Module 9 — ML Teaching Essentials

### 01_model_diagnostics ⭐⭐⭐
**Goal**: Diagnose model behavior instead of training blindly

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Bias-variance | Underfitting vs overfitting regimes | Complexity sweeps + plots |
| Learning curves | Data size vs train/validation performance | `learning_curve(...)` |
| Regularization | L1/L2/ElasticNet tradeoffs | Path visualizations |
| Feature importance | Gini vs permutation importance | Importance comparison code |
| Optimization debugging | LR schedules, gradient flow, early stopping | Training diagnostics utilities |
| Failure pattern recognition | Common ML debugging signatures | Multi-panel diagnostic plots |

---

## Module 10 — Fine-Tuning Protein Structure Models

### 01_protein_structure_finetuning ⭐⭐⭐⭐
**Goal**: Fine-tune Pairformer-style protein models efficiently

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Pairformer stack | Triangle ops + pair transitions in sequence | `PairformerStack` |
| LoRA injection | Low-rank adapters for Q/K/V projections | `inject_lora()`, `merge_lora()` |
| Differential learning rates | Stable adaptation of large pretrained backbones | Multi-group optimizer config |
| Task head design | Mutation-focused pooling and regression | `MutationPredictor` |
| Schedules | Warmup + cosine decay from scratch | `get_lr(step, ...)` |
| Checkpointing | Adapter-only checkpoints for lightweight reuse | Save/load LoRA weights |

---

## Module 11 — Membrane Protein Dynamics

### 01_membrane_protein_dynamics ⭐⭐⭐⭐
**Goal**: Apply modern ML ideas to membrane protein biology

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| TM topology | Sequence patterns and topology prediction | Membrane-sequence features |
| Membrane-specific fine-tuning | ESM2 + LoRA adaptation for TM proteins | `MembraneProteinFineTuner` |
| Conformational VAEs | Latent-variable modeling of structural states | VAE encoder/decoder pieces |
| GPCR screening | Binding-score style downstream prediction | Screening pipeline components |
| Coarse-grained MD | Simplified simulation setup concepts | MARTINI-oriented workflow sketches |

---

## Module 12 — Generative Models

### 01_diffusion_protein_design ⭐⭐⭐⭐
**Goal**: Understand diffusion modeling in the protein-design context

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Forward diffusion | Adding noise according to a schedule | `q_sample(x0, t, noise)` |
| Reverse process | Denoising-based generation | `predict_noise(x_t, t)` |
| Noise schedules | Linear, cosine, log-normal intuition | Schedule comparison code |
| Structure generation link | Why diffusion suits 3D biological objects | Protein-design demos |
| Training objective | Noise prediction vs score matching intuition | Loss implementations |

---

## Module 13 — Bayesian Methods

### 01_bayesian_ml_uncertainty ⭐⭐⭐
**Goal**: Reason about uncertainty in ML predictions and decisions

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Bayes rule | Prior × likelihood → posterior | Conjugate posterior updates |
| Credible intervals | Distribution-aware uncertainty summaries | Posterior interval code |
| MCMC | Approximate sampling from difficult posteriors | Metropolis-Hastings style sampler |
| Posterior predictive | Uncertainty on future observations | Predictive sampling |
| Decision under uncertainty | When calibrated confidence changes action | Risk-aware toy analyses |

---

## Module 14 — Reinforcement Learning

### 01_rl_protein_design ⭐⭐⭐⭐
**Goal**: Apply reinforcement learning ideas to protein design and search

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| MDP setup | States, actions, rewards, transitions for sequence optimization | Environment framing utilities |
| Q-learning / DQN | Value-based RL for discrete sequence edits | `DQNNetwork` |
| REINFORCE | Monte Carlo policy-gradient updates | `PolicyNetwork` |
| PPO | Stable clipped policy optimization | `ActorCritic` |
| GFlowNets | RL-inspired flow matching for diverse high-reward generation | GFlowNet-style trajectory logic |
| Multi-objective design | Balancing stability, binding, and novelty rewards | Reward-combination demos |

---

## Module 15 — Self-Supervised Learning

### 01_contrastive_ssl ⭐⭐⭐⭐
**Goal**: Learn how protein foundation-model pretraining works before supervised fine-tuning

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Masked language modeling | BERT-style token masking for protein sequences | Protein masking utilities |
| Protein transformers | Sequence encoders in the ESM2 style | `ProteinTransformer`-style blocks |
| SimCLR | Contrastive learning with augmentations + NT-Xent loss | Contrastive loss/training loop |
| BYOL | Non-contrastive bootstrap learning with EMA target network | BYOL-style update logic |
| Representation transfer | Linear probes and downstream fine-tuning | Small downstream evaluation heads |
| Foundation-model connection | Why SSL scales in proteins with unlabeled sequence corpora | ESM2-oriented demos |

---

## Module 16 — MLOps & Deployment

### 01_mlops_for_protein_ml ⭐⭐⭐
**Goal**: Learn how to ship and monitor protein ML systems, not just train them

| Topic | Concept | Code You Write |
|-------|---------|---------------|
| Experiment tracking | Metrics, params, artifacts, model registry | MLflow-style logging helpers |
| Reproducibility | Seeds, config snapshots, data checksums | Config + checkpoint metadata |
| Serving | REST inference patterns for trained models | FastAPI-style service skeletons |
| Containers | Packaging models and dependencies for deployment | Docker-oriented examples |
| Drift detection | Detecting feature or distribution shifts in production | Statistical drift checks |
| CI/CD | Automated tests and regression checks for ML changes | Pipeline validation logic |

---

## Interview Question Coverage

### Python / Algorithms
- Edit distance time/space complexity
- Generator vs list for FASTA parsing
- De Bruijn graph for assembly
- Dynamic programming memoization patterns

### ML Fundamentals
- Data leakage: causes, detection, prevention
- ROC-AUC vs PR-AUC: when to use each
- Bias-variance tradeoff in protein ML context
- Handling class imbalance (5+ methods)
- Cross-validation variants: stratified, grouped, leave-one-out

### Structural Biology ML
- RMSD vs TM-score: when each is insufficient
- Why represent proteins as graphs (not sequences)
- SE(3) invariance vs equivariance distinction
- Evoformer vs Pairformer architectural difference
- When to use ESMFold vs AlphaFold 2 vs AlphaFold 3

### Deep Learning / Fine-Tuning
- Catastrophic forgetting: causes and prevention
- LoRA: rank parameter, when it beats full fine-tuning
- Differential learning rates: which layers need which LR
- Gradient checkpointing: memory/speed tradeoff

### AlphaFold 3 (Expert Level)
- FAPE vs RMSD: why FAPE is better for training
- Triangle attention: O(N³) compute, how chunking helps
- Why diffusion replaces the structure module
- CCD vs SMILES: what extra information CCD provides
- lDDT-PLI vs lDDT: what the PLI variant specifically captures
