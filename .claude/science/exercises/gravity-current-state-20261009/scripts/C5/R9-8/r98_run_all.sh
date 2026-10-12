#!/bin/bash
# Regenerates every R9-8 output (each python step < 1.5 min with OMP_NUM_THREADS=2). r85_box_qed.py is an unchanged copy of
# the refereed R8-5 runner (packet scripts/C5/R8-5/r85_box_qed.py), imported for the law's 1D functions.
set -e
export OMP_NUM_THREADS=2
python3 -I r98_checks.py > r98_checks.out
(python3 -I r85_box_qed.py box 2.0 3.0 1.0 2.0 3.0 64 0.2 0.2 | grep b1; python3 -I r98_frame_qed.py 2.0 3.0 1.0 2.0 3.0 64 0.2 0.2 -1 -1) > r98_validate.out
./r98_scan.sh > r98_scan_S3.out
./r98_scan2.sh > r98_scan2.out
./r98_paths.sh > r98_paths_S3.out
./r98_paths2.sh > r98_paths2.out
./r98_straight.sh > r98_straight.out
(python3 -I r98_frame_qed.py 2.0 3.0 1.0 2.0 3.0 32 0.2 0.2 -1 -1; for ng in 24 48; do python3 -I r98_straight_e.py 2.0 3.0 1.0 2.0 3.0 32 0.2 0.2 -1 -1 $ng; done) > r98_straight_quadcheck.out
