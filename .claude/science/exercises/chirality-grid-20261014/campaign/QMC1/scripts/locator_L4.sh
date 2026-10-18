#!/bin/zsh
# 2D L = 4 locator (PREREG section 5 + follow-up C). Sequential, one process at a time.
cd "$(dirname "$0")"
run() { zsh capped.sh runs/$1.log python3 runner.py --dims 4 4 --beta 4 --warm 20 --sweeps 60 --seed $2 --out runs/$1.npz ${@:3}; }
run L4_f2_W0.25 101 --filt f2 --W 0.25 --dtau 0.1 --ns 4
run L4_f2_W0.5  102 --filt f2 --W 0.5  --dtau 0.1 --ns 4
run L4_f2_W1    103 --filt f2 --W 1    --dtau 0.1 --ns 4
run L4_f2_W2    104 --filt f2 --W 2    --dtau 0.1 --ns 4
run L4_f2_W4    105 --filt f2 --W 4    --dtau 0.1 --ns 2
run L4_f2_W8    106 --filt f2 --W 8    --dtau 0.05 --ns 2
run L4_one_W0.05 111 --filt one --W 0.05 --dtau 0.1 --ns 4
run L4_one_W0.1  112 --filt one --W 0.1  --dtau 0.1 --ns 4
run L4_one_W0.25 113 --filt one --W 0.25 --dtau 0.1 --ns 4
run L4_one_W0.5  114 --filt one --W 0.5  --dtau 0.1 --ns 2
run L4_one_W1    115 --filt one --W 1    --dtau 0.1 --ns 2
