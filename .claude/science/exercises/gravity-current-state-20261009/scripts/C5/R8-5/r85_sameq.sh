#!/bin/bash
for a in "224 0.05" "320 0.025" "448 0.0125"; do python3 -I r85_box_qed.py box 2.0 3.0 1.0 2.0 3.0 ${a% *} ${a#* } ${a#* } | grep b1; done
for sh in "1.0 3.0 1.0 1.0 3.0" "2.5 3.1 1.0 2.5 3.1" "-1 -1 1.0 -1 -1" "0.5 1.5 1.0 0.5 1.5"; do python3 -I r85_box_qed.py box $sh 320 0.025 0.025 | grep b1; done
