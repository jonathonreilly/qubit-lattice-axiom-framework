#!/bin/bash
# SU(2) 4D scan; parallel on 8 cores. Outputs data/su2_L{L}_b{beta}_{start}.json
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
jobs=()
for b in 0.25 0.5 0.75 1.0 1.25 1.5 1.75 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.8 3.0 3.5 4.0; do
  jobs+=("8 $b 150 500 3 $RANDOM data/su2_L8_b${b}_cold.json cold")
done
for b in 2.2 2.3 2.5; do jobs+=("8 $b 150 500 3 $RANDOM data/su2_L8_b${b}_hot.json hot"); done
for L in 4 6; do for b in 1.0 1.5 1.9 2.1 2.2 2.3 2.4 2.6 3.0; do jobs+=("$L $b 150 500 3 $RANDOM data/su2_L${L}_b${b}_cold.json cold"); done; done
printf '%s\n' "${jobs[@]}" | PY="$PY" xargs -P 8 -L 1 bash -c '"$PY" su2_mc.py $0 $1 $2 $3 $4 $5 $6 $7'
echo ALLDONE
