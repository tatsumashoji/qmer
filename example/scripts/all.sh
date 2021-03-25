#!/bin/bash

source config

bash p0_setup.sh
$HISAT_INDEX $SourceDirGenome $SourceDirGenome

for i in `ls $D0 | cut -d. -f1-2 | cut -d_ -f1 | sort | uniq`;do
	bash p1_trimmo.sh $i
	bash p2_mapping.sh $i
	bash p3_count.sh $i
	bash p4_qmer.sh $i
done

