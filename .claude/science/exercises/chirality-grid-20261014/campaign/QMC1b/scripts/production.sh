#!/bin/zsh
# QMC-1b production driver (PREREG section 5). One process at a time. Stop for new work at 22:35Z (STOP epoch).
cd "$(dirname "$0")"
STOP=$(date -j -u -f "%Y-%m-%d %H:%M" "2026-10-17 22:35" +%s)
log() { echo "$(date -u +%H:%MZ) $*" >> runs/production_driver.log; }
common=(--kind spin10 --beta 4 --dtau 0.05 --ns 8 --alternate --aux_every 4)
log "start"
for L in 4 6; do for f in fG f2; do
  zsh capped.sh runs/L${L}_${f}_W0.log python3 runner.py $common --dims $L $L --filt $f --W 0 --warm 0 --sweeps 1 --seed 1 --out runs/L${L}_${f}_W0.npz
done; done
log "W=0 references done"
for spec in "fG 4 41004" "f2 4 42004" "fG 2 41002" "f2 2 42002"; do
  set -- ${=spec}
  now=$(date +%s); tmax=$(( STOP - now - 200 ))
  (( tmax < 60 )) && { log "no time for L4 $1 W$2"; continue; }
  log "L4 $1 W$2 seed $3 tmax $tmax"
  zsh capped.sh runs/L4_$1_W$2.log python3 runner.py $common --dims 4 4 --filt $1 --W $2 --warm 20 --sweeps 200 --seed $3 --tmax $tmax --out runs/L4_$1_W$2.npz
  log "L4 $1 W$2 finished"
done
while true; do
  zsh capped.sh runs/queue.out python3 queue_b.py
  grep "^#" runs/queue.out >> runs/production_driver.log
  next=$(grep -v -E "^#|watchdog" runs/queue.out | head -1)
  [[ "$next" == "none" || -z "$next" ]] && { log "queue empty"; break; }
  set -- ${=next}
  now=$(date +%s); tmax=$(( STOP - now - 520 ))
  (( tmax < 600 )) && { log "stop: no time left for L6 $1 W$2"; break; }
  log "L6 $1 W$2 seed $3 tmax $tmax"
  zsh capped.sh runs/L6_$1_W$2.log python3 runner.py $common --dims 6 6 --filt $1 --W $2 --warm 10 --sweeps 200 --seed $3 --tmax $tmax --out runs/L6_$1_W$2.npz
  log "L6 $1 W$2 finished"
done
log "driver done"
