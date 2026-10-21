#!/bin/sh
# Aggregates the TOTAL lines of the current (non-superseded) logs into logs/ALL_TOTALS.log
cd "$(dirname "$0")/../logs"
P=0; F=0
{
for f in s0_sign_lemmas.log s1_localization_controls.log s2_finite_range_battery.log s3_sheet_witness.log; do
  t=$(grep '^TOTAL:' $f | tail -1); echo "$f: $t"
  p=$(echo "$t" | sed 's/.*PASS=\([0-9]*\).*/\1/'); q=$(echo "$t" | sed 's/.*FAIL=\([0-9]*\).*/\1/')
  P=$((P+p)); F=$((F+q))
done
echo "TOTAL: PASS=$P FAIL=$F"
} > ALL_TOTALS.log
cat ALL_TOTALS.log
