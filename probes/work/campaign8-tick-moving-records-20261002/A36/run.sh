#!/bin/zsh
# A36 run wrapper: nice 10, single-threaded BLAS, 55 s alarm inside each script,
# peak RSS from /usr/bin/time -l, and a load gate (skip if the 1-minute load is 6 or more).
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A36
for s in "$@"; do
  load=$(uptime | sed -E 's/.*load averages?: ([0-9.]+).*/\1/')
  ok=$(python3 -c "print(1 if float('$load') < 6 else 0)")
  if [[ "$ok" != "1" ]]; then
    echo "=== $s SKIPPED: 1-min load $load >= 6 ==="
    continue
  fi
  echo "=== $s (1-min load $load) ==="
  /usr/bin/time -l nice -n 10 python3 "$s" > "out_${s%.py}.txt" 2> "time_${s%.py}.txt"
  cat "out_${s%.py}.txt"
  grep -E "real|maximum resident" "time_${s%.py}.txt" | sed 's/^ *//'
  grep -iE "error|traceback" "time_${s%.py}.txt" | head -5
done
