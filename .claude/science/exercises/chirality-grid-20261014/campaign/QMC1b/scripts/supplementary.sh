#!/bin/zsh
# QMC-1b supplementary runs (PREREG follow-up B). One process at a time; starts after production.sh is done.
cd "$(dirname "$0")"
STOP=$(date -j -u -f "%Y-%m-%d %H:%M" "2026-10-17 22:35" +%s)
log() { echo "$(date -u +%H:%MZ) SUPP $*" >> runs/production_driver.log; }
common=(--kind spin10 --beta 4 --dtau 0.05 --ns 8 --alternate --aux_every 4)
until grep -q "driver done" runs/production_driver.log; do sleep 30; done
log "start"
s1_window=0
for spec in "fG 8 41008 61008" "fG 16 41016 61016" "f2 8 42008 62008"; do
  set -- ${=spec}
  W=$2; s4=$3; s6=$4
  if [[ $1 == fG && $W == 16 && $s1_window == 1 ]]; then log "S1 had an L4 window: S3 (fG W16) not run"; continue; fi
  now=$(date +%s); tmax=$(( STOP - now - 200 ))
  (( tmax < 900 )) && { log "no time for L4 $1 W$W"; continue; }
  log "L4 $1 W$W seed $s4"
  zsh capped.sh runs/L4_$1_W$W.log python3 runner.py $common --dims 4 4 --filt $1 --W $W --warm 20 --sweeps 200 --seed $s4 --tmax $tmax --out runs/L4_$1_W$W.npz
  zsh capped.sh runs/e3w_tmp.out python3 e3w_of.py runs/L4_$1_W$W.npz
  line=$(grep -E '^-?[0-9.]+ [0-9]+$' runs/e3w_tmp.out | head -1)
  e3=${line%% *}; n=${line##* }
  log "L4 $1 W$W finished: E3w $e3 n $n"
  [[ -z "$line" ]] && { log "no E3w for L4 $1 W$W: no L6"; continue; }
  if (( e3 > 0.1 || n < 200 )); then log "L4 $1 W$W not a window or incomplete: no L6"; continue; fi
  [[ $1 == fG && $W == 8 ]] && s1_window=1
  now=$(date +%s); left=$(( STOP - now ))
  (( left < 8280 )) && { log "less than 2.3 h left: no L6 $1 W$W"; continue; }
  log "L6 $1 W$W seed $s6"
  zsh capped.sh runs/L6_$1_W$W.log python3 runner.py $common --dims 6 6 --filt $1 --W $W --warm 10 --sweeps 200 --seed $s6 --tmax $(( STOP - now - 520 )) --out runs/L6_$1_W$W.npz
  log "L6 $1 W$W finished"
done
log "done"
