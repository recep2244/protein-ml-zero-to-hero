# data/ — Dataset Directory

This folder is for downloaded datasets. **It is not committed to Git.**

The `.gitignore` at the project root excludes all files in `data/` to prevent accidentally committing large binary files or proprietary datasets. If you add a new dataset, keep it here and it will stay out of version control automatically.

---

## Datasets Used in This Curriculum

The table below lists every external dataset referenced in the notebooks, with instructions for downloading each one. All datasets are freely available.

| Dataset | Module(s) | Notebook(s) | Approx. Size | URL | How to Download |
|---|---|---|---|---|---|
| UniProt/Swiss-Prot (reviewed proteins) | 01, 04, 15 | 01/01, 04/01, 15/01 | ~800 MB | https://www.uniprot.org/downloads | Download `uniprot_sprot.fasta.gz`, unzip to `data/uniprot_sprot.fasta` |
| PDB mmCIF structures | 03, 06, 07 | 03/01, 06/01, 07/01–07/04 | varies per structure | https://www.rcsb.org | Use `biopython` PDBList or wget individual PDB IDs (e.g., `1MBO.cif`) |
| SCOP 2.0 domain classification | 03, 06 | 03/01, 06/01 | ~15 MB | https://scop.mrc-lmb.cam.ac.uk/download | Download `dir.cla.scope.2.08-stable.txt` |
| Pfam domain database | 01, 04 | 01/04, 04/01 | ~2.5 GB (full) | https://pfam.xfam.org/static/documents/current_release/ | Download `Pfam-A.fasta.gz`; for quick tests use the 100-seed subset |
| Human genome GFF3 annotation | 02 | 02/01, 02/02 | ~50 MB | https://ftp.ensembl.org/pub/release-111/gff3/homo_sapiens/ | Download `Homo_sapiens.GRCh38.111.chr.gff3.gz`, unzip |
| TCGA gene expression (LUAD) | 04 | 04/01 | ~200 MB | https://portal.gdc.cancer.gov | Download HTSeq counts via GDC Data Transfer Tool; save to `data/tcga_luad/` |
| BindingDB binding affinity | 10, 13 | 10/01, 13/01 | ~1.5 GB | https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp | Download `BindingDB_All.tsv.zip`, unzip |
| AlphaFold2 predicted structures (E. coli) | 07 | 07/01, 07/02 | ~1 GB | https://alphafold.ebi.ac.uk/download | Download `UP000000625_83333_ECOLI.tar`, extract to `data/af2_ecoli/` |
| Rosalind sample datasets | 01, 08 | 01/01–01/06, 08/01–08/05 | <1 MB each | https://rosalind.info | Each problem page provides a sample dataset link; save to `data/rosalind/` |
| Protein Data Bank Chemical Component Dictionary | 10, 11 | 10/01, 11/01 | ~50 MB | https://www.wwpdb.org/data/ccd | Download `components.cif.gz` |

---

## Download Helper Script

A convenience script to download the most commonly used small datasets is provided at `utils/download_data.py`. Run it from the project root:

```bash
python utils/download_data.py
```

This will download and place Rosalind sample files and a handful of representative PDB structures into `data/`. For large datasets (UniProt, TCGA), follow the manual instructions in the table above.

---

## Simulated Data Fallback

Every notebook in this curriculum generates its own simulated data if the real dataset is not present. This means you can run any notebook without downloading anything first. The simulated data is designed to have the same shape and statistical properties as the real data so that the code and visualizations behave identically.

When a notebook uses simulated data it prints a notice:

```
NOTE: Real dataset not found at data/uniprot_sprot.fasta.
      Using simulated sequences. Download instructions: data/README.md
```

---

## Adding a New Dataset

If you are contributing a notebook that uses an external dataset:

1. Add an entry to the table above in a PR.
2. Implement a simulated-data fallback in the notebook so it runs without the download.
3. Do **not** commit the dataset file itself — only the download instructions.
4. If the dataset requires authentication or a data use agreement, note that clearly in the table.
