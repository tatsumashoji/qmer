#!/bin/bash

source config

#$HISAT_INDEX $SourceDirGenome $SourceDirGenome

$HISAT2 -x $SourceDirGenome \
	-1 $D1/${1}_1.clean.fastq.gz \
	-2 $D1/${1}_2.clean.fastq.gz \
        -p 4 \
	-S $D2/$1.sam 2> $StatsDirBam/$1.txt
$samtools view -Sb $D2/$1.sam > $D2/$1.bam
$samtools sort -@ 4 -o $D2/$1.sort $D2/$1.bam
$samtools index $D2/$1.sort
$samtools view -h $D2/$1.sort > $D2/$1.sam
