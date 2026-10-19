#!/usr/bin/env bash
# C3b reviewer runner (niced, one core). Writes logs/r*.log and logs/review_all.log. ~3 min total.
set -u
cd "$(dirname "$0")"
LOG=logs/review_all.log; : > "$LOG"; P=0; F=0
for s in r1_witness_and_K_exact r2_theorem_H r3_theorem_J_forward r4_kjma_dijkstra; do
  n=${s%%_*}; echo "=== $s ===" | tee -a "$LOG"
  timeout 1200 nice -n 10 python3 "$s.py" > "logs/$n.log" 2>&1
  grep -E "^(PASS|FAIL)" "logs/$n.log" | tee -a "$LOG"
  P=$((P+$(grep -c "^PASS" "logs/$n.log"))); F=$((F+$(grep -c "^FAIL" "logs/$n.log")))
done
echo "TOTAL: PASS=$P FAIL=$F" | tee -a "$LOG"
