#!/bin/zsh
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
cd "$(dirname "$0")"
/usr/bin/time -l python3 nt1_search.py 6 20 7401 11112 > T2_search_Lt12_7401.out 2> T2_search_Lt12_7401.err
/usr/bin/time -l python3 nt1_kernel.py pool_NT1_wsearch_11112_open_Lt12_seed7401_d0.6.npz 6 11112 > T2_kernel_Lt12_7401.out 2> T2_kernel_Lt12_7401.err
/usr/bin/time -l python3 nt1_kernel.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz 6 11112 > T1_Lt12_wsearch1401.out 2> T1_Lt12_wsearch1401.err
echo done > chainB.done
