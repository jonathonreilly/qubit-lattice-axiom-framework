#!/bin/bash
# B24 screens, sequential (4 cores each); each run <= 25 min
cd "$(dirname "$0")"
for tag in mix2:0,1,2,3 mix2:4,5,6 plane:0,1,2,3,4,5 plane:6,7,8,9,10,11; do
  f=screen_$(echo $tag | tr ':,' '_-').log
  timeout 1500 python3 b24_screen.py $tag 4 > $f 2>&1
done
