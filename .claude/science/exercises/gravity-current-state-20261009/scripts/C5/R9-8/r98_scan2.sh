#!/bin/bash
# R9-8: shape S1 (b 1,2; r 1; photon box 1,2) profiles at m = 0.2, N = 96/128; and S3 at m = lam = 0.1, N = 128/160.
export OMP_NUM_THREADS=2
for E in "-1 -1" "0.5 0.9" "0.3 0.9" "0.6 1.4"; do
  for N in 96 128; do python3 -I r98_frame_qed.py 1.0 2.0 1.0 1.0 2.0 $N 0.2 0.2 $E; done
done
for E in "-1 -1" "1.0 1.8" "0.5 1.9"; do
  for N in 128 160; do python3 -I r98_frame_qed.py 2.0 3.0 1.0 2.0 3.0 $N 0.1 0.1 $E; done
done
