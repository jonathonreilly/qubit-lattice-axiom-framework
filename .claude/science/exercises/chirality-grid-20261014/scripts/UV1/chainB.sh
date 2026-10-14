#!/bin/zsh
cd ${0:a:h}
for spec in "6 1" "6 2" "6 3" "8 1" "8 2" "8 3" "8 4" "10 1" "10 2" "10 3" "10 4"; do
  T=${spec% *}; t0=${spec#* }; Lt=$((2*T)); seed=$((7000+100*Lt+t0))
  ./capped.sh INF_torus_Lt${Lt}_t0${t0}.out python3 uv1_inf.py torus $T $t0 16 $seed
done
./capped.sh INF_open_Bsel.out python3 uv1_inf.py open pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz 12,16,17,19,9,10
echo done > chainB.done
./capped.sh Bsel_d2_open.out python3 uv1_d2.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz sel 12,16,17,19,9,10
echo done > chainB2.done
./capped.sh A12s8_search.out python3 uv1_search.py 6 16 8812 tri 8
./capped.sh A12s8_d1_torus.out python3 uv1_d1.py pool_UV1_search_tri_b8_torus_Lt12_seed8812.npz torus - tri:8
echo done > chainB3.done
