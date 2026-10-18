#!/bin/zsh
# QMC-1b follow-up D: W = 8 supplementary reruns with n_s = 4. One process at a time.
cd "$(dirname "$0")"
STOP=$(date -j -u -f "%Y-%m-%d %H:%M" "2026-10-17 22:35" +%s)
log() { echo "$(date -u +%H:%MZ) SUPP-D $*" >> runs/production_driver.log; }
common=(--kind spin10 --beta 4 --dtau 0.05 --ns 4 --alternate --aux_every 4 --W 8 --sweeps 200)
for spec in "4 fG 41108 20" "4 f2 42108 20" "6 fG 61108 10" "6 f2 62108 10"; do
  set -- ${=spec}
  now=$(date +%s); tmax=$(( STOP - now - 520 ))
  (( tmax < 300 )) && { log "no time for L$1 $2"; continue; }
  log "L$1 $2 W8 ns4 seed $3 tmax $tmax"
  zsh capped.sh runs/L$1_$2_W8ns4.log python3 runner.py $common --dims $1 $1 --filt $2 --warm $4 --seed $3 --tmax $tmax --out runs/L$1_$2_W8ns4.npz
  log "L$1 $2 W8 ns4 finished"
done
log "done"
