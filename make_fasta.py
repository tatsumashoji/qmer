# -*- coding: utf-8 -*-
import sys

def make_fasta():
    new = []

    f = open("/home/tatsu2/projects/qmer/"+str(sys.argv[1])).readlines()

    for i in range(len(f)):
        elements = f[i].split(" ")
        new.append(">"+str(i)+"_"+str(elements[0]+"\n"))
        new.append(elements[1])

    g = open("/home/tatsu2/projects/qmer/"+str(sys.argv[1])+".tp2", "w")
    g.writelines(new)
    g.close()



if __name__ == '__main__':
    make_fasta()
