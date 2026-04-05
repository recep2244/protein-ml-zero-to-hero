# Module 02 — Genomics & Gene Analysis
This module covers the full genomics pipeline — from raw RNA-seq counts and variant calling through pathway enrichment — giving you the data wrangling and statistical skills needed for omics-scale biology.

## What You'll Learn
- Parse and manipulate genomic file formats: FASTA, FASTQ, VCF, GTF, BED
- Perform differential expression analysis on RNA-seq count matrices
- Identify and interpret genetic variants (SNPs, indels) from VCF files
- Conduct ORF finding, codon table lookups, and gene prediction
- Build phylogenetic trees from multiple sequence alignments
- Apply pathway and gene ontology enrichment analysis (Fisher's exact, FDR correction)
- Handle the statistical challenges specific to high-dimensional genomics data

## Prerequisites
| Required knowledge | Where to get it |
|-------------------|-----------------|
| Python data manipulation (Pandas, NumPy) | `00_python_ml_basics/02_ml_fundamentals.ipynb` |
| Basic molecular biology (DNA → RNA → protein) | `01_sequence_analysis/01_alignment_algorithms.ipynb` |
| Sequence file formats and parsing | `01_sequence_analysis/02_rosalind_complete.ipynb` |
| Basic statistics (hypothesis testing, p-values) | `00_python_ml_basics/08_mathematical_foundations.ipynb` |

## Notebooks in This Module
| # | Notebook | Topics | Time |
|---|----------|--------|------|
| 1 | `01_genomics_core.ipynb` | Codon tables, ORF finding, GC content, genome annotation, FASTA/VCF parsing | ~5h |
| 2 | `02_rnaseq_analysis.ipynb` | RNA-seq pipeline, count normalization (TPM, RPKM), DEG analysis, heatmaps | ~5h |
| 3 | `03_variant_analysis.ipynb` | VCF parsing, SNP/indel classification, functional annotation, variant filtering | ~4h |
| 4 | `04_pathway_enrichment.ipynb` | GO terms, KEGG pathways, Fisher's exact test, FDR correction, GSEA | ~4h |

## After This Module You Can
- Process RNA-seq count data from raw matrix to ranked differentially expressed gene list
- Parse VCF files and classify variants by functional impact
- Run pathway enrichment analysis and interpret biological significance of gene sets
- Build codon usage tables and predict ORFs in novel sequences
- Apply multiple testing correction correctly in high-dimensional genomics settings

## Key Concepts Introduced
- **Differential expression**: Statistical identification of genes whose mRNA abundance changes significantly between conditions.
- **TPM (Transcripts Per Million)**: Read count normalization that accounts for both sequencing depth and gene length.
- **VCF (Variant Call Format)**: Standard file format encoding genomic variants with quality scores and genotype information.
- **FDR (False Discovery Rate)**: Multiple-testing correction (Benjamini-Hochberg) that controls the expected proportion of false positives.
- **Gene Ontology (GO)**: Hierarchical vocabulary for annotating gene functions across biological process, molecular function, and cellular component.
- **GSEA**: Gene Set Enrichment Analysis — a method to determine whether a predefined gene set shows statistically significant enrichment at the top or bottom of a ranked gene list.

## Next Module
→ [Module 03 — Protein Structural Biology](../03_protein_structural_biology/README.md)

## Difficulty: ⭐⭐⭐ (1–5 stars)
## Estimated Time: 18–22 hours
