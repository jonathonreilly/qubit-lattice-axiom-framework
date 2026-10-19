#!/bin/bash
# C1c thin dynamic queue wrapper around C1b's unchanged run_pt.py.
# usage: worker.sh WORKER_NAME [DEADLINE_HHMM_UTC]   (default deadline 1635: no chunk starts after it)
# Each pass: pick the incomplete job with the lowest (TIER, new_chunks_done) whose lock is free, run one
# 15-min chunk under flock, repeat. Restart-safe: run_pt.py resumes from data/ckpt/TAG.npz.
cd "$(dirname "$0")"
W=$1; DL=${2:-1635}
export NOLOOP_SWEEPS=2000
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMBA_NUM_THREADS=1
LK=/tmp/claude-0/c1c_raw/locks; mkdir -p $LK
LOG=../logs/queue_$W.log
while true; do
  now=$(date -u +%H%M); [ "$now" -ge "$DL" ] && { echo "$(date -u +%H:%M:%S) deadline reached, $W exits" >> $LOG; exit 0; }
  ran=0
  for line in $(grep -v '^#' jobs_C1c.txt | while read -r TAG L SEED START BETAS NCH THERM EVERY TIER BASE; do
        [ -z "$TAG" ] && continue
        n=$(ls ../data/raw/${TAG}_c*.npz 2>/dev/null | wc -l)
        [ "$n" -ge "$NCH" ] && continue
        echo "$TIER $((n-BASE)) $TAG|$L|$SEED|$START|$BETAS|$THERM|$EVERY"
      done | sort -n -k1,1 -k2,2 | awk '{print $3}'); do
    IFS='|' read -r TAG L SEED START BETAS THERM EVERY <<< "$line"
    flock -n -E 75 $LK/$TAG.lock bash -c "n=\$(ls ../data/raw/${TAG}_c*.npz 2>/dev/null | wc -l); echo \"\$(date -u +%H:%M:%S) $W start $TAG chunk \$n\" >> $LOG; nice -n 10 python3 run_pt.py $TAG $L $SEED $START $BETAS 15 $THERM $EVERY >> $LOG 2>&1"
    rc=$?
    [ $rc -eq 75 ] && continue
    ran=1; break
  done
  [ $ran -eq 0 ] && { echo "$(date -u +%H:%M:%S) $W: nothing to run, exits" >> $LOG; exit 0; }
done
