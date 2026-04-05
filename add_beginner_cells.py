"""
add_beginner_cells.py

Performs three tasks:
  Task 1 — Insert domain-specific "Concepts for Beginners" glossary cell after the
            TL;DR / first markdown cell in 11 specified notebooks.
  Task 2 — Append "Common Errors & Troubleshooting" markdown cell before the last
            cell in 9 specified notebooks.
  Task 3 — Append "Notebook Complete" summary markdown cell to every notebook that
            does not already have one (checked by presence of "you can now",
            "notebook complete", or "✅" in the full source text).

All notebooks are modified in-place. nbformat 4.5, 8-char hex cell IDs are preserved.
"""

import json
import os
import random
import string
import glob

BASE = "/home/recep/Desktop/Machine_Learning/projects/hackerrank"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def new_id():
    """Generate a random 8-character lowercase hex cell ID."""
    return "".join(random.choices("0123456789abcdef", k=8))


def make_markdown_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": new_id(),
        "metadata": {},
        "source": source,
    }


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(path: str, nb: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")


def full_source(nb: dict) -> str:
    return " ".join("".join(c["source"]) for c in nb["cells"]).lower()


# ---------------------------------------------------------------------------
# Task 1 — Glossary data
# ---------------------------------------------------------------------------

GLOSSARY_CELLS = {
    "02_genomics_gene_analysis/01_genomics_core.ipynb": (
        "## Genomics — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **Genome** | The complete DNA instruction set of an organism — all chromosomes combined |\n"
        "| **Gene** | A segment of DNA that encodes one protein — like one recipe in a cookbook |\n"
        "| **Codon** | 3 DNA letters that specify one amino acid (e.g. ATG = start; TAA/TAG/TGA = stop) |\n"
        "| **ORF (Open Reading Frame)** | DNA stretch starting at ATG and ending at a stop codon — a candidate gene |\n"
        "| **Transcript** | RNA copy made from a gene — the message that gets translated into protein |\n"
        "| **mRNA** | Messenger RNA: the processed transcript that ribosomes read to build protein |\n"
        "| **FASTA format** | Standard text format for sequences: `>sequence_name` header line, then the sequence |\n"
        "| **GFF/GTF** | Annotation file formats that map gene locations onto a genome (chromosome, start, end, strand) |\n"
        "| **Variant** | A position in the genome that differs between individuals (SNP, insertion, deletion) |\n"
        "| **SNP** | Single Nucleotide Polymorphism — a one-letter DNA difference between individuals |\n"
        "| **Pathway** | A set of genes that work together to perform a biological function (e.g. glycolysis) |\n"
        "| **Differential expression** | A gene is differentially expressed if it's significantly more/less active in condition A vs B |"
    ),
    "02_genomics_gene_analysis/02_rnaseq_analysis.ipynb": (
        "## RNA-seq — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **RNA-seq** | Sequencing all RNA in a sample to measure which genes are active and how much |\n"
        "| **read count** | How many sequencing reads mapped to a gene — proxy for gene activity level |\n"
        "| **normalization** | Adjusting counts to remove technical biases (library size, gene length) so samples are comparable |\n"
        "| **TPM / FPKM** | Normalized expression units that correct for sequencing depth and gene length |\n"
        "| **DEG (Differentially Expressed Gene)** | A gene with significantly different expression between two conditions |\n"
        "| **p-value** | Probability the difference is due to chance; p < 0.05 is the conventional threshold |\n"
        "| **FDR / q-value** | False Discovery Rate correction — adjusts p-values when testing thousands of genes simultaneously |\n"
        "| **fold change** | Ratio of expression between conditions; log2(FC)=1 means 2x higher in condition B |\n"
        "| **volcano plot** | Scatter plot with log2(FC) on x-axis and -log10(p-value) on y-axis — highlights significant DEGs |\n"
        "| **PCA** | Dimensionality reduction that reveals which samples cluster together |\n"
        "| **heatmap** | Grid showing expression levels across genes (rows) and samples (columns) — reveals patterns |\n"
        "| **STAR / HISAT2** | Read alignment tools that map short RNA-seq reads back to the reference genome |"
    ),
    "02_genomics_gene_analysis/03_variant_analysis.ipynb": (
        "## Variant Analysis — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **VCF file** | Variant Call Format — standard text file listing all detected DNA variants with quality scores |\n"
        "| **CHROM/POS/REF/ALT** | VCF columns: chromosome, position, reference base, alternate (variant) base |\n"
        "| **QUAL score** | Confidence that a variant is real (not a sequencing error) — higher = more confident |\n"
        "| **FILTER field** | PASS = variant passed all quality filters; anything else = flag to investigate |\n"
        "| **INFO field** | Additional annotations: allele frequency, functional impact, dbSNP ID, etc. |\n"
        "| **allele frequency** | How common a variant is in the population (0.0 = rare, 1.0 = present in everyone) |\n"
        "| **germline variant** | Inherited DNA change present in every cell of the body |\n"
        "| **somatic variant** | DNA change that arose in one cell (e.g. cancer mutation) — not inherited |\n"
        "| **dbSNP** | NCBI database of known human SNPs — rs IDs (e.g. rs12345) refer to this database |\n"
        "| **synonymous** | Variant that changes the DNA codon but produces the same amino acid — \"silent\" |\n"
        "| **missense** | Variant that changes the codon to encode a DIFFERENT amino acid — may affect function |\n"
        "| **nonsense** | Variant that creates a premature stop codon — truncates the protein |"
    ),
    "02_genomics_gene_analysis/04_pathway_enrichment.ipynb": (
        "## Pathway Enrichment — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **pathway** | A set of genes/proteins that work together for a specific biological process |\n"
        "| **GO term** | Gene Ontology term — a standardised label describing a gene's function (e.g. GO:0006915 = apoptosis) |\n"
        "| **enrichment** | A pathway is enriched if more of your DEGs belong to it than expected by chance |\n"
        "| **Fisher's exact test** | Statistical test asking: \"Is the overlap between my gene list and this pathway surprising?\" |\n"
        "| **hypergeometric test** | Same idea as Fisher's but phrased as drawing balls from an urn — equivalent result |\n"
        "| **background gene set** | All genes measured in your experiment — the universe from which your DEGs came |\n"
        "| **GSEA** | Gene Set Enrichment Analysis — ranks ALL genes by fold-change and finds enriched pathways at the top/bottom |\n"
        "| **KEGG** | Kyoto Encyclopedia of Genes and Genomes — database of metabolic and signalling pathways |\n"
        "| **Reactome** | Another pathway database with more detailed biochemical pathway maps |\n"
        "| **adjusted p-value** | FDR-corrected p-value — essential when testing hundreds of pathways simultaneously |\n"
        "| **NES (Normalized Enrichment Score)** | GSEA score: positive = pathway genes are at the top of the ranked list (upregulated) |\n"
        "| **leading edge** | The subset of pathway genes most responsible for the enrichment signal in GSEA |"
    ),
    "03_protein_structural_biology/01_structure_analysis.ipynb": (
        "## Protein Structure — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **PDB (Protein Data Bank)** | World database of experimentally determined 3D protein structures — free at rcsb.org |\n"
        "| **PDB ID** | 4-character code for a structure (e.g. 1TIM) — like an ISBN for a protein structure |\n"
        "| **atom coordinates** | X, Y, Z positions of each atom in Angstroms (1A = 0.1 nanometre) |\n"
        "| **residue** | One amino acid in the protein chain — the repeating unit of the polymer |\n"
        "| **chain** | One continuous polypeptide strand in a structure; multi-chain structures have A, B, C... |\n"
        "| **Calpha (C-alpha)** | The central carbon of each amino acid backbone — simplest single-point residue representation |\n"
        "| **RMSD** | Root Mean Square Deviation — average distance between equivalent atoms in two structures; 0 = identical |\n"
        "| **B-factor** | Temperature factor — measures how much an atom moves/vibrates; high B = flexible/uncertain |\n"
        "| **secondary structure** | Local patterns: alpha-helix (coiled), beta-sheet (flat), or loop/coil (irregular) |\n"
        "| **TM-score** | Template Modelling score (0-1): >0.5 = same fold, >0.7 = very similar, 1.0 = identical |\n"
        "| **Kabsch algorithm** | Optimal rotation that minimises RMSD between two sets of coordinates |\n"
        "| **cryo-EM** | Electron microscopy method for solving structures of large complexes without crystals |"
    ),
    "03_protein_structural_biology/02_structure_quality_and_features.ipynb": (
        "## Structure Quality — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **Ramachandran plot** | Map of backbone angles (phi, psi) for every residue — most residues should fall in allowed regions |\n"
        "| **phi (phi) angle** | Rotation angle around the N-Calpha bond of a residue backbone |\n"
        "| **psi (psi) angle** | Rotation angle around the Calpha-C bond of a residue backbone |\n"
        "| **allowed region** | phi/psi combination that is sterically possible — outside is a steric clash |\n"
        "| **DSSP** | Algorithm that assigns secondary structure (H=helix, E=sheet, C=coil) from 3D coordinates |\n"
        "| **contact map** | 2D binary matrix: cell (i,j)=1 if residues i and j are within a distance threshold |\n"
        "| **pLDDT** | AlphaFold's per-residue confidence score (0-100); >90 = highly confident, <50 = disordered |\n"
        "| **resolution** | Quality metric for crystal structures in Angstroms; <2.0A = excellent, >3.5A = low resolution |\n"
        "| **R-factor** | How well the model explains the diffraction data; <0.25 is acceptable |\n"
        "| **MolProbity** | Web tool that scores structure quality (clashscore, Ramachandran outliers, rotamer outliers) |\n"
        "| **rotamer** | One of the allowed side-chain conformations for a given amino acid |\n"
        "| **B-factor normalisation** | Scaling B-factors to mean=0, std=1 to compare across structures with different overall flexibility |"
    ),
    "04_ml_bioinformatics/01_ml_for_omics.ipynb": (
        "## ML for Omics — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **omics** | Any large-scale molecular measurement: genomics (DNA), transcriptomics (RNA), proteomics (proteins) |\n"
        "| **p >> n problem** | More features (genes) than samples — classical ML breaks down; needs regularisation |\n"
        "| **high-dimensional data** | Data with thousands of features (genes) — visualisation and ML need special treatment |\n"
        "| **PCA (Principal Component Analysis)** | Rotates data to find the directions of maximum variance — reduces thousands of genes to 2-3 axes |\n"
        "| **explained variance** | What fraction of total variance each principal component captures |\n"
        "| **regularisation (L1/L2)** | Penalty on large weights — L1 (Lasso) does feature selection, L2 (Ridge) shrinks all weights |\n"
        "| **cross-validation** | Repeatedly split data into train/test folds to get reliable performance estimate |\n"
        "| **random forest** | Ensemble of decision trees that vote on predictions — handles high-dimensional data well |\n"
        "| **feature importance** | Score telling which genes contribute most to the model's predictions |\n"
        "| **batch effect** | Technical variation between samples processed at different times or labs — must be corrected |\n"
        "| **UMAP** | Non-linear dimensionality reduction for visualisation — better than PCA at showing clusters |\n"
        "| **survival analysis** | Statistical method for time-to-event data (e.g. time to cancer recurrence) |"
    ),
    "06_structural_ml_gnns/01_structure_ml.ipynb": (
        "## Structural ML & GNNs — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **graph** | A set of nodes (things) connected by edges (relationships) — proteins modelled as residue graphs |\n"
        "| **node** | A single entity in a graph (e.g. one amino acid residue) |\n"
        "| **edge** | A connection between two nodes (e.g. residues within 8A of each other) |\n"
        "| **node feature** | A vector of numbers describing one node (e.g. amino acid one-hot + physicochemical properties) |\n"
        "| **edge feature** | A vector describing one edge (e.g. distance, angle between residues) |\n"
        "| **message passing** | GNN core operation: each node collects information from its neighbours and updates its representation |\n"
        "| **aggregation** | How messages from neighbours are combined — sum, mean, or max |\n"
        "| **GCN** | Graph Convolutional Network — simplest GNN; averages neighbour features with learnable weights |\n"
        "| **equivariance** | A model is SE(3)-equivariant if rotating the input rotates the output by the same amount |\n"
        "| **invariance** | Output doesn't change when input is rotated/translated — what you want for scalar predictions (e.g. energy) |\n"
        "| **k-NN graph** | Graph where each node is connected to its k nearest neighbours in 3D space |\n"
        "| **contact threshold** | Distance cutoff (e.g. 8A between Calpha atoms) used to define which residues are \"in contact\" |"
    ),
    "06_structural_ml_gnns/02_gnn_deep_dive.ipynb": (
        "## GNN Deep Dive — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **MPNN (Message Passing Neural Network)** | General GNN framework: message -> aggregate -> update — most GNNs are special cases |\n"
        "| **readout** | Global pooling that converts node-level representations to a graph-level representation |\n"
        "| **graph-level prediction** | Single output for the whole graph (e.g. protein stability) — needs readout |\n"
        "| **node-level prediction** | Output per node (e.g. per-residue pLDDT) — no readout needed |\n"
        "| **over-smoothing** | Problem with deep GNNs: all node representations converge to the same vector after many layers |\n"
        "| **SE(3)-equivariant GNN** | GNN whose outputs transform correctly under 3D rotations and translations |\n"
        "| **EGNN** | Equivariant GNN that updates both node features AND 3D coordinates in each layer |\n"
        "| **SchNet** | GNN for molecules using radial basis functions to encode interatomic distances |\n"
        "| **DimeNet** | GNN that uses both distances AND angles — captures more geometric information |\n"
        "| **positional encoding** | Extra feature encoding a node's position in the graph (for sequential data like proteins) |\n"
        "| **batch normalisation** | Normalises layer inputs across a batch — stabilises training of deep GNNs |\n"
        "| **residual connection** | Skip connection: `output = layer(x) + x` — prevents vanishing gradients in deep networks |"
    ),
    "08_practical_problems/01_strings_dna.ipynb": (
        "## DNA Strings & Algorithms — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **string algorithm** | Algorithm that operates on sequences of characters — DNA is just a very long string |\n"
        "| **substring** | A contiguous part of a string — finding motifs is a substring search problem |\n"
        "| **complement** | Replace each base: A<->T, G<->C — the other strand of double-stranded DNA |\n"
        "| **reverse complement** | Reverse the complement — how the anti-parallel strand reads 5'->3' |\n"
        "| **Hamming distance** | Number of positions where two strings of equal length differ |\n"
        "| **edit distance** | Minimum insertions + deletions + substitutions to transform string A into B |\n"
        "| **k-mer** | A substring of length k — counting k-mers is a key technique in sequence analysis |\n"
        "| **frequency table** | Count of how often each substring/k-mer appears in a sequence |\n"
        "| **string hashing** | Convert a string to a number for fast lookup — Rabin-Karp uses this for pattern matching |\n"
        "| **trie** | Tree data structure for fast string prefix search — used in genome assembly |\n"
        "| **suffix array** | Sorted list of all suffixes of a string — enables O(log n) pattern search |\n"
        "| **BWT (Burrows-Wheeler Transform)** | String permutation that groups similar characters — base of most genome aligners |"
    ),
    "09_ml_teaching_essentials/01_model_diagnostics.ipynb": (
        "## Model Diagnostics — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **bias** | Systematic error — a biased model makes the same type of mistake consistently |\n"
        "| **variance** | Sensitivity to training data — high-variance model changes dramatically with different training sets |\n"
        "| **bias-variance tradeoff** | Simple models have high bias (underfit); complex models have high variance (overfit) |\n"
        "| **underfitting** | Model is too simple to capture the pattern — both training and validation error are high |\n"
        "| **overfitting** | Model memorises training data — low training error but high validation error |\n"
        "| **learning curve** | Plot of train/val error vs training set size — reveals whether you need more data or less complexity |\n"
        "| **validation curve** | Plot of train/val error vs hyperparameter — shows the underfitting->overfitting transition |\n"
        "| **calibration** | A model is calibrated if its confidence scores match actual frequencies (70% prediction -> 70% correct) |\n"
        "| **reliability diagram** | Plot of mean predicted probability vs actual fraction of positives — checks calibration |\n"
        "| **Platt scaling** | Fits a logistic regression on top of raw model outputs to improve calibration |\n"
        "| **temperature scaling** | Divides logits by a learnable temperature T before softmax — simplest calibration method |\n"
        "| **early stopping** | Stop training when validation loss stops improving — a form of implicit regularisation |"
    ),
    "11_membrane_protein_dynamics/01_membrane_protein_dynamics.ipynb": (
        "## Membrane Proteins — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **membrane protein** | Protein embedded in or spanning the cell membrane — ~30% of all proteins, >50% of drug targets |\n"
        "| **transmembrane (TM) helix** | Alpha-helix that spans the lipid bilayer — hydrophobic residues face the lipid core |\n"
        "| **lipid bilayer** | Double layer of phospholipid molecules forming cell membranes — hydrophilic heads out, hydrophobic tails in |\n"
        "| **GPCR** | G Protein-Coupled Receptor — largest family of membrane proteins; targets of ~34% of all drugs |\n"
        "| **topology** | Number and arrangement of TM helices; in-out vs out-in orientation relative to the cell |\n"
        "| **hydrophobicity** | How much a residue prefers non-polar (lipid) environment; TM helices are hydrophobic |\n"
        "| **MD simulation** | Molecular Dynamics: simulates atomic motion using Newton's laws of motion over nanoseconds-microseconds |\n"
        "| **force field** | Set of equations and parameters describing how atoms interact (CHARMM36m for membrane proteins) |\n"
        "| **conformational change** | Shift in 3D shape upon ligand binding, membrane voltage change, etc. — the basis of function |\n"
        "| **ion channel** | Membrane protein that lets ions (Na+, K+, Ca2+) pass through the membrane selectively |\n"
        "| **cryptic pocket** | Binding site that only opens up in certain conformations — invisible in static crystal structures |\n"
        "| **coarse-grained model** | Simplified model where multiple atoms are merged into one \"bead\" — enables longer simulations |"
    ),
    "13_bayesian_methods/01_bayesian_ml_uncertainty.ipynb": (
        "## Bayesian ML — Concepts for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **Bayesian inference** | Update beliefs with data: prior (what we knew before) x likelihood (what data says) -> posterior |\n"
        "| **prior** | Your probability distribution over parameters BEFORE seeing any data |\n"
        "| **likelihood** | Probability of observing the data given specific parameter values |\n"
        "| **posterior** | Updated probability distribution over parameters AFTER seeing the data |\n"
        "| **uncertainty quantification (UQ)** | Measuring how confident the model is in its predictions — essential for high-stakes decisions |\n"
        "| **aleatoric uncertainty** | Irreducible noise in the data itself (e.g. measurement error) — can't be reduced with more data |\n"
        "| **epistemic uncertainty** | Uncertainty due to lack of data — CAN be reduced by collecting more examples |\n"
        "| **MC Dropout** | Run inference N times with dropout active; spread of predictions = uncertainty estimate |\n"
        "| **conformal prediction** | Statistically rigorous method to build prediction intervals with guaranteed coverage |\n"
        "| **Gaussian Process (GP)** | Non-parametric model that gives a distribution over functions — exact uncertainty, expensive to scale |\n"
        "| **MCMC** | Markov Chain Monte Carlo — samples from the posterior when exact computation is intractable |\n"
        "| **acquisition function** | In Bayesian optimisation: function deciding which point to evaluate next (e.g. Expected Improvement) |"
    ),
    "17_capstone_project/00_end_to_end_pipeline.ipynb": (
        "## Capstone — Quick Reference for Beginners\n\n"
        "| Term | Plain English |\n"
        "|------|---------------|\n"
        "| **EGFR** | Epidermal Growth Factor Receptor — a kinase mutated in ~15% of lung cancers; targeted by erlotinib |\n"
        "| **kinase** | Enzyme that adds phosphate groups to other proteins — switches them on or off |\n"
        "| **L858R** | Most common EGFR activating mutation; leucine (L) at position 858 changed to arginine (R) |\n"
        "| **T790M** | EGFR resistance mutation — emerges after first-generation inhibitor treatment |\n"
        "| **ESM-2** | Meta's protein language model — converts amino acid sequence to rich embedding vectors |\n"
        "| **delta-delta-G (ddG)** | Free energy change of mutation: negative = stabilising, positive = destabilising |\n"
        "| **mutation scanning** | Test all 19 substitutions at every position — identifies hot-spot residues |\n"
        "| **conformal prediction** | Gives guaranteed-coverage prediction intervals (e.g. 95% CI on ddG) |\n"
        "| **Bayesian optimisation** | Efficient search strategy: model uncertainty -> pick most informative next experiment |\n"
        "| **pLDDT** | AlphaFold's confidence score per residue (0-100) — low = disordered or unreliable |\n"
        "| **FastAPI endpoint** | Web URL that accepts a mutation and returns a ddG prediction in real time |\n"
        "| **executive summary** | 200-word plain-English description of your findings written for a non-technical audience |"
    ),
}

# ---------------------------------------------------------------------------
# Task 2 — Common Errors cell
# ---------------------------------------------------------------------------

ERRORS_SOURCE = (
    "## Common Errors & Troubleshooting\n\n"
    "| Error | Cause | Fix |\n"
    "|-------|-------|-----|\n"
    "| `ModuleNotFoundError: No module named 'X'` | Package not installed | Run `!pip install X` in a cell, then restart kernel |\n"
    "| `CUDA out of memory` | GPU RAM exceeded | Reduce batch size, or add `torch.cuda.empty_cache()` |\n"
    "| `RuntimeError: Expected all tensors on same device` | Mixed CPU/GPU tensors | Add `.to(device)` after creating each tensor |\n"
    "| `ValueError: shapes not aligned` | Matrix dimension mismatch | Print `tensor.shape` before the operation to debug |\n"
    "| `KeyError` in DataFrame | Column name wrong or missing | Print `df.columns` to see exact column names |\n"
    "| `IndexError: index out of range` | Loop or slice exceeds sequence length | Print `len(sequence)` and check your index |\n"
    "| Kernel dies silently | Memory overflow (RAM) | Restart kernel, reduce data size, use generators |\n"
    "| `UserWarning: No GPU found` | CUDA not available | Add `device = 'cuda' if torch.cuda.is_available() else 'cpu'` |"
)

TASK2_NOTEBOOKS = [
    "01_sequence_analysis/01_alignment_algorithms.ipynb",
    "01_sequence_analysis/04_rosalind_alignment_advanced.ipynb",
    "01_sequence_analysis/07_hidden_markov_models.ipynb",
    "02_genomics_gene_analysis/04_pathway_enrichment.ipynb",
    "07_alphafold3_core/02_af3_data_pipeline.ipynb",
    "07_alphafold3_core/04_af3_fullscale_and_ccd.ipynb",
    "08_practical_problems/02_dynamic_programming.ipynb",
    "08_practical_problems/03_graphs_assembly.ipynb",
    "14_reinforcement_learning/01_rl_protein_design.ipynb",
]

# ---------------------------------------------------------------------------
# Task 3 — Completion cell data
# ---------------------------------------------------------------------------

# Map relative path -> (skill_bullets, prev_module, next_module)
COMPLETION_DATA = {
    # 00_python_ml_basics — 9 notebooks missing completion
    "00_python_ml_basics/02_ml_fundamentals.ipynb": (
        ["Build and evaluate classification and regression models with scikit-learn",
         "Explain bias-variance tradeoff and apply cross-validation correctly"],
        "01_python_core_for_bioinformatics",
        "03_hackerrank_all_modules",
    ),
    "00_python_ml_basics/03_hackerrank_all_modules.ipynb": (
        ["Solve HackerRank Python and statistics problems across all core tracks",
         "Recognise common problem patterns and apply the right algorithm quickly"],
        "02_ml_fundamentals",
        "04_hackerrank_python_track",
    ),
    "00_python_ml_basics/04_hackerrank_python_track.ipynb": (
        ["Implement Python solutions for HackerRank string, list, and dict challenges",
         "Write clean, idiomatic Python for competitive-style assessments"],
        "03_hackerrank_all_modules",
        "05_hackerrank_statistics_ml_tracks",
    ),
    "00_python_ml_basics/05_hackerrank_statistics_ml_tracks.ipynb": (
        ["Solve HackerRank statistics and ML track problems using NumPy and scipy",
         "Apply descriptive statistics, distributions, and hypothesis testing programmatically"],
        "04_hackerrank_python_track",
        "06_pytorch_fundamentals",
    ),
    "00_python_ml_basics/06_pytorch_fundamentals.ipynb": (
        ["Build, train, and evaluate neural networks with PyTorch from scratch",
         "Use autograd, optimisers, and DataLoaders correctly"],
        "05_hackerrank_statistics_ml_tracks",
        "07_tensorflow_keras",
    ),
    "00_python_ml_basics/07_tensorflow_keras.ipynb": (
        ["Build and train models using the Keras Sequential and Functional APIs",
         "Use callbacks, custom layers, and tf.data pipelines"],
        "06_pytorch_fundamentals",
        "08_mathematical_foundations",
    ),
    "00_python_ml_basics/08_mathematical_foundations.ipynb": (
        ["Apply linear algebra (matrix ops, SVD, eigendecomposition) relevant to ML",
         "Derive and implement gradient descent and backpropagation by hand"],
        "07_tensorflow_keras",
        "09_classical_ml_advanced",
    ),
    "00_python_ml_basics/09_classical_ml_advanced.ipynb": (
        ["Implement and tune SVMs, gradient boosting, and ensemble methods",
         "Apply feature engineering and preprocessing pipelines with scikit-learn"],
        "08_mathematical_foundations",
        "10_how_to_read_a_paper",
    ),
    "00_python_ml_basics/10_how_to_read_a_paper.ipynb": (
        ["Navigate a machine learning paper (abstract, methods, results, limitations)",
         "Identify key contributions and reproduce core experiments from pseudocode"],
        "09_classical_ml_advanced",
        "01_sequence_analysis/01_alignment_algorithms — Module 01",
    ),
    # 01_sequence_analysis — all 7 missing
    "01_sequence_analysis/01_alignment_algorithms.ipynb": (
        ["Implement Needleman-Wunsch global and Smith-Waterman local alignment from scratch",
         "Trace back optimal alignments and interpret scoring matrices"],
        "00_python_ml_basics",
        "02_rosalind_complete",
    ),
    "01_sequence_analysis/02_rosalind_complete.ipynb": (
        ["Solve the core set of Rosalind bioinformatics problems programmatically",
         "Apply string algorithms, combinatorics, and probability to biological sequences"],
        "01_alignment_algorithms",
        "03_rosalind_combinatorics_strings",
    ),
    "01_sequence_analysis/03_rosalind_combinatorics_strings.ipynb": (
        ["Solve Rosalind combinatorics and string-algorithm problems",
         "Implement k-mer counting, motif finding, and string sorting algorithms"],
        "02_rosalind_complete",
        "04_rosalind_alignment_advanced",
    ),
    "01_sequence_analysis/04_rosalind_alignment_advanced.ipynb": (
        ["Implement affine gap penalties and semi-global alignment variants",
         "Apply edit distance and alignment techniques to protein sequences"],
        "03_rosalind_combinatorics_strings",
        "05_rosalind_phylogeny",
    ),
    "01_sequence_analysis/05_rosalind_phylogeny.ipynb": (
        ["Build and interpret phylogenetic trees using parsimony and distance methods",
         "Apply UPGMA and Neighbour Joining algorithms to sequence data"],
        "04_rosalind_alignment_advanced",
        "06_rosalind_assembly_massspec",
    ),
    "01_sequence_analysis/06_rosalind_assembly_massspec.ipynb": (
        ["Model genome assembly as a graph problem and find Eulerian paths",
         "Interpret mass spectrometry peptide spectra for protein sequencing"],
        "05_rosalind_phylogeny",
        "07_hidden_markov_models",
    ),
    "01_sequence_analysis/07_hidden_markov_models.ipynb": (
        ["Implement the Viterbi algorithm and Forward-Backward algorithm for HMMs",
         "Apply HMMs to gene finding, CpG island detection, and profile HMMs"],
        "06_rosalind_assembly_massspec",
        "02_genomics_gene_analysis/01_genomics_core — Module 02",
    ),
    # 02_genomics — only 01 missing (02-04 already have completion)
    "02_genomics_gene_analysis/01_genomics_core.ipynb": (
        ["Parse FASTA files, translate codons, and find ORFs across all 6 reading frames",
         "Represent SNPs and indels and compute Jukes-Cantor evolutionary distance"],
        "01_sequence_analysis",
        "02_rnaseq_analysis",
    ),
    "02_genomics_gene_analysis/05_single_cell_rnaseq.ipynb": (
        ["Process single-cell RNA-seq data: quality control, normalisation, and clustering",
         "Visualise cell populations with UMAP and identify marker genes per cluster"],
        "04_pathway_enrichment",
        "03_protein_structural_biology/01_structure_analysis — Module 03",
    ),
    # 03_protein_structural_biology
    "03_protein_structural_biology/01_structure_analysis.ipynb": (
        ["Parse PDB files with BioPython and extract residue-level 3D coordinates",
         "Compute RMSD between structures and apply the Kabsch alignment algorithm"],
        "02_genomics_gene_analysis",
        "02_structure_quality_and_features",
    ),
    "03_protein_structural_biology/02_structure_quality_and_features.ipynb": (
        ["Compute Ramachandran angles, secondary structure labels, and contact maps",
         "Normalise B-factors and interpret pLDDT confidence scores"],
        "01_structure_analysis",
        "04_ml_bioinformatics/01_ml_for_omics — Module 04",
    ),
    # 05_deep_learning
    "05_deep_learning_finetuning/01_dl_and_finetuning.ipynb": (
        ["Implement CNNs, Transformers, and LoRA fine-tuning with PyTorch",
         "Apply EarlyStopping and monitor gradient flow during training"],
        "04_ml_bioinformatics",
        "02_sequence_models_rnn_lstm",
    ),
    # 06_structural_ml_gnns
    "06_structural_ml_gnns/01_structure_ml.ipynb": (
        ["Represent proteins as graphs and build protein contact graphs from PDB coordinates",
         "Train a GCN to predict residue-level or graph-level properties"],
        "05_deep_learning_finetuning",
        "02_gnn_deep_dive",
    ),
    "06_structural_ml_gnns/02_gnn_deep_dive.ipynb": (
        ["Implement message passing, aggregation, and readout layers from scratch",
         "Understand SE(3)-equivariance and why it matters for 3D molecular models"],
        "01_structure_ml",
        "07_alphafold3_core/00_af3_zero_to_hero — Module 07",
    ),
    # 07_alphafold3_core — only 06 missing
    "07_alphafold3_core/06_af3_diffusion_deep_dive.ipynb": (
        ["Implement the AlphaFold3 diffusion head: noise schedule, denoising network, and sampling",
         "Explain the role of the conditioner trunk and how conditioning embeddings steer diffusion"],
        "05_af3_training_loop",
        "08_practical_problems/01_strings_dna — Module 08",
    ),
    # 08_practical_problems — all 6 missing
    "08_practical_problems/01_strings_dna.ipynb": (
        ["Solve DNA string manipulation and pattern matching problems efficiently",
         "Implement reverse complement, k-mer counting, and Hamming distance"],
        "07_alphafold3_core",
        "02_dynamic_programming",
    ),
    "08_practical_problems/02_dynamic_programming.ipynb": (
        ["Apply dynamic programming to sequence alignment, knapsack, and longest-path problems",
         "Recognise optimal-substructure patterns and implement memoisation/tabulation"],
        "01_strings_dna",
        "03_graphs_assembly",
    ),
    "08_practical_problems/03_graphs_assembly.ipynb": (
        ["Model biological assembly as Eulerian/Hamiltonian path problems on de Bruijn graphs",
         "Implement BFS/DFS and topological sort for genome-assembly workflows"],
        "02_dynamic_programming",
        "04_statistics_ml_practical",
    ),
    "08_practical_problems/04_statistics_ml_practical.ipynb": (
        ["Apply hypothesis testing, bootstrapping, and regression to biological datasets",
         "Implement and interpret ROC/AUC, precision-recall, and calibration curves"],
        "03_graphs_assembly",
        "05_alignment_phylogeny",
    ),
    "08_practical_problems/05_alignment_phylogeny.ipynb": (
        ["Solve combined alignment and phylogenetics problems at HackerRank difficulty",
         "Apply UPGMA, Neighbour Joining, and parsimony methods programmatically"],
        "04_statistics_ml_practical",
        "06_mock_assessment",
    ),
    "08_practical_problems/06_mock_assessment.ipynb": (
        ["Complete a timed mock assessment covering all practical problem types",
         "Identify your weak areas and revisit the relevant module notebooks"],
        "05_alignment_phylogeny",
        "09_ml_teaching_essentials/01_model_diagnostics — Module 09",
    ),
    # 09_ml_teaching_essentials
    "09_ml_teaching_essentials/01_model_diagnostics.ipynb": (
        ["Diagnose underfitting and overfitting using learning and validation curves",
         "Calibrate classifier probabilities with Platt scaling and temperature scaling"],
        "08_practical_problems",
        "10_openfold3_finetuning/00_openfold3_walkthrough — Module 10",
    ),
    # 10_openfold3_finetuning — only 01 missing
    "10_openfold3_finetuning/01_protein_structure_finetuning.ipynb": (
        ["Fine-tune a Pairformer-based protein structure model with LoRA adapters",
         "Apply the complete fine-tuning loop: data loading, loss, validation, and checkpointing"],
        "00_openfold3_walkthrough",
        "11_membrane_protein_dynamics/01_membrane_protein_dynamics — Module 11",
    ),
    # 11_membrane_protein_dynamics
    "11_membrane_protein_dynamics/01_membrane_protein_dynamics.ipynb": (
        ["Predict transmembrane topology and fine-tune a structure model on membrane proteins",
         "Explain how lipid bilayer context changes protein structure predictions"],
        "10_openfold3_finetuning",
        "02_md_simulation_basics",
    ),
    "11_membrane_protein_dynamics/02_md_simulation_basics.ipynb": (
        ["Describe the Verlet integrator, periodic boundary conditions, and PME electrostatics",
         "Compare classical force fields with ML potentials for molecular dynamics"],
        "01_membrane_protein_dynamics",
        "12_generative_models/01_diffusion_protein_design — Module 12",
    ),
    # 12_generative_models — only 01 missing (02_connecting and 02_flow have completion)
    "12_generative_models/01_diffusion_protein_design.ipynb": (
        ["Implement the forward noising process and reverse denoising for protein backbone diffusion",
         "Condition generation on sequence or structural motifs"],
        "11_membrane_protein_dynamics",
        "02_connecting_modules_12_to_15 or 02_flow_matching_protein_design",
    ),
    # 13_bayesian_methods
    "13_bayesian_methods/01_bayesian_ml_uncertainty.ipynb": (
        ["Quantify aleatoric and epistemic uncertainty with MC Dropout and conformal prediction",
         "Apply Bayesian optimisation with a Gaussian Process surrogate for protein design"],
        "12_generative_models",
        "14_reinforcement_learning/01_rl_protein_design — Module 14",
    ),
    # 14_reinforcement_learning
    "14_reinforcement_learning/01_rl_protein_design.ipynb": (
        ["Implement DQN and PPO for discrete sequence optimisation",
         "Explain how GFlowNets sample diverse, high-reward protein sequences"],
        "13_bayesian_methods",
        "15_self_supervised_learning/01_contrastive_ssl — Module 15",
    ),
    # 15_self_supervised_learning
    "15_self_supervised_learning/01_contrastive_ssl.ipynb": (
        ["Implement masked language modelling and SimCLR contrastive pretraining",
         "Fine-tune a self-supervised protein encoder for downstream property prediction"],
        "14_reinforcement_learning",
        "16_mlops_deployment/01_mlops_for_protein_ml — Module 16",
    ),
    # 16_mlops_deployment
    "16_mlops_deployment/01_mlops_for_protein_ml.ipynb": (
        ["Set up experiment tracking with MLflow and model serving with FastAPI",
         "Build a CI/CD pipeline for protein ML models with monitoring and drift detection"],
        "15_self_supervised_learning",
        "17_capstone_project/00_end_to_end_pipeline — Module 17",
    ),
}


def make_completion_cell(skills, prev_mod, next_mod):
    bullets = "\n".join(f"- {s}" for s in skills)
    source = (
        "## Notebook Complete\n\n"
        "**You can now:**\n"
        f"{bullets}\n\n"
        "**Where this fits:**\n"
        f"- Previous: {prev_mod}\n"
        f"- Next: {next_mod} — check the README\n\n"
        "**Before moving on, check:**\n"
        "- [ ] All code cells ran without errors\n"
        "- [ ] You understand what each function does (read the docstrings)\n"
        "- [ ] You can explain the key concept in one sentence without looking at notes"
    )
    return make_markdown_cell(source)


# ---------------------------------------------------------------------------
# Helper — find insertion index for glossary (after TL;DR or first markdown)
# ---------------------------------------------------------------------------

def find_glossary_insert_index(cells):
    """Return the index to insert the glossary cell.

    Strategy: insert after the first markdown cell whose source contains
    'TL;DR' (case-insensitive).  If none found, insert after the very first
    markdown cell (index 0 -> insert at 1).
    """
    for i, c in enumerate(cells):
        if c["cell_type"] == "markdown":
            src = "".join(c["source"]).lower()
            if "tl;dr" in src or "plain english" in src:
                return i + 1
    # Fallback: after first markdown cell
    for i, c in enumerate(cells):
        if c["cell_type"] == "markdown":
            return i + 1
    return 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    modified = []

    # ---- Task 1 ----
    print("=== Task 1: Adding glossary cells ===")
    for rel_path, glossary_source in GLOSSARY_CELLS.items():
        path = os.path.join(BASE, rel_path)
        nb = load(path)
        src_all = full_source(nb)
        if "concepts for beginners" in src_all:
            print(f"  SKIP (already has glossary): {rel_path}")
            continue
        idx = find_glossary_insert_index(nb["cells"])
        cell = make_markdown_cell(glossary_source)
        nb["cells"].insert(idx, cell)
        save(path, nb)
        modified.append(rel_path)
        print(f"  ADDED glossary at index {idx}: {rel_path}")

    # ---- Task 2 ----
    print("\n=== Task 2: Adding Common Errors cells ===")
    for rel_path in TASK2_NOTEBOOKS:
        path = os.path.join(BASE, rel_path)
        nb = load(path)
        src_all = full_source(nb)
        if "common errors" in src_all or "troubleshooting" in src_all:
            print(f"  SKIP (already has errors section): {rel_path}")
            continue
        # Insert before last cell
        insert_idx = len(nb["cells"]) - 1
        cell = make_markdown_cell(ERRORS_SOURCE)
        nb["cells"].insert(insert_idx, cell)
        save(path, nb)
        modified.append(rel_path)
        print(f"  ADDED errors cell before last cell: {rel_path}")

    # ---- Task 3 ----
    print("\n=== Task 3: Adding completion cells ===")
    for rel_path, (skills, prev_mod, next_mod) in COMPLETION_DATA.items():
        path = os.path.join(BASE, rel_path)
        nb = load(path)
        src_all = full_source(nb)
        if "you can now" in src_all or "notebook complete" in src_all or "✅" in src_all:
            print(f"  SKIP (already has completion): {rel_path}")
            continue
        cell = make_completion_cell(skills, prev_mod, next_mod)
        nb["cells"].append(cell)
        save(path, nb)
        modified.append(rel_path)
        print(f"  ADDED completion cell: {rel_path}")

    print(f"\nDone. Modified {len(modified)} notebooks.")
    for p in modified:
        print(f"  {p}")


if __name__ == "__main__":
    run()
