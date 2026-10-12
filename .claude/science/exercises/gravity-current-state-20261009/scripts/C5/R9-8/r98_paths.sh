#!/bin/bash
export OMP_NUM_THREADS=2
for E in "-1 -1" "1.0 1.8" "0.5 1.9" "0.6 1.4" "0.3 1.9"; do for N in 96 128; do python3 -I r98_paths.py 2.0 3.0 1.0 2.0 3.0 $N 0.2 $E; done; done
