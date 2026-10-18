#!/bin/bash
# B23 runner chain (~15 min on 4 cores): every family chunk, the summary, the two cross-checks, then the aggregate.
# Usage: run_all.sh [--aggregate-only]
cd "$(dirname "$0")"
if [ "$1" != "--aggregate-only" ]; then
  for T in cliff2:0,1,2,3 cliff2:4,5,6,7 cliff2:8,9,10 pi6 taste_pi6; do
    L=screen_$(echo $T | tr ':,' '_-').log
    ( time python3 b23_screen.py $T 4 ) > $L 2>&1
  done
  python3 summarise.py > summary.log 2>&1
  python3 chk_defects.py > chk_defects.log 2>&1
  python3 chk_kstar_dirac.py > chk_kstar_dirac.log 2>&1
fi
grep -h "^RESULT" screen_*.log summary.log
P=$(grep -h "^TOTAL" screen_*.log summary.log chk_defects.log chk_kstar_dirac.log | sed -E 's/.*PASS=([0-9]+).*/\1/' | paste -sd+ | bc)
F=$(grep -h "^TOTAL" screen_*.log summary.log chk_defects.log chk_kstar_dirac.log | sed -E 's/.*FAIL=([0-9]+).*/\1/' | paste -sd+ | bc)
echo "TOTAL: PASS=$P FAIL=$F"
