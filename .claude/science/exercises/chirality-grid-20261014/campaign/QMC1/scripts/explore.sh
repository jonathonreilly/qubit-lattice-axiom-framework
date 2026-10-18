#!/bin/zsh
# exploratory locator at 2D L = 4 (short runs; PREREG section 5 locator purpose)
cd "$(dirname "$0")"
zsh capped.sh runs/explore_f2_W0.log python3 runner.py --dims 4 4 --filt f2 --W 0 --beta 4 --dtau 0.1 --warm 0 --sweeps 1 --out runs/explore_f2_W0.npz
for W in 0.25 1 4; do
zsh capped.sh runs/explore_f2_W$W.log python3 runner.py --dims 4 4 --filt f2 --W $W --beta 4 --dtau 0.1 --warm 10 --sweeps 12 --out runs/explore_f2_W$W.npz
done
for W in 1 4; do
zsh capped.sh runs/explore_one_W$W.log python3 runner.py --dims 4 4 --filt one --W $W --beta 4 --dtau 0.1 --warm 10 --sweeps 12 --out runs/explore_one_W$W.npz
done
