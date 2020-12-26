# -*- coding: utf-8 -*-
from Bio import SeqIO
import pandas as pd

def count(seq, n):
    res = {}
    for i in range(len(seq)-n+1):
        if seq[i:i+n] in res.keys():
            res[seq[i:i+n]] += 1
        else:
            res[seq[i:i+n]] = 1

    return res


def count_fasta(seqs, n):
    res_all = {}
    for name in seqs.keys():
        bias = int(name.split("_")[1])
        seq = str(seqs[name])
        res = count(seq, n)
        res = {key : res[key] * bias for key in res.keys()}
        for key in res.keys():
            try:
                res_all[key] += res[key]
            except:
                res_all[key] = res[key]

    return res_all


def drop_N(qmer):
    return {key : qmer[key] for key in qmer.keys() if "N" not in key}


def save_qmer(qmer, fname):
    df = pd.DataFrame(pd.Series(qmer))
    df.columns = [fname]
    df.to_csv(fname)


if __name__ == '__main__':
    seqs = {i.description : i.seq for i in SeqIO.parse("tp2","fasta")}
    qmers = [count_fasta(seqs,i+1) for i in range(11)]
    qmers_drop = [drop_N(i) for i in qmers]
    for i in range(len(qmers_drop)):
        save_qmer(qmers_drop[i], "qmer_"+str(i+1)+".csv")
