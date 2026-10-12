#!/bin/bash
# shape scan: b1 b2 r c1 c2 ; two (N, m) points each (m = lam)
for sh in "1.0 2.0 1.0 1.0 2.0" "1.5 2.5 1.0 1.5 2.5" "2.0 3.0 1.0 2.0 3.0" "2.0 3.0 0.5 2.0 3.0" "0.5 1.5 1.0 0.5 1.5" \
          "2.0 3.0 1.0 0.5 1.0" "1.0 3.0 1.0 1.0 3.0" "2.5 3.1 1.0 2.5 3.1" "2.0 3.0 1.0 -1 -1" "-1 -1 1.0 -1 -1" "-1 -1 1.0 2.0 3.0"; do
  for nm in "224 0.05" "320 0.025"; do
    OMP_NUM_THREADS=2 python3 -I r85_box_qed.py box $sh ${nm% *} ${nm#* } ${nm#* } | grep b1
  done
done
