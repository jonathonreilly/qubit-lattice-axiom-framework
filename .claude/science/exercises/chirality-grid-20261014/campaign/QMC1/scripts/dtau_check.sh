#!/bin/zsh
# follow-up E: Trotter / Spin(10)-anisotropy check, f2 W = 2, L = 4, dtau = 0.05 (compare with L4_f2_W2 at dtau = 0.1)
cd "$(dirname "$0")"
zsh capped.sh runs/L4dt_f2_W2_dt0.05.log python3 runner.py --dims 4 4 --filt f2 --W 2 --beta 4 --dtau 0.05 --ns 4 --warm 20 --sweeps 60 --seed 404 --out runs/L4dt_f2_W2_dt0.05.npz
