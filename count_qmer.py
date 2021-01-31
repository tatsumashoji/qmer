# -*- coding: utf-8 -*-
import sys
from Bio import SeqIO
import pandas as pd

def count(res, seq, n, bias):
    for i in range(len(seq)-n+1):
        try:
            res[seq[i:i+n]] += bias
        except:
            res[seq[i:i+n]] = bias

    return res


def count_fasta(seqs, n):
    res = {}
    for name in seqs.keys():
        bias = int(name.split("_")[1])
        seq = str(seqs[name])
        res = count(res, seq, n, bias)

    return res


def drop_N(qmer):
    return {key : qmer[key] for key in qmer.keys() if "N" not in key}


def save_qmer(qmer, fname):
    df = pd.DataFrame(pd.Series(qmer))
    df.columns = [fname]
    df.to_csv(fname)


if __name__ == '__main__':
    seqs = {i.description : i.seq for i in SeqIO.parse("/home/tatsu2/projects/qmer/"+str(sys.argv[1])+".tp2","fasta")}
    size = int(sys.argv[2])


    for i in range(size):
        qmer = count_fasta(seqs, i+1)
        qmer_drop = drop_N(qmer)
        save_qmer(qmer_drop, "/home/tatsu2/projects/qmer/"+str(sys.argv[1])+".qmer_"+str(i+1)+".csv")
