#!/bin/zsh
for N in 48 96; do for m in 0.1 0.05 0.025; do for D in 0.0 0.5; do
  zsh capped.sh gk_N${N}_m${m}_D${D}.out python3 gen1_kernel.py $N $m $D G
done; done; done
echo done > run_kernel.done
