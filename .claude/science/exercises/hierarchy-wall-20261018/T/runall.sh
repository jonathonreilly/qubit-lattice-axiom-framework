#!/bin/zsh
cd ${0:a:h}
export NUMBA_NUM_THREADS=4
zsh scripts/capped.sh run_d2_b2.out python3 sim.py d2_b2.npz 2 128 2 256
zsh scripts/capped.sh run_d2_b3.out python3 sim.py d2_b3.npz 2 162 3 256
zsh scripts/capped.sh run_d3_b2.out python3 sim.py d3_b2.npz 3 32 2 192
zsh scripts/capped.sh run_d3_b3.out python3 sim.py d3_b3.npz 3 36 3 192
echo ALLDONE > runall.done
