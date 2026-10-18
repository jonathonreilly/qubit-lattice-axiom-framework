#!/bin/zsh
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
cd "$(dirname "$0")"
while [ ! -f chainB.done ]; do sleep 3; done
/usr/bin/time -l python3 nt1_phase.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz 6 > P1_phase_Lt12.out 2> P1_phase_Lt12.err
echo done > chainC.done
