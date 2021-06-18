# q-mer analysis: a generalized method for analyzing RNA-Seq data.

This repository is for the paper "q-mer analysis: a generalized method for analyzing RNA-Seq data."


# 1. How to use

To use q-mer analysis for the example data (example.sam), conduct the following.

```bash
./qmer example.sam example_result 10
```

# 2. How to reproduce the Figures in the paper

To reproduce, follow the jupyter notebook in ``qmer_cocaine`` or ``qmer_sz``.
Note that you need the gff file for _H. sapiens_ to follow the notebook ``1.count_based.ipynb``.

# 3. Requirements

- python (3.7.3)
- anaconda3-5.3.1
- biopython (1.75)
- pandas (0.23.4)
- numpy (1.15.1)
- sklearn (0.24.1)
- bokeh (2.2.3)


