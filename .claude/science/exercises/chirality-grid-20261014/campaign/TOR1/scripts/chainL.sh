#!/bin/zsh
cd "$(dirname "$0")"
P=pool_TOR1_srch_Lt4_k6_s3201.npz
zsh capped.sh L_cheap_28.out python3 tor1_kernel.py $P 4 2 8 mod,O,vec0,W,PG upper
zsh capped.sh L_cheap_212.out python3 tor1_kernel.py $P 4 2 12 mod,O,vec0,W,PG upper
zsh capped.sh L_chi_28.out python3 tor1_kernel.py $P 4 2 8 chi upper
zsh capped.sh L_chi_28_herm.out python3 tor1_kernel.py $P 4 2 8 chi rev:11:2
zsh capped.sh L_chi_212.out python3 tor1_kernel.py $P 4 2 12 chi upper
zsh capped.sh L_cheap_38sub.out python3 tor1_kernel.py $P 4 3 8 mod,O,vec0,W,PG sub:12:2
zsh capped.sh L_chi_38sub.out python3 tor1_kernel.py $P 4 3 8 chi sub:12:2
echo done > chainL.done
