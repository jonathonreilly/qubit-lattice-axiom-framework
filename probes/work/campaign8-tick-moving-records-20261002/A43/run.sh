#!/bin/zsh
# A43 runner: load gate (<6), shared numeric lock, nice 10, four BLAS caps at 1,
# 28 s CPU limit, wall time and peak RSS from /usr/bin/time -l.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
cd $SP/c8/A43
for s in "$@"; do
  load=$(uptime | sed -E 's/.*load averages?: *([0-9.]+).*/\1/')
  echo "=== $s (1-min load $load) ==="
  if (( $(echo "$load >= 6" | bc -l) )); then echo "SKIPPED: load $load >= 6"; continue; fi
  if [[ -d $SP/c8/NUMLOCK ]]; then
    age=$(( $(date +%s) - $(stat -f %m $SP/c8/NUMLOCK) ))
    if (( age < 180 )); then echo "SKIPPED: lock held, age ${age}s"; continue; fi
    echo "stale lock (age ${age}s) removed"; rmdir $SP/c8/NUMLOCK
  fi
  mkdir $SP/c8/NUMLOCK || { echo "SKIPPED: lock race"; continue; }
  ( ulimit -t 28; /usr/bin/time -l nice -n 10 python3 -u "$s" > "out_${s%.py}.txt" 2> "time_${s%.py}.txt" )
  rmdir $SP/c8/NUMLOCK
  cat "out_${s%.py}.txt"
  grep -E "real|maximum resident" "time_${s%.py}.txt" | sed 's/^ *//'
  grep -iE "error|traceback" "time_${s%.py}.txt" | head -5
done
