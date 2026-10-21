#!/bin/bash
# Re-runs the fast reviewer checks; route A/B/gold data come from the checkpoints in logs/*.json
# (regenerate with run_queue.sh and run_queue2.sh). Writes logs/review_all.log ending with TOTAL.
cd "$(dirname "$0")"
nice -n 10 python3 r8_crosscheck_pointwise.py > logs/r8_crosscheck_pointwise.log 2>&1
nice -n 10 python3 r8_report.py > logs/r8_report.log 2>&1
{
for f in r8_symbolic r8_crosscheck_pointwise r8_report; do echo "$f: $(grep '^TOTAL' logs/$f.log)"; done
P=0; F=0
for f in r8_symbolic r8_crosscheck_pointwise r8_report; do
  l=$(grep '^TOTAL' logs/$f.log); p=$(echo $l | sed 's/.*PASS=\([0-9]*\).*/\1/'); q=$(echo $l | sed 's/.*FAIL=\([0-9]*\).*/\1/'); P=$((P+p)); F=$((F+q)); done
echo "TOTAL: PASS=$P FAIL=$F"
} > logs/review_all.log
cat logs/review_all.log
