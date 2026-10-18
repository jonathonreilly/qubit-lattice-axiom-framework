#!/bin/zsh
cd ${0:a:h}
./capped.sh Bsel_d2_open.out python3 uv1_d2.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz sel 12,16,17,19,9,10
echo done > chainC1.done
./capped.sh A12s8_search.out python3 uv1_search.py 6 16 8812 tri 8
./capped.sh A12s8_d1_torus.out python3 uv1_d1.py pool_UV1_search_tri_b8_torus_Lt12_seed8812.npz torus - tri:8
echo done > chainC2.done
