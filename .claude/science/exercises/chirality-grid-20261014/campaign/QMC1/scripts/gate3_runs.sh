#!/bin/zsh
# gate (iii): reduced-flavour QMC at the ED point, two Trotter steps, sequential (one process at a time)
cd "$(dirname "$0")"
zsh capped.sh runs/gate3_dt005.log python3 runner.py --kind reduced --dims 3 --filt f1 --W 2 --beta 2 --dtau 0.05 --ns 4 --warm 200 --sweeps 12000 --eqt_points 5 --kinetic --seed 11 --out runs/gate3_dt005.npz
zsh capped.sh runs/gate3_dt010.log python3 runner.py --kind reduced --dims 3 --filt f1 --W 2 --beta 2 --dtau 0.1 --ns 4 --warm 200 --sweeps 12000 --eqt_points 5 --kinetic --seed 12 --out runs/gate3_dt010.npz
