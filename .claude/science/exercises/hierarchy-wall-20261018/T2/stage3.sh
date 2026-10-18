#!/bin/zsh
# Stage 3 (added 18:59Z after seeing that omega is not separated from 0.2 with L<=48): more statistics at L=48, 64, same beta, new seeds
cd ${0:a:h}
until [[ -f data/stage2.done ]]; do sleep 2; done
B=0.5561
zsh scripts/capped.sh data/s3_L48.log ./lc wolff 48 $B 30000 300 3048 data/s3_L48.bin 3
zsh scripts/capped.sh data/s3_L64.log ./lc wolff 64 $B 15000 300 3064 data/s3_L64.bin 4
date -u > data/stage3.done
