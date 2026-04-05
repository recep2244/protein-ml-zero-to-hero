# Glossary — Bioinformatics & Structural Biology ML

> **How to use this glossary:** If you encounter a term you don't know in a notebook, look it up here first. Each entry gives you a plain English explanation, the technical definition, and where in the curriculum to find it in action.

---

## Biology & Bioinformatics

**Amino acid**
*Plain English:* The building blocks of proteins — there are 20 standard ones.
*Technical:* Organic molecules with a central carbon, an amino group (-NH₂), a carboxyl group (-COOH), and a side chain (R group) that determines chemical properties.
*Curriculum:* Module 01 (sequence encoding), Module 07 (embedding)

**Protein**
*Plain English:* A chain of amino acids that folds into a 3D shape to do a job.
*Technical:* A polypeptide chain (primary structure) that forms α-helices and β-sheets (secondary structure), then folds into a 3D tertiary structure. Function depends on 3D shape.
*Curriculum:* Module 03 (structure), Module 07 (prediction)

**DNA / RNA**
*Plain English:* DNA stores the genetic blueprint; RNA carries instructions from DNA to make proteins.
*Technical:* DNA = double-stranded deoxyribonucleic acid (A,T,C,G bases). RNA = single-stranded ribonucleic acid (A,U,C,G bases). Transcription: DNA→RNA. Translation: RNA→protein.
*Curriculum:* Module 02 (genomics)

**Codon**
*Plain English:* A 3-letter RNA code that specifies one amino acid.
*Technical:* A triplet of nucleotides (e.g., AUG = methionine / start codon). 64 codons encode 20 amino acids + 3 stop codons.
*Curriculum:* Module 02/01 (codon tables, ORF finding)

**ORF (Open Reading Frame)**
*Plain English:* A section of DNA that could encode a protein — starts with ATG, ends with a stop codon.
*Technical:* A continuous stretch of codons from a start codon (ATG) to a stop codon (TAA/TAG/TGA), on any of the 6 reading frames (3 per strand).
*Curriculum:* Module 02/01

**FASTA format**
*Plain English:* A simple text file format for storing DNA/protein sequences.
*Technical:* Lines starting with `>` are headers (sequence name/description); following lines are the sequence. Used universally in bioinformatics.
*Curriculum:* Module 01/01, Module 17/00

**PDB (Protein Data Bank)**
*Plain English:* The world's archive of protein 3D structures, like a library of molecular models.
*Technical:* Repository of experimentally determined 3D structures from X-ray crystallography, NMR, cryo-EM. PDB format stores ATOM records with x,y,z coordinates per atom.
*Curriculum:* Module 03/01

