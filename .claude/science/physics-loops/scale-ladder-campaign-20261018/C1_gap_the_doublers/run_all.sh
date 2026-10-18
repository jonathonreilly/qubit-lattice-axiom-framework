#!/bin/bash
# C1 runners: c1_reps.py (~50 s), c1_bdg_step.py N=32 (~105 s), c1_anomaly.py (~5 s). Prints per-runner logs and an aggregate TOTAL.
cd "$(dirname "$0")"
python3 c1_reps.py > c1_reps.log 2>&1
python3 c1_bdg_step.py 32 > c1_bdg_step.log 2>&1
python3 c1_anomaly.py > c1_anomaly.log 2>&1
P=0; F=0
for f in c1_reps.log c1_bdg_step.log c1_anomaly.log; do
  l=$(grep "TOTAL:" $f); echo "$f: $l"
  p=$(echo "$l" | sed -E 's/.*PASS=([0-9]+).*/\1/'); q=$(echo "$l" | sed -E 's/.*FAIL=([0-9]+).*/\1/')
  P=$((P+p)); F=$((F+q))
done
echo "TOTAL: PASS=$P FAIL=$F"
