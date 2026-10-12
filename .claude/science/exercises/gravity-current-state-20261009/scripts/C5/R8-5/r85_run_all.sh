#!/bin/bash
# Reproduces every R8-5 output (each step < 1 min on the probe machine; OMP_NUM_THREADS=2).
set -e
export OMP_NUM_THREADS=2
python3 -I r85_box_qed.py validate > r85_validate.out
for N in 64 96 128 160; do for m in 0.2 0.1; do python3 -I r85_box_qed.py box 2.0 3.0 1.0 2.0 3.0 $N $m $m | grep b1; done; done > r85_S3_conv.out
for a in "160 0.05" "224 0.05" "224 0.025" "320 0.025" "320 0.0125" "448 0.0125"; do python3 -I r85_box_qed.py box 2.0 3.0 1.0 2.0 3.0 ${a% *} ${a#* } ${a#* } | grep b1; done > r85_S3_ir.out
./r85_shapes.sh > r85_shapes.out
(for r in 2 4 8 16 32; do for N in 224 320; do python3 -I r85_box_qed.py box 2.0 3.0 $r 2.0 3.0 $N 0.05 0.05 | grep b1; done; done
 for r in 4 16; do python3 -I r85_box_qed.py box 1.0 2.0 $r 1.0 2.0 320 0.05 0.05 | grep b1; done) > r85_heavy_edge.out
python3 -I r85_gauge_check.py > r85_gauge_check.out   # (the N=400 resolution rows were appended by an inline run; see report)
python3 -I r85_lemmaC_illustration.py > r85_lemmaC_illustration.out
python3 -I r85_numbers.py > r85_numbers.out
./r85_sameq.sh > r85_sameq_check.out
python3 -I r85_inbox_rules.py > r85_inbox_rules.out
