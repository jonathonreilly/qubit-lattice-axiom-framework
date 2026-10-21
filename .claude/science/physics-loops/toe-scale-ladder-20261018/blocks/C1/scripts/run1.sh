#!/bin/bash
# run one production job line (args = L V T nsweep ntherm seed J dtau factor every); log to logs/queue_C.log
cd "$(dirname "$0")/.."
t0=$(date +%s)
out=$(nice -n 10 python3 scripts/prod.py "$@" 2>&1 | tail -c 600)
echo "[$(date -u +%H:%M:%S)] $* -> $(( $(date +%s)-t0 ))s :: $out" >> logs/queue_C.log
