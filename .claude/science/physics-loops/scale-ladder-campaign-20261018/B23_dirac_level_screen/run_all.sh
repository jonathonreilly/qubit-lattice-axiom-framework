#!/bin/bash
# B23 runner chain: every family chunk, then the summary.  Logs: screen_<tag>.log
cd "$(dirname "$0")"
for T in cliff2:0,1,2,3 cliff2:4,5,6,7 cliff2:8,9,10 pi6 taste_pi6; do
  L=screen_$(echo $T | tr ':,' '_-').log
  ( time python3 b23_screen.py $T 4 ) > $L 2>&1
done
