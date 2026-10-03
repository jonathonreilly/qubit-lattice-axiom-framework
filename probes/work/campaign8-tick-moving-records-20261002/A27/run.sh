#!/bin/zsh
# Run one A27 check script with the campaign caps: nice 10, single-threaded BLAS,
# a 55 s in-script alarm, and peak RSS reported by /usr/bin/time -l.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A27
for s in "$@"; do
  echo "=== $s ==="
  /usr/bin/time -l nice -n 10 python3 "$s" > "out_${s%.py}.txt" 2> "time_${s%.py}.txt"
  cat "out_${s%.py}.txt"
  grep -E "real|maximum resident" "time_${s%.py}.txt" | sed 's/^ *//'
done
