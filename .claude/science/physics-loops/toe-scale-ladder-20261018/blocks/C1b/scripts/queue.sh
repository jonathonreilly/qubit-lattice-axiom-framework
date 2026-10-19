#!/bin/bash
# usage: queue.sh JOBFILE QUEUENAME
# JOBFILE lines: TAG L SEED START BETAS NCHUNKS [THERM] [EVERY]
# runs each job's chunks (15 min each) until data/raw/TAG_c*.npz count >= NCHUNKS; safe to restart anytime.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMBA_NUM_THREADS=1
while read -r TAG L SEED START BETAS NCH THERM EVERY; do
  [ -z "$TAG" ] && continue
  [[ "$TAG" == \#* ]] && continue
  while true; do
    n=$(ls ../data/raw/${TAG}_c*.npz 2>/dev/null | wc -l)
    [ "$n" -ge "$NCH" ] && break
    echo "$(date -u +%H:%M:%S) start $TAG chunk $n" >> ../logs/queue_$2.log
    nice -n 10 python3 run_pt.py $TAG $L $SEED $START $BETAS 15 ${THERM:-1000} ${EVERY:-1} >> ../logs/queue_$2.log 2>&1
  done
done < "$1"
echo "$(date -u +%H:%M:%S) queue $2 done" >> ../logs/queue_$2.log
