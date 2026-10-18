#!/bin/zsh
cd ${0:a:h}
for N in 32 48 64 96; do for D in 0.0 0.5; do for m in 0.1 0.05 0.025; do
  zsh capped.sh flav_N${N}_m${m}_D${D}.out python3 yuk_lv.py flav $N $m $D
done; done; done
for N in 24 32 48; do
  zsh capped.sh strain_N${N}_m0.1_D0.5.out python3 yuk_lv.py strain $N 0.1 0.5
done
zsh capped.sh strain_N32_m0.1_D0.0.out python3 yuk_lv.py strain 32 0.1 0.0
for N in 24 32; do
  zsh capped.sh offd_N${N}_m0.1_D0.5.out python3 yuk_lv.py offd $N 0.1 0.5
done
echo ALLDONE > run2.done
