# -*- coding: utf-8 -*-
import sys
import itertools as it

def count(res, seq, n, bias):
    for i in range(len(seq)-n+1):
        try:
            res[seq[i:i+n]] += bias
        except:
            res[seq[i:i+n]] = bias

    return res


def count_fasta(infile, n):
    v = [i.rstrip().split(" ") for i in open(infile, "r").readlines()]
    res = {}
    for t in v:
        bias = int(t[0])
        seq = str(t[1])
        res = count(res, seq, n, bias)

    return res


def drop_N(qmer):
    return {key : qmer[key] for key in qmer.keys() if "N" not in key}


def qmer_all(b, q):
    b = ["A","T","G","C"]
    if q >= 2:
        return ["".join(i) for i in list(it.product(b, qmer_all(b, q - 1)))]
    else:
        return b

def qmer_sort(res, q):
    b = ["A","T","G","C"]
    qindex = qmer_all(b, q)
    result = []
    for i in qindex:
        try:
            result.append([i,str(res[i])])
        except:
            result.append([i,"0"])
    return result


def save_qmer(qmer, fname):
    f = open(fname, "w")
    qmer_array = [",".join(i) + "\n" for i in qmer]
    f.writelines(qmer_array)
    f.close()


if __name__ == '__main__':
    infile = sys.argv[1]
    size = int(sys.argv[2])

    for i in range(size):
        qmer = count_fasta(infile, i + 1)
        qmer_drop = drop_N(qmer)
        qmer_s = qmer_sort(qmer_drop, i + 1)
        save_qmer(qmer_s, infile + ".qmer_"+str(i+1)+".csv")
