# -*- coding: utf-8 -*-
import sys


def make_fasta(infile, outfile):
    new = []

    f = open(infile).readlines()

    for i in range(len(f)):
        elements = f[i].split(" ")
        new.append(">"+str(i)+"_"+str(elements[0]+"\n"))
        new.append(elements[1])

    g = open(outfile, "w")
    g.writelines(new)
    g.close()



if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile.split(".")[0] + ".tp2"
    make_fasta(infile, outfile)

