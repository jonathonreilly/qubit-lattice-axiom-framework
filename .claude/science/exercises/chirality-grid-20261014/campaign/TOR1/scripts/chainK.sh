#!/bin/zsh
cd "$(dirname "$0")"
P=pool_TOR1_Lt4_k6_s3101.npz
zsh capped.sh K_cheap_24.out python3 tor1_kernel.py $P 4 2 4 mod,O,vec0,W,PG upper
zsh capped.sh K_cheap_26.out python3 tor1_kernel.py $P 4 2 6 mod,O,vec0,W,PG upper
zsh capped.sh K_chi_24.out python3 tor1_kernel.py $P 4 2 4 chi upper
zsh capped.sh K_chi_24_herm.out python3 tor1_kernel.py $P 4 2 4 chi rev:11:2
zsh capped.sh K_chi_26.out python3 tor1_kernel.py $P 4 2 6 chi upper
zsh capped.sh K_cheap_34.out python3 tor1_kernel.py $P 4 3 4 mod,O,vec0,W,PG upper
zsh capped.sh K_chi_34.out python3 tor1_kernel.py $P 4 3 4 chi upper
zsh capped.sh K_mod_44sub.out python3 tor1_kernel.py $P 4 4 4 mod,O sub:12:2
echo done > chainK.done
