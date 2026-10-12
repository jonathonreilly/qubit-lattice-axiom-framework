#!/bin/bash
export OMP_NUM_THREADS=2
for E in "0.3 1.9" "1.0 1.8"; do for N in 128 160; do python3 -I r98_paths.py 2.0 3.0 1.0 2.0 3.0 $N 0.1 $E; done; done
for E in "0.3 0.9" "0.5 0.9"; do python3 -I r98_paths.py 1.0 2.0 1.0 1.0 2.0 128 0.2 $E; done
