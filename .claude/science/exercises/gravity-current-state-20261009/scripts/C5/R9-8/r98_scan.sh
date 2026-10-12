#!/bin/bash
# R9-8 profile scan, shape S3 (b 2,3; r 1; photon box 2,3), m = lam = 0.2, N = 96 and 128. E1 < 0 = BQ control.
export OMP_NUM_THREADS=2
for E in "-1 -1" "1.0 1.8" "1.2 1.9" "0.6 1.4" "0.5 1.9" "0.3 1.9" "1.5 1.95" "0.25 0.5"; do
  for N in 96 128; do python3 -I r98_frame_qed.py 2.0 3.0 1.0 2.0 3.0 $N 0.2 0.2 $E; done
done
