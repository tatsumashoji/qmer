# -*- coding: utf-8 -*-
import sys


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
    f = open(fname, "w")
    qmer_array = [i + "," + qmer[i] + "\n" for i in qmer.keys()]
    f.writelines(qmer_array)
    f.close()


if __name__ == '__main__':
    # input1: fasta file
    infile = sys.argv[1]
    fasta = [i.rstrip() for i in open(infile).readlines()]
    seqs = {infile[2*i].split(">")[1] : infile[2*i+1] for i in range(int(len(infile)/2))}

    # input2: q value
    size = int(sys.argv[2])

    # calc. q-mer vectors
    for i in range(size):
        qmer = count_fasta(seqs, i+1)
        qmer_drop = drop_N(qmer)
        save_qmer(qmer_drop, infile + ".qmer_"+str(i+1)+".csv")
