#!/bin/zsh
# control f == 1 at L = 6 (follow-up F): W = 0.25 (onset: gap opens with S10 jump at L = 4) and W = 1 (strong coupling).
# n_s = 4 at L = 6 for memory (gate ii monitored).
cd "$(dirname "$0")"
run() { zsh capped.sh runs/$1.log python3 runner.py --dims 6 6 --beta 4 --seed $2 --out runs/$1.npz ${@:3}; }
run L6_one_W0.25 313 --filt one --W 0.25 --dtau 0.1 --ns 4 --warm 15 --sweeps 45
run L6_one_W1    315 --filt one --W 1    --dtau 0.1 --ns 4 --warm 15 --sweeps 45
