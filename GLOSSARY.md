# Glossary — Bioinformatics ML Curriculum

Every technical term used across the 40 notebooks in this curriculum, defined in plain English first and then technically. Terms are grouped by domain and sorted alphabetically within each section. Use the section headers to jump to the area you need.

If a term is not here, check `RESOURCES.md` or ask Claude Code: "explain [term] in the context of this curriculum."

---

## Table of Contents

- [Biology Terms](#biology-terms)
- [Bioinformatics Terms](#bioinformatics-terms)
- [Machine Learning Terms](#machine-learning-terms)
- [Advanced ML Terms](#advanced-ml-terms)
- [Structural ML Terms](#structural-ml-terms)

---

## Biology Terms

### Allele
**Plain English:** Most genes come in different versions — like eye color can be "blue version" or "brown version." Each of those versions is called an allele. You inherit one from each parent, so you carry two alleles for most genes.
**Technical:** An allele is a variant form of a gene at a specific locus on a chromosome. Diploid organisms carry two alleles per locus, which may be identical (homozygous) or different (heterozygous).
**In this curriculum:** Module 02 (`02_genomics_gene_analysis/`) covers allele frequencies, Hardy-Weinberg equilibrium, and variant analysis.

### Alpha Helix
**Plain English:** One of the most common shapes that a section of protein chain folds into. Imagine winding a piece of ribbon tightly around a cylinder — the resulting spiral is an alpha helix. It is held together by weak bonds between nearby parts of the chain.
**Technical:** A right-handed coiled secondary structure where the backbone NH group of each amino acid forms a hydrogen bond with the backbone C=O group of the amino acid four residues earlier. Approximately 3.6 residues per turn.
**In this curriculum:** Module 03 (`03_protein_structural_biology/`) involves parsing and identifying secondary structure elements including alpha helices from PDB files.

### Amino Acid
**Plain English:** The building blocks of proteins. There are 20 types, each with a slightly different shape and chemical personality. When linked together in a chain, they form a protein. The order of amino acids in the chain determines what shape the protein will fold into.
**Technical:** Amino acids are organic molecules containing an amine group (-NH2), a carboxyl group (-COOH), and a variable side chain (R group). The 20 standard amino acids differ in their R groups, which determine their chemical properties (hydrophobic, polar, charged, etc.).
**In this curriculum:** Amino acid sequences (FASTA format) are the input to nearly every model in this curriculum, from Module 01 through Module 17.

### Beta Sheet
**Plain English:** Another common protein fold shape. Instead of a spiral like the alpha helix, imagine two or more sections of the protein chain lying side by side, like strands in a piece of fabric. These strands are held together by weak bonds between them.
**Technical:** A secondary structure where multiple strands of the polypeptide backbone lie alongside each other, connected by inter-strand hydrogen bonds. Strands can be parallel (N-termini pointing the same way) or antiparallel (N-termini alternating direction).
**In this curriculum:** Secondary structure prediction and identification from PDB files is covered in Module 03. DSSP classification of secondary structure is used in Module 07.

### Codon
**Plain English:** DNA is written in a 4-letter alphabet (A, T, G, C). But proteins are written in a 20-letter alphabet (the 20 amino acids). The translation table between them reads 3 DNA letters at a time — that group of 3 is called a codon. Each codon specifies one amino acid (or a "stop" signal).
**Technical:** A codon is a triplet of nucleotides in mRNA that specifies either an amino acid or a stop signal during translation. The genetic code maps 64 possible codons (4^3) to 20 amino acids plus 3 stop codons, with most amino acids having multiple synonymous codons (degeneracy).
**In this curriculum:** Codon tables and translation are implemented in Module 02 (`02_genomics_gene_analysis/01_`). ORF finding requires reading the sequence in all six reading frames.

### DNA (Deoxyribonucleic Acid)
**Plain English:** The long molecule that stores the instructions for building every protein in a living organism. Written in a 4-letter alphabet (A, T, G, C), it is arranged in two strands that wrap around each other in the famous double helix. Different sections of DNA are called genes, and each gene contains the instructions for one protein.
**Technical:** DNA is a double-stranded polymer of deoxyribonucleotides. The two strands are antiparallel and complementary (A pairs with T, G pairs with C). The sequence encodes genetic information that is transcribed to mRNA and then translated to protein.
**In this curriculum:** DNA sequences are worked with throughout Modules 01 and 02. Sequence alignment algorithms operate directly on DNA strings.

### Gene
**Plain English:** A section of DNA that contains the instructions for building one protein. Humans have about 20,000 genes, each one a different set of instructions. When a gene is "active," the cell reads those instructions and builds the corresponding protein.
**Technical:** A gene is a sequence of DNA that encodes a functional RNA molecule, most commonly an mRNA that is translated into a protein. Genes include both coding regions (exons) and regulatory regions (promoters, enhancers) that control when and how much the gene is expressed.
**In this curriculum:** Gene structure, ORF finding, and gene expression analysis are covered in Modules 01-04.

### Gene Ontology (GO)
**Plain English:** A standardized vocabulary for describing what a gene or protein does. Instead of every lab using different words to say "this protein helps cells divide," GO provides universal terms everyone can use. This makes it possible to compare results across experiments and organisms.
**Technical:** Gene Ontology is a controlled vocabulary with three sub-ontologies: Biological Process (what pathway the gene participates in), Molecular Function (the biochemical activity of the gene product), and Cellular Component (where in the cell the gene product acts). GO terms are organized hierarchically.
**In this curriculum:** GO annotations and pathway analysis are introduced in Module 02 as part of interpreting gene expression results.

### Gene Expression
**Plain English:** The process of a cell reading a gene and using it to build the corresponding protein. Not all genes are active in all cells at all times — gene expression is regulated. Measuring which genes are "on" or "off" in a disease state vs. a healthy state is one of the main uses of genomics in medicine.
**Technical:** Gene expression refers to the transcription of a gene into mRNA and the subsequent translation into protein. Expression levels are typically measured by RNA-seq, which counts mRNA copies. Differential expression analysis identifies genes that are significantly more or less expressed between conditions.
**In this curriculum:** Gene expression data analysis is the focus of Module 04 (`04_ml_bioinformatics/01_`), including the high-dimensional (p>>n) challenge and dimensionality reduction.

### Genotype
**Plain English:** Your complete DNA sequence — the set of alleles you carry for every gene. Two people can have the same phenotype (brown eyes) but different genotypes (different specific DNA variants that both happen to produce brown pigment).
**Technical:** Genotype refers to the genetic composition of an individual, either at a specific locus or across the genome. In population genetics, genotype frequencies at a locus are described as the proportions of AA, Aa, and aa individuals in a population.
**In this curriculum:** Genotype-phenotype relationships and Hardy-Weinberg equilibrium are covered in Module 02.

### GPCR (G Protein-Coupled Receptor)
**Plain English:** One of the most important protein families in medicine. GPCRs sit on the surface of cells and act like antennas: they detect a signal on the outside (like a hormone or a drug molecule), and transmit that signal to the inside of the cell. About 30% of all approved drugs work by binding to a GPCR.
**Technical:** GPCRs are integral membrane proteins with seven transmembrane helices. Ligand binding triggers conformational changes that activate intracellular G proteins, initiating downstream signaling cascades. They are the largest family of drug targets in the human genome.
**In this curriculum:** GPCRs are studied as a specific case of transmembrane proteins in Module 11 (`11_membrane_protein_dynamics/`).

### Hardy-Weinberg Equilibrium
**Plain English:** A mathematical rule that says: in a population that is not changing (no natural selection, no mutations, random mating), the proportions of different alleles will stay constant from generation to generation, and you can predict the proportion of each genotype from just the allele frequencies. It is a useful baseline — when the data deviates from this prediction, something biologically interesting is happening.
**Technical:** For a biallelic locus with allele frequencies p and q (where p + q = 1), Hardy-Weinberg equilibrium predicts genotype frequencies of p2 (AA), 2pq (Aa), and q2 (aa). Significant deviation indicates selection, population structure, genotyping error, or other factors.
**In this curriculum:** Hardy-Weinberg calculations are implemented in Module 02 as part of variant analysis.

### Intrinsically Disordered Region (IDR)
**Plain English:** Most proteins fold into a specific 3D shape. But some sections of a protein — or even entire proteins — never settle into one fixed shape. They stay floppy and flexible, sampling many conformations. These regions are called intrinsically disordered. They are not broken — many of them are biologically critical, especially in signaling.
**Technical:** IDRs are protein segments lacking a stable three-dimensional structure under physiological conditions. They are characterized by low sequence complexity, enrichment in polar and charged residues, and depletion of hydrophobic residues. Many IDRs adopt transient structures upon binding partners.
**In this curriculum:** Disorder prediction and handling of flexible regions is discussed in Module 07 in the context of AlphaFold3's pLDDT confidence metric.

### KEGG (Kyoto Encyclopedia of Genes and Genomes)
**Plain English:** A large database that maps out the biological "circuits" inside cells — which proteins interact with which other proteins, and what those interactions accomplish (like breaking down glucose, or sending a growth signal). It is a reference for interpreting which pathways are activated or deactivated in a disease.
**Technical:** KEGG is a bioinformatics database integrating genomic, chemical, and systemic functional information. It includes pathway maps, molecular interaction networks, reaction networks, and genome/chemical databases. KEGG pathway analysis is commonly used to interpret differential expression results.
**In this curriculum:** KEGG pathways are used in Module 02 and Module 04 to contextualize gene expression changes.

### Lipid Bilayer
**Plain English:** The thin wall that surrounds every cell. It is made of two layers of fat molecules (lipids) facing each other. The outside of each layer is water-loving, and the inside is water-repelling. This creates a barrier that controls what goes in and out of the cell. Membrane proteins (like GPCRs) are embedded in this bilayer.
**Technical:** A biological membrane composed of two sheets of phospholipid molecules. Each phospholipid has a hydrophilic (water-loving) head and two hydrophobic (water-repelling) fatty acid tails. The tails face inward, forming a hydrophobic core that prevents the passage of polar molecules and ions.
**In this curriculum:** Lipid bilayer properties and their effect on embedded proteins are covered in Module 11.

### mRNA (Messenger RNA)
**Plain English:** The middle step between DNA and protein. When a gene is "on," the cell makes a copy of the gene's instructions in a slightly different format (RNA instead of DNA) — that copy is mRNA. It then travels to the ribosome, which reads the mRNA and assembles the corresponding protein.
**Technical:** mRNA is a single-stranded RNA molecule transcribed from a DNA template by RNA polymerase. It carries the coding sequence (codons) that ribosomes read during translation to synthesize protein. The 5' UTR, 3' UTR, and poly-A tail regulate mRNA stability and translation efficiency.
**In this curriculum:** RNA-seq measures mRNA abundance. mRNA sequences appear in ORF finding exercises in Module 01 and 02.

### PDB (Protein Data Bank)
**Plain English:** The world's archive of protein 3D shapes. When scientists determine the structure of a protein (using X-ray crystallography, cryo-electron microscopy, or NMR), they deposit their coordinates here. The PDB contains over 200,000 structures and is freely accessible to anyone. AlphaFold was trained largely on PDB structures.
**Technical:** The RCSB Protein Data Bank (PDB) is a global archive of experimentally determined three-dimensional structures of biological macromolecules. Each entry includes atomic coordinates, experimental metadata, and sequence information in PDB or mmCIF format.
**In this curriculum:** PDB parsing and structure analysis is the core of Module 03. Modules 06, 07, and 10 all use PDB-derived data.

### Peptide Bond
**Plain English:** The chemical connection that links amino acids together into a protein chain. When two amino acids join, they release a water molecule and form a peptide bond. A protein is just a very long chain of amino acids held together by peptide bonds.
**Technical:** A peptide bond is a covalent amide bond formed between the carboxyl group (-COOH) of one amino acid and the amine group (-NH2) of the next, with loss of water. The resulting C-N bond has partial double-bond character due to resonance, restricting rotation and enforcing planarity.
**In this curriculum:** Peptide bond geometry constrains backbone structure and is fundamental to understanding protein secondary structure, covered in Module 03.

### Phenotype
**Plain English:** The observable characteristics of an organism — how it looks, how it behaves, whether it has a particular disease. Phenotype is the result of genotype plus environment. Two people with the same genetic variant might show different phenotypes depending on their lifestyle, age, and other genes.
**Technical:** Phenotype encompasses all observable or measurable characteristics of an organism resulting from the interaction of its genotype with its environment. In clinical genomics, phenotype often refers to the presence or absence of a disease or trait.
**In this curriculum:** Genotype-phenotype associations and variant effect prediction are covered in Modules 02 and 04.

### Primary Structure
**Plain English:** The sequence of amino acids in a protein, read from one end (the N-terminus) to the other (the C-terminus). It is the one-dimensional description of the protein — just a string of letters. Everything else (shape, function) flows from this sequence.
**Technical:** Primary structure is the linear amino acid sequence of a polypeptide chain, determined by the gene sequence. It is conventionally written N-terminus to C-terminus using single-letter or three-letter amino acid codes.
**In this curriculum:** Primary structure (amino acid sequence) is the input to every model in Modules 05-10.

### Protein
**Plain English:** The workhorses of the cell. Proteins are long chains of amino acids that fold into 3D shapes and perform nearly every function in biology: catalyzing chemical reactions, transmitting signals, providing structural support, defending against pathogens. There are about 20,000 different proteins in the human body.
**Technical:** A protein is a macromolecule composed of one or more polypeptide chains, each a sequence of amino acids joined by peptide bonds. Proteins fold into specific three-dimensional structures determined by their amino acid sequence, and these structures determine their function.
**In this curriculum:** Protein structure and function is the central subject of this entire curriculum, from Module 01 through Module 17.

### Quaternary Structure
**Plain English:** Some proteins work as a team — multiple protein chains come together and function as a unit. The way those chains are assembled and arranged is the quaternary structure. Hemoglobin (which carries oxygen in blood) is a classic example: four protein chains assembled into one functional unit.
**Technical:** Quaternary structure refers to the arrangement of multiple folded polypeptide subunits (protomers) in a multi-subunit complex. It is stabilized by the same non-covalent interactions as tertiary structure, plus occasional disulfide bonds between subunits.
**In this curriculum:** Multi-chain protein complexes are handled in Module 07 (AlphaFold3 multi-chain prediction) and Module 10.

### RNA (Ribonucleic Acid)
**Plain English:** A molecule similar to DNA but with a few chemical differences. RNA plays many roles in the cell: mRNA carries gene instructions from DNA to the ribosome, tRNA delivers amino acids during protein synthesis, and rRNA is the structural component of the ribosome itself. Some RNA molecules also act as enzymes.
**Technical:** RNA is a single-stranded nucleic acid composed of ribonucleotides (containing ribose instead of deoxyribose, and uracil instead of thymine). Major classes include mRNA (coding), tRNA (transfer), rRNA (ribosomal), snRNA (splicing), miRNA, and lncRNA.
**In this curriculum:** RNA structure and interactions are included in AlphaFold3's scope (Module 07), which can predict RNA-protein and RNA-DNA complexes.

### Secondary Structure
**Plain English:** The local 3D shape that sections of the protein chain fold into. The two most common secondary structures are the alpha helix (a coil) and the beta sheet (parallel strands). These are the building blocks that combine to form the overall 3D shape.
**Technical:** Secondary structure refers to the local conformation of the polypeptide backbone, arising from regular patterns of backbone hydrogen bonding. Alpha helices and beta strands are the canonical secondary structures, with turns and coils connecting them.
**In this curriculum:** Secondary structure assignment (DSSP) and prediction are covered in Module 03 and used as features in Modules 06 and 07.

### SNP (Single Nucleotide Polymorphism)
**Plain English:** A single-letter difference in DNA between individuals. Imagine two people's DNA is identical except one spot where one person has an "A" and the other has a "G." That is a SNP. Most SNPs have no effect, but some change a protein's function and can influence disease risk.
**Technical:** A SNP is a single base-pair variation at a specific position in the genome, present in at least 1% of the population. SNPs can be synonymous (not changing the amino acid), missense (changing the amino acid), or nonsense (introducing a stop codon). Genome-wide association studies (GWAS) link SNPs to phenotypes.
**In this curriculum:** SNP analysis and variant effect prediction are covered in Module 02. Mutation effect prediction using protein language models is in Module 10.

### Tertiary Structure
**Plain English:** The complete 3D shape of the protein — how all the helices and sheets fold up against each other to form the final structure. This is the structure that determines the protein's function. This is what AlphaFold predicts.
**Technical:** Tertiary structure is the three-dimensional conformation of an entire polypeptide chain, including all side chains. It arises from non-covalent interactions (hydrophobic packing, hydrogen bonds, electrostatic interactions, van der Waals forces) and disulfide bonds. Tertiary structure determines binding pockets and functional surfaces.
**In this curriculum:** Tertiary structure prediction and analysis is the main focus of Modules 03, 06, 07, and 10.

### Transcription
**Plain English:** The first step in using a gene: copying the DNA instructions into RNA. The enzyme that does this (RNA polymerase) reads the DNA and produces a complementary mRNA strand. The mRNA then travels out of the nucleus to be used as a template for building the protein.
**Technical:** Transcription is the synthesis of RNA from a DNA template by RNA polymerase. The process involves promoter recognition, initiation, elongation, and termination. In eukaryotes, pre-mRNA undergoes processing (5' capping, splicing, 3' polyadenylation) before export from the nucleus.
**In this curriculum:** The transcription/translation flow is foundational context for all sequence-based models in Modules 01-05.

### Translation
**Plain English:** The second step: reading the mRNA instructions and assembling the protein. The ribosome moves along the mRNA, reads each codon, and adds the corresponding amino acid to the growing protein chain. When it hits a stop codon, the protein is released.
**Technical:** Translation is the ribosome-mediated synthesis of a polypeptide chain from an mRNA template. tRNA molecules deliver aminoacyl-tRNAs to the ribosomal A site, the peptidyl transferase catalyzes peptide bond formation, and the ribosome translocates along the mRNA in the 5' to 3' direction.
**In this curriculum:** Codon tables and translation are implemented in Module 02. Understanding translation is prerequisite for understanding ORF finding.

### Transmembrane Helix
**Plain English:** Some proteins need to reach through the cell wall (the lipid bilayer). To do this, a section of the protein forms a helix that is covered in water-repelling amino acids — this lets it pass through the water-repelling interior of the membrane. GPCRs have seven of these transmembrane helices.
**Technical:** A transmembrane helix is an alpha-helical segment of a membrane protein that spans the lipid bilayer. It is enriched in hydrophobic residues and is approximately 20-25 amino acids long, matching the thickness of the hydrophobic core of the bilayer (~30 Angstroms).
**In this curriculum:** Transmembrane topology prediction and membrane-specific modeling are covered in Module 11.

---

## Bioinformatics Terms

### BLAST (Basic Local Alignment Search Tool)
**Plain English:** A fast tool for searching a database of known sequences to find anything similar to your query sequence. If you have a new protein sequence and want to know if anything like it has been seen before, you BLAST it against the protein database (NCBI nr). It returns a list of similar sequences ranked by similarity score.
**Technical:** BLAST uses a heuristic algorithm (seeded word matching followed by ungapped, then gapped, extension) to find local alignments between a query sequence and database sequences. It reports alignments with their E-value (expected number of alignments with that score by chance in a database of that size).
**In this curriculum:** BLAST concepts and sequence search are covered in Module 01 (`01_sequence_analysis/03_`).

### BLOSUM62
**Plain English:** A scoring matrix for amino acid substitutions. Not all substitutions are equally likely — some amino acids frequently swap for each other during evolution (because they have similar shapes), while others almost never do. BLOSUM62 assigns a score to every possible amino acid swap, positive for common swaps and negative for rare ones. Alignment algorithms use these scores to find biologically meaningful alignments.
**Technical:** BLOSUM62 is a substitution matrix derived from aligned blocks of protein sequences sharing 62% identity. Each entry BLOSUM62[a][b] gives the log-odds score for observing amino acid b in a position where amino acid a is present. It is the default substitution matrix for BLAST protein searches.
**In this curriculum:** BLOSUM62 is used in sequence alignment scoring in Module 01 and for computing evolutionary distance features in later modules.

### CCD (Chemical Component Dictionary)
**Plain English:** The PDB's reference dictionary for every small molecule that has ever appeared in a protein structure — drug molecules, cofactors, metal ions, etc. Each entry has the molecule's name, chemical formula, and 3D atom positions. AlphaFold3 uses the CCD to represent small molecule ligands.
**Technical:** The CCD is a curated library of chemical component definitions used in PDB entries. Each CCD entry specifies atom names, connectivity (bonding graph), ideal coordinates, and chemical properties. AlphaFold3 encodes ligands using CCD-derived atom-level features as input to its structure prediction pipeline.
**In this curriculum:** CCD-based ligand encoding is described in Module 07 and used in Module 10 for protein-ligand binding prediction.

### De Bruijn Graph
**Plain English:** A way of assembling a genome from millions of short overlapping fragments (reads). Instead of trying to overlap whole reads (computationally expensive), you break everything into short k-letter words (k-mers) and build a graph where each word connects to its overlap. Following a path through the graph reconstructs the original sequence.
**Technical:** A De Bruijn graph for genome assembly has one node per unique (k-1)-mer, and one directed edge per k-mer connecting its left (k-1)-mer to its right (k-1)-mer. The genome assembly problem reduces to finding an Eulerian path (visiting every edge once) in this graph.
**In this curriculum:** De Bruijn graphs and genome assembly are covered in Module 01 (`01_sequence_analysis/05_`).

### Edit Distance
**Plain English:** A measure of how different two strings are, defined as the minimum number of insertions, deletions, and substitutions needed to turn one string into the other. For DNA or protein sequences, edit distance (and its extensions) is the basis of sequence alignment.
**Technical:** Also called Levenshtein distance. For strings s and t, the edit distance is computed by dynamic programming. The recurrence is dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (0 if s[i]==t[j] else 1)).
**In this curriculum:** Edit distance is introduced as the conceptual foundation for Needleman-Wunsch in Module 01.

### Hidden Markov Model (HMM)
**Plain English:** A statistical model for sequences where there is an underlying process (the "hidden" part) generating what you observe. For protein families, the hidden states are positions in the protein (structurally conserved positions, insertions, deletions), and what you observe are the amino acids at each position. HMMs can model the variability across all members of a protein family.
**Technical:** An HMM is a probabilistic model with hidden states connected by transition probabilities and observed emissions at each state with emission probabilities. For sequence analysis, profile HMMs model multiple sequence alignments: match states emit amino acid distributions, insert states model insertions, and delete states model gaps.
**In this curriculum:** Profile HMMs for protein family modeling are covered in Module 01 (`01_sequence_analysis/04_`). MSA-based HMMs are used as features in AlphaFold (Module 07).

### Kabsch Algorithm
**Plain English:** A method for finding the best way to rotate one protein structure to match another. Given two sets of corresponding atom positions, the Kabsch algorithm finds the rotation matrix that minimizes the sum of squared distances between them. This is necessary before computing RMSD.
**Technical:** The Kabsch algorithm computes the optimal rotation matrix R that minimizes the RMSD between two centered point sets. It uses Singular Value Decomposition (SVD) of the covariance matrix H = P^T Q, giving R = V U^T (with a correction for reflections).
**In this curriculum:** Implemented from scratch in Module 03 (`03_protein_structural_biology/01_`). Understanding SVD and rotation matrices is expected for this module.

### Multiple Sequence Alignment (MSA)
**Plain English:** Aligning many related sequences simultaneously so that corresponding positions line up across all sequences. If you have the same gene from 100 different species, an MSA shows which positions are conserved across all species (likely critical for function) and which vary (less constrained).
**Technical:** An MSA is an arrangement of three or more biological sequences such that homologous positions are aligned across all sequences, with gap characters inserted as necessary. Common algorithms include Clustal, MAFFT, and MUSCLE. MSAs encode evolutionary information used by AlphaFold and protein language models.
**In this curriculum:** MSA construction and usage are covered in Module 01. AlphaFold3 uses MSA as a key input (Module 07). ESM-2 was trained on evolutionary sequences from MSAs (Module 15).

### Needleman-Wunsch
**Plain English:** An algorithm for finding the best global alignment of two sequences — aligning them end to end. It works by dynamic programming: filling in a table where each cell represents the best score for aligning the first i characters of sequence A with the first j characters of sequence B.
**Technical:** Needleman-Wunsch is an O(mn) dynamic programming algorithm for global sequence alignment, where m and n are the sequence lengths. The scoring matrix is filled using: dp[i][j] = max(dp[i-1][j-1] + s(a_i, b_j), dp[i-1][j] - gap, dp[i][j-1] - gap). The alignment is recovered by traceback.
**In this curriculum:** Implemented from scratch in Module 01 (`01_sequence_analysis/01_`). One of the first exercises in the curriculum.

### Open Reading Frame (ORF)
**Plain English:** A section of a DNA or RNA sequence that could potentially encode a protein. It starts with the start codon (ATG) and ends with a stop codon. Finding all ORFs in a genome is one of the first steps in predicting which genes are present.
**Technical:** An ORF is a continuous stretch of codons beginning with a start codon (ATG) and ending with a stop codon (TAA, TAG, or TGA), read in a single reading frame. A genome has six possible reading frames (three on each strand). ORF finding filters by minimum length to reduce false positives.
**In this curriculum:** ORF finding is implemented in Module 02 (`02_genomics_gene_analysis/01_`).

### PAE (Predicted Aligned Error)
**Plain English:** A confidence score generated by AlphaFold for each pair of residues in a prediction. It estimates: "how far off would the position of residue A be, if I aligned the structure on residue B?" Low PAE means AlphaFold is confident about the relative positions of two residues. High PAE means it is uncertain — often because the residues are in flexible regions or different domains.
**Technical:** PAE is a per-residue-pair confidence metric output by AlphaFold. PAE[i][j] is the expected position error (in Angstroms) at residue i when the predicted and true structures are aligned on residue j. PAE matrices are used to identify well-predicted domains and flexible interdomain relationships.
**In this curriculum:** PAE matrices are output and interpreted in Module 07. They are used to distinguish rigid domains from flexible linkers.

### pLDDT (Predicted Local Distance Difference Test)
**Plain English:** AlphaFold's per-residue confidence score. Each residue gets a score from 0 to 100. A score above 90 means AlphaFold is very confident about that residue's position. A score below 50 means the residue is likely in a disordered region and the predicted position is not reliable.
**Technical:** pLDDT is a per-residue confidence score predicted by AlphaFold's structure module. It estimates the lDDT-Ca score (local distance difference test on Ca atoms) that the prediction would achieve relative to the experimental structure. pLDDT > 90: high confidence; 70-90: good; 50-70: low; <50: disordered.
**In this curriculum:** pLDDT scores are output by AlphaFold in Module 07 and used as confidence filters in Module 10.

### RMSD (Root Mean Square Deviation)
**Plain English:** A single number measuring how different two protein structures are. You align them on top of each other, measure the distance between each pair of corresponding atoms, square all those distances, average them, and take the square root. RMSD = 0 means identical structures. RMSD > 2 Angstroms usually means significantly different structures.
**Technical:** RMSD = sqrt(1/N * sum_i |r_i - r'_i|^2), where r_i and r'_i are the positions of corresponding atoms in the two structures after optimal superimposition. Typically computed on Ca atoms only for structure comparison purposes.
**In this curriculum:** RMSD is implemented in Module 03 and used throughout Modules 06, 07, and 17 to evaluate structure prediction quality.

### Rosalind
**Plain English:** A free online platform (rosalind.info) with hundreds of bioinformatics programming exercises, named after Rosalind Franklin. Each problem teaches a specific algorithm or biological concept through a coding challenge. Many problems in this curriculum are adapted from or directly reference Rosalind.
**Technical:** Rosalind is an educational platform for learning bioinformatics through problem solving. It covers topics from basic string operations on DNA to advanced graph algorithms and probabilistic models, with automatic solution checking.
**In this curriculum:** Rosalind problems are woven throughout Modules 01 and 02, and collected in Module 08 (`08_practical_problems/`).

### Sequence Alignment
**Plain English:** The process of lining up two or more biological sequences (DNA, RNA, or protein) to find the regions that match. Matching regions often indicate shared ancestry or shared function. The alignment reveals which positions are conserved and which have changed during evolution.
**Technical:** Sequence alignment assigns a correspondence between positions in two or more sequences, with gap characters inserted to maximize a scoring function (match/mismatch scores and gap penalties). Global alignment (Needleman-Wunsch) aligns full sequences; local alignment (Smith-Waterman) finds the best-scoring sub-alignment.
**In this curriculum:** Sequence alignment algorithms are the core of Module 01, and evolutionary information from MSAs feeds into all subsequent structure prediction modules.

### Smith-Waterman
**Plain English:** Like Needleman-Wunsch, but for local alignment — finding the best matching region within two longer sequences, rather than aligning them end to end. This is useful when you want to find a conserved domain inside a larger protein.
**Technical:** Smith-Waterman is an O(mn) dynamic programming algorithm for local sequence alignment. It differs from Needleman-Wunsch in that negative scores are set to zero (dp[i][j] = max(0, ...)), and traceback starts from the highest-scoring cell. It finds the optimal local alignment.
**In this curriculum:** Implemented in Module 01 (`01_sequence_analysis/02_`), alongside Needleman-Wunsch.

### TM-score (Template Modeling Score)
**Plain English:** A better measure of structural similarity than RMSD for comparing whole proteins. RMSD is very sensitive to a few badly aligned regions even if most of the structure is correct. TM-score normalizes by protein length and focuses on the global fold similarity, giving a score between 0 and 1. TM-score > 0.5 generally means the same fold.
**Technical:** TM-score = max{ 1/L_target * sum_i 1/(1 + (d_i/d_0)^2) }, where d_i is the distance between the i-th pair of aligned residues after optimal superimposition, d_0 is a length-dependent normalization factor, and the maximum is over all alignments. It is invariant to protein length.
**In this curriculum:** TM-score is implemented in Module 03 alongside RMSD, and used as the primary evaluation metric in Module 17.

---

## Machine Learning Terms

### Attention Mechanism
**Plain English:** A way for a neural network to focus on the most relevant parts of its input when producing an output. Instead of processing every input position equally, attention computes a weighted sum of all positions, where the weights are learned based on how relevant each position is to the current computation.
**Technical:** Given query Q, key K, and value V matrices, attention computes: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) * V. The softmax produces normalized attention weights; the output is a weighted sum of the values. Multi-head attention applies this h times in parallel with different learned projections.
**In this curriculum:** Attention is introduced in Module 05 and is the core operation in the Transformer (Module 05), the Pairformer (Module 07), and LoRA (Module 10).

### Backpropagation
**Plain English:** The algorithm that teaches a neural network. After making a prediction, you compute how wrong it was (the loss). Backpropagation then works backwards through the network, computing how much each weight contributed to that error, so you can adjust each weight slightly to reduce the error next time.
**Technical:** Backpropagation applies the chain rule of calculus to compute the gradient of the loss with respect to every parameter in the network. Starting from the loss and moving backwards through the computational graph, each operation's local gradient is multiplied by the upstream gradient.
**In this curriculum:** Backpropagation is introduced in Module 00 (PyTorch autograd section) and assumed throughout. The gradient flow section of Module 05 covers vanishing/exploding gradients.

### Batch Normalization
**Plain English:** A technique for stabilizing neural network training. Between layers, it normalizes the values passing through (subtracts the mean, divides by the standard deviation), then applies a learned scaling and shift. This prevents values from getting too large or too small, which helps training converge faster.
**Technical:** For a mini-batch of activations, BatchNorm computes: y = gamma * (x - mean_batch) / sqrt(var_batch + epsilon) + beta, where gamma and beta are learned parameters. At test time, running statistics from training are used. It reduces internal covariate shift.
**In this curriculum:** Batch normalization is covered in Module 05 as part of the normalization techniques section. Layer normalization (used in Transformers) is also covered.

### Batch Size
**Plain English:** How many training examples you show the network at once before updating its weights. A small batch (e.g., 8) gives noisier but faster updates. A large batch (e.g., 512) gives more accurate gradient estimates but requires more memory and compute per update.
**Technical:** Batch size is the number of samples processed in one forward-backward pass. The gradient computed over a mini-batch is an estimate of the true gradient over the full dataset. Very small batches add regularization-like noise; very large batches can converge to sharp, less generalizable minima.
**In this curriculum:** Batch size is a training hyperparameter throughout Modules 05-10. Gradient accumulation (Module 07) simulates large batches when memory is limited.

### BERT
**Plain English:** A widely influential language model (from Google, 2018) that introduced bidirectional pre-training: reading text from both left to right and right to left simultaneously. This gives richer representations than earlier models that only read in one direction. The protein language model ESM-2 is essentially BERT applied to protein sequences.
**Technical:** BERT (Bidirectional Encoder Representations from Transformers) uses a Transformer encoder pre-trained on masked language modeling (predict randomly masked tokens) and next sentence prediction. The bidirectional self-attention allows each position to attend to all others, unlike causal models.
**In this curriculum:** BERT-style masked language modeling is the pre-training objective for ESM-2, covered in Module 15. Fine-tuning BERT-like models with LoRA is covered in Module 10.

### BiLSTM (Bidirectional Long Short-Term Memory)
**Plain English:** A type of recurrent neural network that reads a sequence both forward (left to right) and backward (right to left) and combines both representations. For protein sequences, reading bidirectionally captures both local and long-range context. BiLSTMs were the dominant sequence model before Transformers.
**Technical:** A BiLSTM runs a forward LSTM and a backward LSTM over the input sequence, then concatenates (or sums) their hidden states at each position. LSTMs use gating mechanisms (input, forget, output gates) to selectively retain information over long sequences, addressing the vanishing gradient problem of vanilla RNNs.
**In this curriculum:** BiLSTMs are introduced in Module 05 as the pre-Transformer baseline, used for splice site prediction in the provided figure (`bilstm_splice.png`).

### CNN (Convolutional Neural Network)
**Plain English:** A neural network that applies the same learned filter repeatedly across the input, scanning for local patterns. Originally developed for images (where nearby pixels are related), CNNs also work well for sequences (where nearby residues are related). They are efficient because the same filter is shared across all positions.
**Technical:** CNNs apply learned convolutional filters of width k to the input, producing feature maps. Key operations: convolution (filter sliding across input), pooling (spatial downsampling), and non-linear activation. For sequences, 1D convolutions with variable filter sizes capture motifs at different scales.
**In this curriculum:** CNNs for sequence classification are covered in Module 05. They appear again in Module 07 as part of the structure module's pair representation processing.

### Cross-Validation
**Plain English:** A more robust way to estimate how well your model generalizes than a single train/test split. You split the data into k equal parts, train on k-1 parts and test on the remaining part, then repeat k times (each time holding out a different part). The average test performance across all k rounds is your estimate.
**Technical:** k-fold cross-validation partitions the dataset into k folds. In each of k iterations, one fold is the validation set and the remaining k-1 folds are the training set. Stratified k-fold maintains class proportions in each fold. Leave-one-out (LOO) is the limiting case k=n.
**In this curriculum:** Cross-validation is covered in Module 00 and used throughout Modules 04 and 08 for small-dataset evaluation.

### Data Leakage
**Plain English:** Accidentally letting your model see test data during training, which makes its performance look better than it actually is. Common examples: normalizing the whole dataset before splitting train/test (the test set statistics "leaked" into training), or including future information as features.
**Technical:** Data leakage occurs when information from outside the training set contaminates the model during training, leading to overly optimistic evaluation metrics. Common sources: preprocessing the entire dataset before splitting, target encoding with test labels, or temporal leakage in time-series data.
**In this curriculum:** Data leakage is a key warning in Module 04 (gene expression analysis with high-dimensional features) and Module 09.

### Dropout
**Plain English:** A regularization technique where, during training, you randomly turn off some neurons (set them to zero) with a certain probability. This forces the network to learn redundant representations and not rely too heavily on any single neuron, reducing overfitting.
**Technical:** During training, each neuron's activation is set to zero with probability p (the dropout rate), and the remaining activations are scaled by 1/(1-p) to maintain expected activation magnitudes. At test time, all neurons are active (dropout is disabled). Commonly used with p=0.1-0.5.
**In this curriculum:** Dropout is covered in Module 05 and used for uncertainty estimation (MC Dropout) in Module 13.

### Embedding
**Plain English:** A way to represent discrete objects (like letters, words, or amino acids) as dense vectors of numbers. Instead of treating each amino acid as one of 20 separate categories, an embedding maps it to a point in, say, 128-dimensional space, where similar amino acids end up close together.
**Technical:** An embedding is a learned mapping from a discrete set (vocabulary of size V) to a continuous vector space of dimension d. Implemented as a lookup table (weight matrix of shape V x d). The embedding layer is typically the first layer of sequence models and its weights are trained along with the rest of the network.
**In this curriculum:** Amino acid embeddings are used in all sequence models from Module 05 onward. Protein language model embeddings (ESM-2) are used as pre-computed features in Modules 10 and 15.

### Equivariance
**Plain English:** A property of a model meaning that if you transform its input in some way (like rotating a protein), the output transforms in the same predictable way. For a protein structure model, rotating the protein should rotate the predicted forces, not change them randomly. Equivariant models are more physically meaningful and data-efficient.
**Technical:** A function f is equivariant to a group G if f(g * x) = rho(g) * f(x) for all group elements g, where rho is a representation of G on the output space. For SE(3), equivariance to rotations and translations is essential for physical correctness in molecular modeling.
**In this curriculum:** Equivariance is introduced in Module 06 and is a design requirement for the GNN architectures in Modules 06 and 07.

### Fine-Tuning
**Plain English:** Starting from a model that has already been trained on a large dataset, and then training it further on your specific, smaller dataset. The idea is that the large pre-trained model has already learned useful general representations, and you just need to adapt them to your specific task.
**Technical:** Fine-tuning initializes model weights from a pre-trained checkpoint and continues training with a small learning rate on task-specific data. The pre-trained representations are used as a starting point, which requires less data and compute than training from scratch. May involve updating all parameters or just a subset (partial fine-tuning, LoRA, etc.).
**In this curriculum:** Fine-tuning is introduced in Module 05 and is the core topic of Modules 10 and 15.

### GNN (Graph Neural Network)
**Plain English:** A neural network designed to work on graph-structured data — nodes connected by edges. For proteins, you can represent the protein as a graph where each amino acid is a node and edges connect amino acids that are spatially close. A GNN can learn from both the node features (what amino acid it is) and the graph structure (which amino acids are neighbors).
**Technical:** GNNs update node representations by aggregating information from neighboring nodes (message passing). At each layer: h_v^(l+1) = UPDATE(h_v^(l), AGGREGATE({h_u^(l) : u in N(v)})). Common variants: GCN, GAT, MPNN, SchNet, DimeNet.
**In this curriculum:** GNNs for protein structure are the focus of Module 06. The message passing framework and equivariant GNNs are covered in detail.

### Gradient Descent
**Plain English:** The core algorithm for training neural networks. Imagine you are standing on a hilly landscape in fog, trying to reach the lowest point (the minimum loss). Gradient descent says: look at the slope under your feet (the gradient), and take a small step downhill. Repeat many times until you reach the bottom (or close enough).
**Technical:** Gradient descent updates parameters theta by: theta = theta - alpha * gradient_loss(theta), where alpha is the learning rate. Stochastic gradient descent (SGD) computes the gradient on a single sample; mini-batch SGD uses a small batch. Adam combines SGD with adaptive per-parameter learning rates and momentum.
**In this curriculum:** Gradient descent is introduced in Module 00 and used throughout. Adam optimizer is the default in all deep learning modules.

### Learning Rate
**Plain English:** How big a step to take in gradient descent. Too large: the model overshoots the minimum and training is unstable. Too small: training takes forever. Learning rate scheduling (starting large and decreasing over time) is often used to get the best of both worlds.
**Technical:** The learning rate alpha is the scalar multiplier of the gradient in the parameter update rule. Common schedules: constant, step decay, cosine annealing, linear warmup + decay (used in Transformers). Learning rate warmup prevents large updates at the start of training when gradients are noisy.
**In this curriculum:** Learning rate scheduling is covered in Module 05 and used in training loops throughout Modules 07-10.

### LoRA (Low-Rank Adaptation)
**Plain English:** A clever method for fine-tuning large neural networks using very few additional parameters. Instead of updating all the weights in a large weight matrix, LoRA learns two small matrices whose product approximates the change needed. This reduces memory and compute by up to 100x while maintaining most of the performance.
**Technical:** For a weight matrix W (d x k), LoRA adds a learned perturbation: W_new = W + BA, where B (d x r) and A (r x k) are learned matrices with rank r << min(d,k). The original W is frozen. During inference, the perturbation is merged: W_merged = W + BA.
**In this curriculum:** LoRA is introduced in Module 05 and is the capstone technique of Module 10 for fine-tuning Pairformer on specific protein families.

### Loss Function
**Plain English:** A mathematical formula that measures how wrong your model's predictions are. The goal of training is to minimize this number. For classification, cross-entropy loss is common (it penalizes confident wrong predictions heavily). For regression, mean squared error (MSE) is common.
**Technical:** A loss function L(y_pred, y_true) maps predictions and true labels to a scalar value. For classification: cross-entropy = -sum_c y_c * log(p_c). For regression: MSE = 1/n * sum(y_pred - y_true)^2. The loss must be differentiable with respect to model parameters.
**In this curriculum:** Loss functions are introduced in Module 00. FAPE loss (a specialized structural loss) is derived and implemented in Module 07.

### LSTM (Long Short-Term Memory)
**Plain English:** A type of recurrent neural network with a special memory cell that can selectively remember or forget information over long sequences. The gating mechanisms prevent the "forgetting" problem that plagues simple RNNs, making LSTMs effective for longer sequences.
**Technical:** An LSTM unit has a cell state C_t and hidden state h_t, updated by input gate i, forget gate f, and output gate o: C_t = f * C_{t-1} + i * tanh(W_c [h_{t-1}, x_t] + b_c); h_t = o * tanh(C_t). The gates are sigmoid activations.
**In this curriculum:** LSTMs are covered in Module 05 as part of the recurrent architecture section, and appear in BiLSTM context.

### Message Passing
**Plain English:** The core operation in graph neural networks. Each node "sends a message" to its neighbors (passes some information about itself), collects messages from its own neighbors, and updates itself based on those messages. After several rounds, each node's representation captures information from its neighborhood.
**Technical:** In the message passing neural network (MPNN) framework: m_v = SUM_{u in N(v)} M(h_v, h_u, e_{vu}); h_v' = U(h_v, m_v), where M is the message function, U is the update function, and e_{vu} is the edge feature. Multiple rounds of message passing expand the receptive field.
**In this curriculum:** Message passing is introduced in Module 06 (`06_structural_ml_gnns/01_`) and is the computational primitive for all GNN models in the curriculum.

### Neural Network
**Plain English:** A computational system loosely inspired by the brain. It consists of layers of simple processing units (neurons), each of which computes a weighted sum of its inputs and passes the result through a non-linear function. By stacking many layers, neural networks can learn very complex patterns.
**Technical:** A feedforward neural network computes f(x) = sigma_L(W_L sigma_{L-1}(...sigma_1(W_1 x + b_1)...) + b_L), where W_l and b_l are weight matrices and bias vectors, and sigma_l are non-linear activation functions (ReLU, GELU, etc.). Parameters are learned by gradient descent.
**In this curriculum:** Neural networks are introduced in Module 00 (PyTorch) and used throughout. The architecture details vary: CNNs, RNNs, Transformers, GNNs — all are types of neural networks.

### Overfitting
**Plain English:** When a model learns the training data so well that it memorizes noise and quirks instead of learning the underlying pattern. It performs great on training data but poorly on new data it has not seen. Overfitting is more likely when the model is large and the dataset is small.
**Technical:** Overfitting occurs when model complexity exceeds what the training data can support. Formally, the generalization gap (test loss - train loss) is large and positive. Mitigation: regularization (L1/L2, dropout), early stopping, data augmentation, cross-validation for model selection.
**In this curriculum:** Overfitting and regularization are covered in Module 00 and 09. The bias-variance tradeoff is a central theme of Module 09.

### Regularization
**Plain English:** Techniques to prevent overfitting by penalizing model complexity. L1 regularization adds the sum of absolute weight values to the loss (encouraging sparse weights). L2 regularization adds the sum of squared weight values (encouraging small weights). Dropout is another form of regularization.
**Technical:** L2 regularization (weight decay) adds lambda * ||w||^2 to the loss, penalizing large weights. L1 regularization adds lambda * ||w||_1, inducing sparsity (many weights become exactly zero). In Adam optimizer, weight_decay parameter implements decoupled weight decay (AdamW).
**In this curriculum:** Regularization is covered in Modules 00 and 09. Weight decay as regularization is used in all transformer training runs.

### Transfer Learning
**Plain English:** Using knowledge gained from one task to help with a different but related task. Train a large model on a huge general dataset, then adapt it to your specific problem with much less data. The key insight is that features learned from the general task are often useful for the specific task.
**Technical:** Transfer learning involves pre-training a model on a source task and fine-tuning on a target task. The pre-trained weights serve as initialization. In the extreme case (zero-shot transfer), the pre-trained model is used directly without any fine-tuning on the target task.
**In this curriculum:** Transfer learning is introduced in Module 05 and is the foundational strategy of Module 10 (fine-tuning AlphaFold/OpenFold for specific protein families).

### Transformer
**Plain English:** The architecture behind almost every modern large language model (GPT, BERT, etc.) and protein model (AlphaFold, ESM-2). It processes sequences in parallel using attention: every position can directly attend to every other position, capturing long-range dependencies that recurrent networks struggle with.
**Technical:** The Transformer consists of stacked encoder and/or decoder layers, each containing multi-head self-attention and a position-wise feedforward network, with residual connections and layer normalization. Position is encoded via positional embeddings or rotary position embeddings (RoPE).
**In this curriculum:** The Transformer is introduced in Module 05. The Pairformer (Module 07) is a specialized Transformer operating on pairwise representations.

---

## Advanced ML Terms

### AlphaFold3
**Plain English:** The third version of structural biology research labs's protein structure prediction system, released in 2024. It extends AlphaFold2 in two critical ways: it can model any biological molecule (proteins, DNA, RNA, small molecules, ions), and it uses a diffusion model for structure generation instead of the earlier coordinate regression approach.
**Technical:** AlphaFold3 uses a Pairformer-based network to build a pairwise representation of the input, followed by a diffusion model that generates all-atom coordinates conditioned on that representation. It accepts multi-entity inputs and jointly models inter-molecular contacts.
**In this curriculum:** AlphaFold3 is the central focus of Module 07, with six dedicated notebooks covering its architecture, training, and evaluation.

### BF16 (Brain Float 16)
**Plain English:** A data type that uses half the memory of the standard 32-bit float, but with a different tradeoff than float16. BF16 keeps the full dynamic range of float32 (same number of exponent bits) but with less precision. For neural network training, this is usually a good tradeoff — you get fast mixed-precision training without the numerical instability that plagues float16.
**Technical:** BF16 is a 16-bit floating point format with 1 sign bit, 8 exponent bits, and 7 mantissa bits (vs. float32: 1/8/23). The 8-bit exponent matches float32, allowing straightforward conversion and preventing overflow. Supported by modern GPUs (A100, H100) and Google TPUs for fast matrix multiplication.
**In this curriculum:** BF16 mixed precision training is used in the AlphaFold3 training loop (Module 07) and OpenFold fine-tuning (Module 10).

### Bootstrap Ensemble
**Plain English:** A way to estimate uncertainty by training multiple models on slightly different random subsets of your training data. If all models agree on a prediction, you can be confident. If they disagree, that disagreement quantifies the uncertainty. Bootstrap ensembles are a practical and well-calibrated uncertainty method.
**Technical:** Bootstrap sampling draws N samples with replacement from a dataset of size N, creating multiple training sets. A model trained on each bootstrap sample forms an ensemble. The variance across ensemble predictions estimates the epistemic (model) uncertainty. For deep learning, this is expensive; MC Dropout is a cheaper approximation.
**In this curriculum:** Bootstrap ensembles and uncertainty quantification are covered in Module 13 (`13_bayesian_methods/01_`).

### Conformal Prediction
**Plain English:** A statistical framework for producing prediction intervals with a guaranteed coverage rate — for example, "I am 95% confident the true label is in this set." Unlike Bayesian methods, conformal prediction makes no assumptions about the data distribution and works with any model.
**Technical:** Conformal prediction uses calibration data to compute non-conformity scores (how unusual a point is relative to the training distribution). The prediction set at level 1-alpha includes all labels whose non-conformity score is below the (1-alpha) quantile of calibration scores. Coverage is exact for exchangeable data.
**In this curriculum:** Conformal prediction is covered in Module 13 as a distribution-free uncertainty quantification method.

### DDPM (Denoising Diffusion Probabilistic Model)
**Plain English:** The specific type of diffusion model used in systems like Stable Diffusion and AlphaFold3. The training process adds noise to data in small steps (the forward process), then trains a neural network to predict and remove that noise (the reverse process). Generation is done by starting from pure noise and repeatedly denoising.
**Technical:** DDPM defines a forward Markov chain q(x_t|x_{t-1}) = N(x_t; sqrt(1-beta_t) x_{t-1}, beta_t I) that gradually corrupts data. A neural network epsilon_theta is trained to predict the noise: L = E[||epsilon - epsilon_theta(x_t, t)||^2]. Sampling reverses the chain using the learned denoiser.
**In this curriculum:** DDPM is implemented in Module 12 (`12_generative_models/01_`) and used as the structure generation module in Module 07.

### Diffusion Model
**Plain English:** A generative model that learns to create new examples (images, protein structures, molecules) by learning how to reverse the process of adding random noise. You train it by: (1) adding increasing amounts of noise to real data, (2) training the model to predict what noise was added. Then to generate new examples, you start with pure noise and let the model gradually remove noise.
**Technical:** Diffusion models define a forward process that gradually destroys data structure by adding Gaussian noise, and a learned reverse process that denoises step by step. The score network parameterizes the reverse diffusion. Variants include DDPM, score matching, and flow matching (used in AlphaFold3).
**In this curriculum:** Diffusion models are introduced in Module 12 and are the structure generation mechanism in Module 07.

### Distogram
**Plain English:** A predicted probability distribution over the distances between every pair of amino acids in a protein. Instead of predicting a single distance, the model predicts: "there is a 15% chance residues 10 and 50 are 5-10 Angstroms apart, a 60% chance they are 10-15 Angstroms apart," etc. Distogram prediction was a key step in AlphaFold2's architecture.
**Technical:** A distogram bins the inter-residue Cb-Cb distance distribution into 64 discrete bins (2-22 Angstroms). The model predicts a categorical distribution over bins for each residue pair. The distogram provides a 2D representation of the protein fold that can be used directly for structure calculation or as an auxiliary loss.
**In this curriculum:** Distogram prediction is covered in Module 07 as an auxiliary prediction head in the AlphaFold3 training pipeline.

### FAPE Loss (Frame-Aligned Point Error)
**Plain English:** A specialized loss function used to train AlphaFold. It measures how wrong the predicted structure is relative to the true structure, but does so in a clever, physically meaningful way: it measures errors from the perspective of each amino acid's local coordinate frame. This makes the loss invariant to the overall rotation and position of the protein.
**Technical:** FAPE = 1/(N*N) * sum_{ij} ||T_i^{-1}(x_j) - T_i^{-1}(x_j')||, where T_i is the backbone rigid frame at residue i, x_j are true atom positions, and x_j' are predicted positions. The error is expressed in the local coordinate system of each residue's frame, making it SE(3)-invariant.
**In this curriculum:** FAPE loss is derived from first principles and implemented in Module 07 (`07_alphafold3_core/02_`).

### Flow Matching
**Plain English:** A modern alternative to DDPM for generative models. Instead of a fixed noise schedule, flow matching learns a vector field that maps noise to data along straight-line paths. This leads to faster sampling (fewer steps needed) and better training stability. AlphaFold3 uses a variant of flow matching.
**Technical:** Flow matching trains a velocity field v_theta(x, t) to match the conditional vector field that transforms samples from a noise distribution to the data distribution along straight-line trajectories. The objective is E[||v_theta(x_t, t) - (x_1 - x_0)||^2]. Samples are generated by integrating the ODE: dx/dt = v_theta(x, t).
**In this curriculum:** Flow matching is introduced in Module 07 as the diffusion variant used by AlphaFold3, and compared to DDPM in Module 12.

### GFlowNet (Generative Flow Network)
**Plain English:** A type of generative model that is particularly good at generating diverse objects that satisfy certain properties. Instead of optimizing for the single best molecule, a GFlowNet learns to sample proportionally to reward — so it explores the full space of good molecules, not just the best one found.
**Technical:** A GFlowNet models a sequential decision process (adding atoms, bonds) as a flow network, with a training objective that the flow through a terminal state should be proportional to its reward R(x). This ensures the generated distribution matches R^alpha, allowing the discovery of diverse high-reward objects.
**In this curriculum:** GFlowNets are introduced in Module 14 (`14_reinforcement_learning/01_`) as an alternative to PPO for molecule generation tasks.

### Gradient Accumulation
**Plain English:** A way to effectively train with a larger batch size when your GPU does not have enough memory to hold the full batch. Instead of updating weights after every batch, you run several smaller batches forward and backward, accumulate the gradients, and only update the weights after k batches. This is equivalent to training with k times the batch size.
**Technical:** Gradient accumulation runs k forward-backward passes before calling optimizer.step() and zero_grad(). The gradients are automatically summed across the k passes. Effective batch size = batch_size * accumulation_steps. Gradients should be divided by accumulation_steps if the loss is already averaged within each mini-batch.
**In this curriculum:** Gradient accumulation is part of the AlphaFold3 training loop implementation in Module 07.

### Gradient Clipping
**Plain English:** A safety technique for training neural networks. Sometimes during training, the gradient becomes extremely large (this is called an "exploding gradient"), which would make the weight update so large that it destroys the model. Gradient clipping caps the gradient magnitude at a maximum value before applying it.
**Technical:** Gradient clipping by norm rescales the gradient if its L2 norm exceeds a threshold: if ||g||_2 > clip_value, then g = g * clip_value / ||g||_2. PyTorch provides torch.nn.utils.clip_grad_norm_. Clip values of 1.0 or 0.1 are common for transformer training.
**In this curriculum:** Gradient clipping is part of the AlphaFold3 and OpenFold training loops in Modules 07 and 10.

### MC Dropout (Monte Carlo Dropout)
**Plain English:** A clever trick to estimate prediction uncertainty using a model that already has dropout. Normally, dropout is turned off at test time. MC Dropout keeps dropout on during inference and makes many predictions for the same input. The spread of those predictions estimates how uncertain the model is.
**Technical:** MC Dropout performs T stochastic forward passes with dropout enabled at test time. The predictive mean is the average of the T outputs, and the predictive uncertainty is estimated from their variance. It approximates Bayesian inference in a neural network with a specific prior over weights.
**In this curriculum:** MC Dropout is covered in Module 13 as a practical uncertainty estimation technique for protein structure prediction confidence.

### Pairformer
**Plain English:** The central neural network in AlphaFold3. It processes information about every pair of residues in the protein simultaneously, allowing the model to reason about how the distance between residues A and B is related to the distance between A and C, and between B and C (the triangle constraint). After many rounds, it builds a rich representation of the protein's structure.
**Technical:** The Pairformer is a stack of blocks, each containing: triangle attention (attending over pairs using triangle update rules), outer product mean (updating pair representations from single-sequence representations), and pair-to-single and single-to-pair transitions via feedforward networks. It operates on a (L x L x c_z) pairwise representation.
**In this curriculum:** The Pairformer is the focus of Module 07 (`07_alphafold3_core/01_`). Its implementation is the core of the OpenFold fine-tuning capstone in Module 10.

---

## Structural ML Terms

### Backbone Frame
**Plain English:** A local coordinate system defined by the backbone atoms of each amino acid. By placing a coordinate frame at each residue (using the positions of the N, Ca, and C atoms to define the axes), you can describe the relative positions of all other atoms in terms of local coordinates. This is the basis of FAPE loss.
**Technical:** The backbone frame at residue i is a rigid body transform T_i = (R_i, t_i) where R_i is the rotation matrix defined by the N-Ca-C backbone atoms and t_i is the translation (Ca position). All atom positions can be expressed in the local frame: x_local = R_i^T (x_global - t_i).
**In this curriculum:** Backbone frames are defined and implemented in Module 07 as the foundation for FAPE loss and the diffusion process.

### Boltz-2
**Plain English:** A recently released open-source protein structure prediction model from MIT, competitive with AlphaFold3, that can model proteins, nucleic acids, small molecules, and their interactions. Its key advance is end-to-end differentiability, making it easier to fine-tune for specific downstream tasks.
**Technical:** Boltz-2 uses a diffusion-based architecture with a confidence model output. It was trained on the PDB and is publicly available under an open-source license. Unlike AlphaFold3's server-only access, Boltz-2 can be run locally and fine-tuned.
**In this curriculum:** Boltz-2 is introduced in Module 07 as a contemporary alternative to AlphaFold3, with a comparison of architectures. Practical usage is covered in Module 10.

### E(3)-Equivariance
**Plain English:** A property of a model that means: if you rotate or reflect the protein in 3D space, the model's output rotates or reflects in the same way. For protein models, this is essential: the physics does not care about the orientation of your lab frame, so neither should your model. Achieving equivariance makes models much more data-efficient.
**Technical:** A function f is E(3)-equivariant if f(Rx + t) = rho(R) f(x) for all rotations/reflections R and translations t, where rho(R) is a group representation on the output space. SE(3)-equivariance excludes reflections. For scalars, rho(R) = 1 (invariance). For vectors, rho(R) = R.
**In this curriculum:** E(3)-equivariance is introduced in Module 06 (`06_structural_ml_gnns/02_`) and is a key design principle for all coordinate-based models in the curriculum.

### ESM-2
**Plain English:** A protein language model from Meta AI, trained on hundreds of millions of protein sequences. It reads an amino acid sequence and produces a rich numerical representation (embedding) for each residue that captures evolutionary, structural, and functional information. These embeddings are useful starting points for many downstream tasks.
**Technical:** ESM-2 (Evolutionary Scale Modeling 2) is a transformer-based protein language model with up to 15 billion parameters, pre-trained with masked language modeling on the UniRef90 sequence database. It produces per-residue embeddings that encode sequence context and co-evolutionary information implicitly.
**In this curriculum:** ESM-2 embeddings are used as features in Modules 10 and 15. Fine-tuning ESM-2 with LoRA for mutation effect prediction is a Module 10 exercise.

### MACE
**Plain English:** A fast and accurate machine learning force field — a model that predicts the energy and forces on each atom in a molecule from atom positions. MACE uses equivariant message passing to capture the geometric symmetries of atomic systems. It is used for molecular dynamics simulations.
**Technical:** MACE (Multi-Atomic Cluster Expansion) is an equivariant GNN that uses higher-order equivariant features (up to angular momentum l=3) for atomic representations. It achieves high accuracy on small molecule and materials property prediction while being significantly faster than quantum chemistry methods.
**In this curriculum:** MACE is introduced in Module 06 as an example of equivariant GNNs applied to molecular simulation.

### NequIP
**Plain English:** An early and influential equivariant neural network for molecular force fields. Unlike earlier models that treated forces as scalars, NequIP directly predicts vector-valued forces that transform correctly under rotation — a consequence of its E(3)-equivariant architecture.
**Technical:** NequIP (Neural Equivariant Interatomic Potentials) uses E(3)-equivariant convolutions building irreducible representations of the rotation group (spherical harmonics). Messages between atoms include both scalar (l=0) and vector (l=1) features, updated via equivariant tensor products (Clebsch-Gordan coefficients).
**In this curriculum:** NequIP is introduced in Module 06 as a foundational example of E(3)-equivariant molecular machine learning.

### OpenFold
**Plain English:** An open-source reimplementation of AlphaFold2, built in PyTorch, that is fully trainable and customizable. Unlike the official AlphaFold code (which was not designed for training from scratch), OpenFold allows researchers to fine-tune the model on new data, change the architecture, and run large-scale training experiments.
**Technical:** OpenFold implements the AlphaFold2 architecture in PyTorch with several engineering improvements: memory-efficient attention, kernel fusions, and support for multi-GPU training. It reproduces AlphaFold2's performance and adds trainability features not present in the original implementation.
**In this curriculum:** OpenFold is the code base for the capstone fine-tuning exercises in Module 10. The code walkthrough in Module 10 walks through OpenFold's Pairformer and structure module.

### Outer Product Mean
**Plain English:** A specific operation in AlphaFold's Pairformer for updating the pairwise (2D) representation using information from the single-sequence (1D) representation. For each pair of positions (i, j), you take the outer product of their single-sequence representations and average the result. This lets information flow from the sequence channel into the structure channel.
**Technical:** For single representations s_i and s_j (each of dimension c_s), the outer product mean update to pair representation z_ij is: z_ij += Linear(flatten(s_i outer_product s_j)), where the outer product s_i outer s_j has dimension c_s x c_s, which is linearly projected to the pair dimension c_z.
**In this curriculum:** The outer product mean is implemented in Module 07 as part of the Pairformer block.

### Rigid Body Transform
**Plain English:** A mathematical description of how to rotate and move a 3D object without stretching or squishing it. A rigid body transform is defined by a rotation (which way it is facing) and a translation (where it is located). In protein structure modeling, each residue's backbone frame is a rigid body.
**Technical:** A rigid body transform is an element of SE(3) (special Euclidean group): T = (R, t) where R is SO(3) (rotation matrix, det=1) and t is R^3 (translation vector). Composition: T_1 compose T_2 = (R_1 R_2, R_1 t_2 + t_1). Inverse: T^{-1} = (R^T, -R^T t).
**In this curriculum:** Rigid body transforms are defined in Module 07 and used throughout the AlphaFold3 implementation for backbone frame operations.

### Triangle Attention
**Plain English:** A specialized form of attention used in AlphaFold's Pairformer. In a protein, if residue A is close to B, and B is close to C, then A and C are probably somewhat close too (the triangle inequality). Triangle attention enforces this constraint by, when updating the (A,B) pair representation, attending over all pairs involving A or B, weighted by the (A,C) and (B,C) representations.
**Technical:** Triangle attention starting from node i: for each pair (i,j), attention weights are computed as a_{ijk} = softmax(1/sqrt(d) * Q_{ij} K_{ik} + b_{jk}), where Q, K come from z_{ij} and z_{ik}, and b_{jk} is a gate from z_{jk}. The update is z'_{ij} += sum_k a_{ijk} * V_{ik}. This shares information along the triangle (i,j), (i,k), (j,k).
**In this curriculum:** Triangle attention is implemented from scratch in Module 07 (`07_alphafold3_core/01_`). It is one of the most architecturally novel components of AlphaFold3.

---

*Last updated: 2026-04-05. To suggest additions or corrections, ask Claude Code: "update the GLOSSARY with the term X."*
