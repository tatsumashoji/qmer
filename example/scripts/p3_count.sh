#!/bin/bash

source config

$featureCounts -p -t mRNA -g Parent -a $SourceDirGenomeMeta -o $D3/$1.count $D2/$1.sort

