#!/bin/zsh
# after phase2: sector-factorisation check, f2 L = 6 W = 8 (strongest locator W; n_s = 8 at dtau = 0.05 keeps the
# stabilisation interval 0.4 and the memory of the other L = 6 runs), dtau check, control L = 6, 1D
cd "$(dirname "$0")"
zsh capped.sh check_sector.out python3 check_sector.py
zsh capped.sh runs/L6_f2_W8.log python3 runner.py --dims 6 6 --beta 4 --seed 308 --out runs/L6_f2_W8.npz --filt f2 --W 8 --dtau 0.05 --ns 8 --warm 15 --sweeps 45
zsh dtau_check.sh
[ -f control_L6.sh ] && zsh control_L6.sh
zsh runs_1d.sh
