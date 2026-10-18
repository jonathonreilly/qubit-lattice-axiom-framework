#!/bin/bash
cd "$(dirname "$0")"
for P in S S2 S4; do B24_NM=20 timeout 1500 python3 screen25.py $P 4 > screen25_$P.log 2>&1; done
