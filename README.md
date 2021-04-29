# q-mer analysis: a generalized method for analyzing RNA-Seq data.

# 1. About

This repository is made for reproducing the results shown in the paper above.<br>
To reproduce, follow the below.

1. git clone https://github.com/tatsumashoji/qmer
2. cd path/to/qmer/example/scripts
3. Edit the command paths written in ``config`` file accordingly.
4. ``bash all.sh``
5. Follow the jupyter notebook "1.characterize_qmer_vectors.ipynb" to get Table 1.
6. Follow the jupyter notebook "2.count_based.ipynb" to get Figure 2 (A).
7. Follow the jupyter notebook "3.qmer_transformation.ipynb" to get Figure 2 other than (A).

Note that ``all.sh`` will take more than 1 month since ``all.sh`` does followings.

- Download fastq files. (36 RNA-Seq data in total).
- QC, mapping and count for each RNA-Seq data.
- Produce q-mer vector for each RNA-Seq data.

# 2. Requirements

- SRA tool kit (2.10.8)(fastq_dump)
- Trimmomatic (0.39)
- HISAT2 (2-2.2.1)
- featureCounts (2.0.1)
- python (3.7.3)
 - anaconda3-5.3.1
 - biopython (1.75)
 - pandas (0.23.4)
 - numpy (1.15.1)
 - sklearn (0.24.1)
 - bokeh (2.2.3)


