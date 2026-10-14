#!/bin/zsh
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
cd "$(dirname "$0")"
while [ ! -f chainC.done ]; do sleep 3; done
/usr/bin/time -l python3 nt1_kernel.py pool_K2c_wsearch_hard_O_open_Lt20_seed1420.npz 10 11112 > T1_Lt20_wsearch1420.out 2> T1_Lt20_wsearch1420.err
echo done > chainD.done