**RMSD (Root Mean Square Deviation)**
*Plain English:* A number measuring how similar two protein shapes are — lower is more similar.
*Technical:* RMSD = sqrt(1/N × Σ |rᵢ - r'ᵢ|²) for N atom pairs after optimal alignment. Units: Ångströms. < 2Å = very similar; > 5Å = quite different.
*Curriculum:* Module 03/01

**TM-score**
*Plain English:* A better version of RMSD for comparing protein structures — not sensitive to protein length.
*Technical:* TM-score ∈ (0,1]. > 0.5 = same fold; > 0.9 = very similar. Length-normalized, so 100-residue and 500-residue proteins can be compared fairly.
*Curriculum:* Module 03/01

**Multiple Sequence Alignment (MSA)**
*Plain English:* Lining up many related protein sequences to see which positions are conserved.
*Technical:* Algorithm that inserts gaps (-) to maximize matches across sequences. Used in AlphaFold to find co-evolutionary signals.
*Curriculum:* Module 01/04, Module 07/02

**BLOSUM62**
*Plain English:* A scoring table for how likely one amino acid is to be replaced by another during evolution.
*Technical:* Log-odds substitution matrix from blocks of alignments with ~62% identity. Entry (i,j) = log(observed/expected frequency of swapping amino acid i for j).
*Curriculum:* Module 01/02

**Sequence alignment (NW/SW)**
*Plain English:* Finding the best way to match two sequences, allowing gaps.
*Technical:* Needleman-Wunsch (global alignment, fills full grid) and Smith-Waterman (local alignment, allows negative values to reset). Both use dynamic programming.
*Curriculum:* Module 01/01

**ΔΔG (Delta Delta G)**
*Plain English:* How much a mutation changes a protein's stability — negative = stabilizing, positive = destabilizing.
*Technical:* ΔΔG = ΔG(mutant) − ΔG(wild-type), where ΔG = folding free energy. Measured in kcal/mol. Positive ΔΔG > 1 kcal/mol typically destabilizes folding.
*Curriculum:* Module 10/01

**pLDDT**
*Plain English:* AlphaFold's confidence score for each residue — 0 to 100, higher is more confident.
*Technical:* Predicted Local Distance Difference Test. Average over local Cα-Cα distances. > 90: very high confidence; 70-90: confident; 50-70: low confidence; < 50: unreliable.
*Curriculum:* Module 07/03, Module 17/00

**PAE (Predicted Aligned Error)**
*Plain English:* AlphaFold's confidence in the relative position of two residues — lower is more confident.
*Technical:* Predicted error (in Å) in residue j's position when the structure is aligned on residue i. Low off-diagonal PAE = confident about domain-domain interface.
*Curriculum:* Module 07/03, Module 17/00

**Homology**
*Plain English:* Two genes/proteins are homologs if they share a common ancestor.
*Technical:* Orthologs = same gene in different species (same function). Paralogs = duplicate within a genome (often different function). Sequence identity > 30% strongly suggests homology.
*Curriculum:* Module 01 (BLAST), Module 02

**Variant / SNP**
*Plain English:* A position in the genome where individuals differ. SNP = single base change.
*Technical:* Single Nucleotide Polymorphism: one DNA base differs from the reference. Variants in coding regions can change amino acids (missense), stop codons (nonsense), or be silent (synonymous).
*Curriculum:* Module 02/03

**Gene ontology (GO)**
*Plain English:* A standardized vocabulary for describing what genes and proteins do.
*Technical:* Structured vocabulary with three aspects: Biological Process, Molecular Function, Cellular Component. Used in pathway enrichment analysis.
*Curriculum:* Module 02/04

**MD simulation (Molecular Dynamics)**
*Plain English:* Simulating the motion of every atom in a protein over time, like watching a protein wiggle.
*Technical:* Numerically integrates Newton's equations of motion using a force field (equations describing atomic interactions). Time step ~2 femtoseconds. Generates conformational ensemble.
*Curriculum:* Module 11/02

---

## Machine Learning

**Gradient descent**
*Plain English:* The method models use to learn — take small steps downhill on the error surface.
*Technical:* Iteratively update parameters θ ← θ − η∇L(θ) where η is learning rate and ∇L is gradient of loss. Variants: SGD, Adam, AdamW.
*Curriculum:* Module 00/05, Module 05/01

**Overfitting**
*Plain English:* Model memorizes the training data instead of learning patterns — works perfectly on training data, fails on new data.
*Technical:* Training loss << validation loss. Caused by model complexity >> data complexity. Fixes: regularization, more data, dropout, early stopping.
*Curriculum:* Module 09/01

**Bias-variance tradeoff**
*Plain English:* Simple models make systematic errors (bias); complex models make erratic errors (variance). You need to balance both.
*Technical:* Total error = bias² + variance + irreducible noise. High bias = underfitting. High variance = overfitting. Sweet spot minimizes total.
*Curriculum:* Module 09/01

**Transformer**
*Plain English:* The neural network architecture behind GPT, BERT, and AlphaFold — processes sequences by having every element "attend" to every other.
*Technical:* Multi-head self-attention + FFN layers + residual connections. Attention: Q, K, V matrices where output = softmax(QKᵀ/√d)V. Parallelizable over sequence length.
*Curriculum:* Module 05/01, Module 07

**Attention mechanism**
*Plain English:* A way for a model to decide which parts of the input to focus on when processing each element.
*Technical:* Scaled dot-product attention: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V. Multi-head attention runs multiple attention heads in parallel and concatenates.
*Curriculum:* Module 05/01, Module 07/01

**LoRA (Low-Rank Adaptation)**
*Plain English:* A way to fine-tune a huge model cheaply by only training small "adapter" matrices.
*Technical:* Replace weight update ΔW (d×d) with AB where A (d×r) and B (r×d), r << d. Reduces trainable parameters from d² to 2dr. Original weights frozen.
*Curriculum:* Module 05/01, Module 10/01

**Dropout**
*Plain English:* Randomly turn off some neurons during training to prevent the network from relying too much on any one feature.
*Technical:* During training, each neuron is set to 0 with probability p (typically 0.1-0.5). At inference, multiply weights by (1-p). Regularizes the network.
*Curriculum:* Module 05/01, Module 13 (MC Dropout)

**Batch normalization**
*Plain English:* Normalize the activations in each layer to keep training stable.
*Technical:* For each mini-batch, normalize to zero mean, unit variance, then apply learned scale γ and shift β: x̂ = (x − μ_batch) / σ_batch; y = γx̂ + β.
*Curriculum:* Module 05/01

**Loss function**
*Plain English:* A number measuring how wrong the model's predictions are — lower is better.
*Technical:* Cross-entropy for classification, MSE for regression, FAPE for protein structure. The gradient of the loss guides parameter updates.
*Curriculum:* Module 00/05, Module 07/05

**Learning rate**
*Plain English:* How big a step to take when updating the model — too big = unstable, too small = slow.
*Technical:* η in θ ← θ − η∇L. Typical range 1e-5 to 1e-2. Warmup schedules start small and increase, then cosine decay back down.
*Curriculum:* Module 05/01, Module 07/05

**Early stopping**
*Plain English:* Stop training when the validation error stops improving — prevents wasting time and overfitting.
*Technical:* Monitor validation metric every N epochs. Stop when it hasn't improved for `patience` epochs. Save best checkpoint.
*Curriculum:* Module 05/01

---

## Deep Learning Architecture

**CNN (Convolutional Neural Network)**
*Plain English:* A neural network that scans across the input with a small "filter" — good at local patterns.
*Technical:* Convolutional layers learn local feature detectors via shared weight kernels. Pooling layers downsample. Used for sequences (1D conv) and images (2D conv).
*Curriculum:* Module 05/01

**RNN / LSTM**
*Plain English:* A neural network designed to process sequences one step at a time, remembering what came before.
*Technical:* LSTM: input, forget, output gates control what to remember/forget. BiLSTM runs in both directions, concatenates hidden states. Largely replaced by Transformers but still used.
*Curriculum:* Module 05/02

**GNN (Graph Neural Network)**
*Plain English:* A neural network that operates on graph-structured data — perfect for proteins (atoms = nodes, bonds = edges).
*Technical:* Message passing: each node aggregates features from neighbors, updates its state. Equivariant GNNs respect 3D rotations/translations (critical for proteins).
*Curriculum:* Module 06/01

**Equivariance / Invariance**
*Plain English:* A model is equivariant if rotating the input rotates the output the same way. Invariant if rotation doesn't change output at all. Proteins need equivariant models.
*Technical:* Equivariant: f(Rx) = Rf(x). Invariant: f(Rx) = f(x). SE(3)-equivariant models handle 3D rotations + translations.
*Curriculum:* Module 06/01

**Diffusion model**
*Plain English:* A generative model that learns to undo noise — you start with random noise and gradually denoise it into a sample.
*Technical:* Forward process: add Gaussian noise over T steps. Reverse process: train a neural network to predict noise (DDPM) or score (DDIM). Used in RFdiffusion, AlphaFold3.
*Curriculum:* Module 12/01

**DDPM (Denoising Diffusion Probabilistic Model)**
*Plain English:* The most common type of diffusion model — trains a network to remove noise.
*Technical:* Forward: xₜ = √ᾱₜ x₀ + √(1-ᾱₜ) ε, ε ~ N(0,I). Reverse: p_θ(xₜ₋₁|xₜ) learned by a noise predictor. Loss: ||ε - ε_θ(xₜ, t)||².
*Curriculum:* Module 12/01

---

## Advanced ML & Structural Biology

**Pairformer (AlphaFold3)**
*Plain English:* The core neural network in AlphaFold3 — processes both single-residue features and pairwise residue-residue features simultaneously.
*Technical:* Operates on MSA representation (N_seq × N_res × c_m) and pair representation (N_res × N_res × c_z). Triangle attention + outer product mean update per layer.
*Curriculum:* Module 07/01

**Triangle attention**
*Plain English:* A special attention mechanism that enforces the triangle inequality in protein distance geometry.
*Technical:* Updates pair features (i,j) by attending over pairs (i,k) or (k,j), giving each pair information about "what is between them". Two variants: starting node and ending node.
*Curriculum:* Module 07/01

**FAPE loss**
*Plain English:* AlphaFold3's way of measuring structural error — checks atom positions from every residue's own reference frame.
*Technical:* Frame Aligned Point Error: FAPE = 1/(N_frames × N_atoms) × Σ_{t,i} ||Tₜ⁻¹ x̂ᵢ − Tₜ⁻¹ xᵢ||. Clamped at 10Å to prevent outlier explosion.
*Curriculum:* Module 07/05

**ESM-2 (Evolutionary Scale Modeling)**
*Plain English:* A protein language model trained on 250M sequences — like GPT but for proteins.
*Technical:* BERT-style Transformer trained with masked language modelling on UniRef50. Produces per-residue embeddings that encode evolutionary and structural information without alignment.
*Curriculum:* Module 15/01

**MC Dropout (Monte Carlo Dropout)**
*Plain English:* A Bayesian trick: run the model many times with dropout ON at test time to get a distribution of predictions.
*Technical:* At inference, keep dropout active. Run forward pass N times. Variance of predictions = epistemic uncertainty (model uncertainty). Mean = prediction.
*Curriculum:* Module 13/01

**GFlowNet**
*Plain English:* A generative model that learns to sample diverse solutions proportional to a reward — not just the single best solution.
*Technical:* Learns a policy that generates objects (molecules, sequences) with probability proportional to R(x). Balances exploration and exploitation. Used in drug discovery.
*Curriculum:* Module 14/01

**SimCLR / BYOL**
*Plain English:* Self-supervised learning methods — train on unlabeled data by learning that different views of the same sample should have similar representations.
*Technical:* SimCLR: maximize agreement between augmented views via contrastive loss. BYOL: no negatives — online network predicts target network's representation. Used to pretrain ESM-2-style protein encoders.
*Curriculum:* Module 15/01

**Backbone frame**
*Plain English:* The local coordinate system defined by a residue's N-Cα-C atoms.
*Technical:* A Rigid body (rotation R ∈ SO(3), translation t ∈ ℝ³) defining a local frame. AlphaFold3 predicts all backbone frames, then places side chains within each frame.
*Curriculum:* Module 10/00

**BF16 (BFloat16)**
*Plain English:* A way to store numbers using less memory — 2 bytes instead of 4 — keeping the same range but less precision.
*Technical:* 1 sign bit, 8 exponent bits, 7 mantissa bits. Same dynamic range as FP32 (8 exponent bits), less precision than FP32 (23 mantissa bits). Supported on A100/H100 but not T4.
*Curriculum:* Module 07/05, CLOUD_SETUP.md

---

## Tools & Frameworks

**PyTorch**
*Plain English:* The main Python library for building neural networks — used throughout this curriculum.
*Curriculum:* Module 05 onward

**Biopython**
*Plain English:* Python library for parsing biology file formats (FASTA, PDB, GenBank).
*Curriculum:* Module 01, 02, 03

**scikit-learn**
*Plain English:* Python library for classical ML algorithms (random forests, SVM, PCA, cross-validation).
*Curriculum:* Module 00/05, Module 04

**MLflow**
*Plain English:* Tool for tracking ML experiments — log metrics, parameters, and model checkpoints.
*Curriculum:* Module 16/01

**FastAPI**
*Plain English:* Python library for building REST APIs — used to deploy ML models as web services.
*Curriculum:* Module 16/01

---

*This glossary covers ~55 terms. If you encounter a term not listed here, search the notebooks directly or ask in the CONTRIBUTING.md discussion channels.*
