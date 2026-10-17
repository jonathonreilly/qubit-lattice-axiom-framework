#!/bin/zsh
# QMC-1b gates, sequential (one process at a time). PREREG section 4.
cd "$(dirname "$0")"
zsh capped.sh runs/gates_i_iia.out python3 validate_b.py
for f in f1 g1; do
  zsh capped.sh runs/gate3_$f.log python3 runner.py --kind reduced --dims 3 --filt $f --W 2 --beta 2 --dtau 0.05 --ns 4 \
     --warm 200 --sweeps 6000 --eqt_points 5 --kinetic --alternate --seed 3301 --out runs/gate3_$f.npz
done
zsh capped.sh runs/gate3_compare.out python3 gate3_compare.py f1 g1
echo "gates done $(date -u +%H:%MZ)" >> runs/gates_done.txt
