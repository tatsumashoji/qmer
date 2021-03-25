#!/bin/bash

source config

java -jar $Trimmo \
    PE -phred33 -threads 4 \
    $D0/${1}_1.fastq.gz \
    $D0/${1}_2.fastq.gz \
    $D1/${1}_1.clean.fastq.gz \
    $D1/${1}_1.clean.fastq.gz.unpaired \
    $D1/${1}_2.clean.fastq.gz \
    $D1/${1}_2.clean.fastq.gz.unpaired \
    ILLUMINACLIP:$Iclip:2:30:10 \
    TRAILING:3 LEADING:3 SLIDINGWINDOW:4:15 MINLEN:20 &> $StatsDirTrimo/$1.txt
