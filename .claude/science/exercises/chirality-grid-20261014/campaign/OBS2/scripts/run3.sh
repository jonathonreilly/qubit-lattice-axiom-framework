#!/bin/zsh
cd ${0:a:h}
for N in 32 48 64 96; do for D in 0.0 0.5; do for m in 0.1 0.05 0.025; do
  zsh capped.sh flav_N${N}_m${m}_D${D}.out python3 yuk_lv.py flav $N $m $D
done; done; done
echo ALLDONE > run3.done
