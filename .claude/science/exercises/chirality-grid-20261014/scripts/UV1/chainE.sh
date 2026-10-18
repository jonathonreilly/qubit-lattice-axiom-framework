#!/bin/zsh
cd ${0:a:h}
until [ -f chainD.done ]; do sleep 3; done
./capped.sh VINF_Lt20_t04.out python3 uv1_inf_verify.py pool_UV1_inf_torus_Lt20_t04_seed9004.npz 12
./capped.sh VINF_Lt16_t03.out python3 uv1_inf_verify.py pool_UV1_inf_torus_Lt16_t03_seed8603.npz 12
echo done > chainE.done
