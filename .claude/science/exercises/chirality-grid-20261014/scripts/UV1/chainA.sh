#!/bin/zsh
cd ${0:a:h}
./capped.sh A12h_d1_torus.out python3 uv1_d1.py pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz torus - hard:0
./capped.sh A12t_d1_torus.out python3 uv1_d1.py pool_K2c_wgsearch_tri_O_torus_Lt12_seed4412.npz torus - tri:0
./capped.sh A16h_d1_torus.out python3 uv1_d1.py pool_K2c_wgsearch_hard_O_torus_Lt16_seed4416.npz torus - hard:0
./capped.sh Bsel_d1_open.out python3 uv1_d1.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz open - hard:0
echo done > chainA.done
