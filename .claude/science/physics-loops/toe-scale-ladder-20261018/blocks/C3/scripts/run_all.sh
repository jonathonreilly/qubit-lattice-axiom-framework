#!/bin/sh
# Runs all C3 scripts and prints the aggregate TOTAL line.
D=$(dirname "$0")
P=0; Fl=0
for s in s1_iid_paths_and_coding_radius s2_rate_modulated s3_correlated_clocks_and_witness; do
  echo "=== $s ==="
  python3 "$D/$s.py" > "$D/../logs/$s.out" 2>&1
  cat "$D/../logs/$s.out"
  line=$(grep -E '^s[0-9]: PASS=' "$D/../logs/$s.out" | tail -1)
  p=$(echo "$line" | sed -E 's/.*PASS=([0-9]+).*/\1/'); f=$(echo "$line" | sed -E 's/.*FAIL=([0-9]+).*/\1/')
  [ -z "$p" ] && { p=0; f=1; }
  P=$((P+p)); Fl=$((Fl+f))
done
echo "TOTAL: PASS=$P FAIL=$Fl"
