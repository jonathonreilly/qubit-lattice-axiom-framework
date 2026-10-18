#!/bin/zsh
for N in 48 96; do for m in 0.1 0.05 0.025; do for D in 0.0 0.5; do
  zsh capped.sh r2_kin_N${N}_m${m}_D${D}.out python3 yuk_lv3.py kin $N $m $D
done; done; done
echo done > run_r2.done
