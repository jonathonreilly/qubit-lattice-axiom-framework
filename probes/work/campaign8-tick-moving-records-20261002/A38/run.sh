#!/bin/zsh
# A38 runner: nice 10, all BLAS thread caps at 1, 55 s alarm inside each script,
# load gate (1-min load < 6), peak RSS from /usr/bin/time -l.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A38
for s in "$@"; do
  load=$(uptime | sed -E 's/.*load averages?: *([0-9.]+).*/\1/')
  echo "=== $s (1-min load $load) ==="
  if (( $(echo "$load >= 6" | bc -l) )); then echo "SKIPPED: load $load >= 6"; continue; fi
  /usr/bin/time -l nice -n 10 python3 "$s" > "out_${s%.py}.txt" 2> "time_${s%.py}.txt"
  cat "out_${s%.py}.txt"
  grep -E "real|maximum resident" "time_${s%.py}.txt" | sed 's/^ *//'
  grep -iE "error|Traceback" -A3 "time_${s%.py}.txt" | head -20
done
