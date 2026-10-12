#!/bin/bash
# straight-path electron (and photon) for S3, m = lam = 0.2; ng = 96 Gauss-Legendre nodes along each path; N = 48.
export OMP_NUM_THREADS=2
python3 -I r98_frame_qed.py 2.0 3.0 1.0 2.0 3.0 48 0.2 0.2 -1 -1
for E in "-1 -1" "0.3 1.9" "1.0 1.8"; do python3 -I r98_straight_e.py 2.0 3.0 1.0 2.0 3.0 48 0.2 0.2 $E 96; done
