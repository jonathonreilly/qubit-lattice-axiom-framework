#!/usr/bin/env bash
# C3b runner: runs every script (niced), stores per-script output in logs/*.out, aggregates PASS/FAIL into logs/run_all.log.
# Total wall time ~ 15-20 min on one shared core.
set -u
cd "$(dirname "$0")"
LOG=../logs/run_all.log
: > "$LOG"
P=0; F=0
for s in s1_exact_checks s2_nucleation_growth s3_gaussian_clocks s3b_scale_of_theorem_H s4_two_stage; do
  echo "=== $s ===" | tee -a "$LOG"
  nice -n 10 python3 "$s.py" > "../logs/$s.out" 2>&1
  grep -E "^(PASS|FAIL)" "../logs/$s.out" | tee -a "$LOG"
  p=$(grep -c "^PASS" "../logs/$s.out"); f=$(grep -c "^FAIL" "../logs/$s.out")
  P=$((P+p)); F=$((F+f))
done
echo "TOTAL: PASS=$P FAIL=$F" | tee -a "$LOG"
