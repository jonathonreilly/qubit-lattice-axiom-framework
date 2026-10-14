#!/bin/zsh
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
cd "$(dirname "$0")"
while pgrep -f "nt1_kernel.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401" > /dev/null; do sleep 3; done
/usr/bin/time -l python3 nt1_kernel.py pool_K2c_wgsearch_hard_O_open_Lt12_seed4401.npz 6 11112 > T1_Lt12_wgsearch4401.out 2> T1_Lt12_wgsearch4401.err
/usr/bin/time -l python3 nt1_d1p.py pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz 6 3 > D1p_Lt12.out 2> D1p_Lt12.err
/usr/bin/time -l python3 nt1_search.py 6 20 7401 11112 > T2_search_Lt12_7401.out 2> T2_search_Lt12_7401.err
/usr/bin/time -l python3 nt1_kernel.py pool_NT1_wsearch_11112_open_Lt12_seed7401_d0.6.npz 6 11112 > T2_kernel_Lt12_7401.out 2> T2_kernel_Lt12_7401.err
echo done > chainA.done
