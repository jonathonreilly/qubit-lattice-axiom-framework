#!/bin/zsh
# Stage 1: FSS at beta0 = 0.556 (from the coarse scan), MCRG ops on L=16 (2 levels), L=24 (2), L=32 (3)
cd ${0:a:h}
B=0.556
zsh scripts/capped.sh data/s1_L8.log  ./lc wolff 8  $B 100000 500 1008 data/s1_L8.bin 0
zsh scripts/capped.sh data/s1_L12.log ./lc wolff 12 $B 100000 500 1012 data/s1_L12.bin 0
zsh scripts/capped.sh data/s1_L16.log ./lc wolff 16 $B 100000 500 1016 data/s1_L16.bin 2
zsh scripts/capped.sh data/s1_L24.log ./lc wolff 24 $B 50000 500 1024 data/s1_L24.bin 2
zsh scripts/capped.sh data/s1_L32.log ./lc wolff 32 $B 30000 500 1032 data/s1_L32.bin 3
date -u > data/stage1.done
