#!/bin/bash

# Load basic info.
source config


# Make directories
mkdir -p $SourceDir $StatsDir $StatsDirTrimo $StatsDirBam
mkdir -p $D0 $D1 $D2 $D3 $D4


# Download fastqs
# Healthy controls
for i in SRR5616891 SRR5616892 SRR5616893 SRR5616894 SRR5616895 SRR5616896 SRR5616897 SRR5616898 SRR5616899 SRR5616900 SRR5616901 SRR5616902 SRR5616903 SRR5616904 SRR5616905; do
	$fastq_dump --split-files --gzip $i
done
# Cocaine addicts
for i in SRR5616906 SRR5616907 SRR5616908 SRR5616909 SRR5616910 SRR5616911 SRR5616912 SRR5616913 SRR5616914 SRR5616915 SRR5616916 SRR5616917 SRR5616918 SRR5616919 SRR5616920 SRR5616922 SRR5616923 SRR5616924 SRR5616921; do
        $fastq_dump --split-files --gzip $i
done
mv SRR* $D0


# Get reference genome & gene feature file
wget http://ftp.ensembl.org/pub/release-103/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.toplevel.fa.gz
mv Homo_sapiens.GRCh38.dna.toplevel.fa.gz $SourceDir
gzip -d $SourceDir/Homo_sapiens.GRCh38.dna.toplevel.fa.gz
wget http://ftp.ensembl.org/pub/release-103/gff3/homo_sapiens/Homo_sapiens.GRCh38.103.gff3.gz
mv homo_sapiens/Homo_sapiens.GRCh38.103.gff3.gz $SourceDir
gzip -d $SourceDir/homo_sapiens/Homo_sapiens.GRCh38.103.gff3.gz

