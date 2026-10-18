#!/bin/zsh
# 2D L = 6 f2 runs (PREREG section 5 + follow-up D: W in {1, 2, 4}); free reference W = 0 (one exact sweep).
cd "$(dirname "$0")"
run() { zsh capped.sh runs/$1.log python3 runner.py --dims 6 6 --beta 4 --seed $2 --out runs/$1.npz ${@:3}; }
run L6_f2_W0   300 --filt f2 --W 0 --dtau 0.1 --ns 4 --warm 0 --sweeps 1
run L6_f2_W2   302 --filt f2 --W 2 --dtau 0.1 --ns 4 --warm 15 --sweeps 45
run L6_f2_W1   301 --filt f2 --W 1 --dtau 0.1 --ns 4 --warm 15 --sweeps 45
run L6_f2_W4   304 --filt f2 --W 4 --dtau 0.1 --ns 4 --warm 15 --sweeps 45
