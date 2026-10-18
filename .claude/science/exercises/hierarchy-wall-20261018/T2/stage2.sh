#!/bin/zsh
# Stage 2: beta = 0.5561 (stage-1 crossings L <= 24); L=48 (MCRG 3 levels), L=64 (MCRG 4 levels); then M3 landed-kernel dynamics
cd ${0:a:h}
until [[ -f data/stage1.done ]]; do sleep 2; done
B=0.5561
zsh scripts/capped.sh data/s2_L48.log ./lc wolff 48 $B 15000 300 2048 data/s2_L48.bin 3
zsh scripts/capped.sh data/s2_L64.log ./lc wolff 64 $B 10000 300 2064 data/s2_L64.bin 4
for L in 8 12 16; do zsh scripts/capped.sh data/m3_L$L.log ./lc lc $L $B 400000 20000 30$L data/m3_L$L.bin; done
zsh scripts/capped.sh data/m3_L24.log ./lc lc 24 $B 200000 20000 3024 data/m3_L24.bin
date -u > data/stage2.done
