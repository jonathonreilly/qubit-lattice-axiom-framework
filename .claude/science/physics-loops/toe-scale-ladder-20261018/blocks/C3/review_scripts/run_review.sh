#!/bin/sh
# Re-runs the reviewer's independent checks (about 70 s single core, niced).
cd "$(dirname "$0")"
for s in r1_xor_linear_coding_radius r2_rate_dependent_forward_mc r3_stopping_set_exact_and_markov r4_clocks_bounds_witness; do
  nice -n 19 python3 $s.py > logs/${s%%_*}.log
done
cat logs/r1.log logs/r2.log logs/r3.log logs/r4.log | grep -v '^TOTAL' > logs/review_all.log
P=$(grep -c '^\[PASS\]' logs/review_all.log); F=$(grep -c '^\[FAIL\]' logs/review_all.log)
echo "TOTAL: PASS=$P FAIL=$F" >> logs/review_all.log
