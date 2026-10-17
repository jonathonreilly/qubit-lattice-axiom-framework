#!/bin/zsh
cd "$(dirname "$0")"
P=pool_TOR1_srch_Lt4_k6_s3201.npz
zsh capped.sh HAAR_control.out python3 tor1_haar_control.py $P 4
zsh capped.sh L_chi_28_herm.out python3 tor1_kernel.py $P 4 2 8 chi rev:11:2
zsh capped.sh L_chi_212.out python3 tor1_kernel.py $P 4 2 12 chi upper
zsh capped.sh L_cheap_38sub.out python3 tor1_kernel.py $P 4 3 8 mod,O,vec0,W,PG sub:12:2
# dropped (F6): zsh capped.sh L_chi_38sub.out python3 tor1_kernel.py $P 4 3 8 chi sub:12:2
zsh capped.sh HESS_Lx4_Lt8_11112.out python3 tor1_hess.py 4 8 11112 2 7301
zsh capped.sh HESS_Lx4_Lt8_L1.out python3 tor1_hess.py 4 8 L1 1 7301
zsh capped.sh WARD_Lx4_Lt8.out python3 tor1_ward.py 4 8
echo done > chainM.done
