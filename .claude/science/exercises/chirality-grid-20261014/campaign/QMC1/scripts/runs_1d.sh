#!/bin/zsh
# 1+1D runs (validation/NT-3 comparison only; no reading), then f2 L = 4 W = 16 (does the filtered S10 turn over at
# strong coupling like the control does at W ~ 1?), then the 1D control. Sequential.
cd "$(dirname "$0")"
run() { zsh capped.sh runs/$1.log python3 runner.py --beta 4 --warm 20 --sweeps 60 --seed $2 --out runs/$1.npz ${@:3}; }
run L1D8_f1_W1   201 --dims 8  --filt f1 --W 1 --dtau 0.1 --ns 4
run L1D16_f1_W1  202 --dims 16 --filt f1 --W 1 --dtau 0.1 --ns 4
run L1D8_f1_W4   203 --dims 8  --filt f1 --W 4 --dtau 0.1 --ns 2
run L1D16_f1_W4  204 --dims 16 --filt f1 --W 4 --dtau 0.1 --ns 2
run L4_f2_W16    107 --dims 4 4 --filt f2 --W 16 --dtau 0.025 --ns 4
run L1D8_one_W0.25  211 --dims 8  --filt one --W 0.25 --dtau 0.1 --ns 4
run L1D16_one_W0.25 212 --dims 16 --filt one --W 0.25 --dtau 0.1 --ns 4
# follow-up I: Trotter check of the key L4/L6 ratio at W = 2: L = 6 at dtau = 0.05 (n_s = 8, same 0.4 interval/memory)
zsh capped.sh runs/L6dt_f2_W2_dt0.05.log python3 runner.py --dims 6 6 --filt f2 --W 2 --beta 4 --dtau 0.05 --ns 8 --warm 10 --sweeps 30 --seed 405 --tmax 2100 --out runs/L6dt_f2_W2_dt0.05.npz
