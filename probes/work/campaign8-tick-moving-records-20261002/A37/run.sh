#!/bin/zsh
# Run one A37 check script with the campaign caps: nice 10, single-threaded BLAS,
# an in-script alarm (each script sets signal.alarm(55)), peak RSS from /usr/bin/time -l.
# Refuses to start if the 1-minute load average is 6 or more.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A37
for s in "$@"; do
  load1=$(sysctl -n vm.loadavg | awk '{print $2}')
  echo "=== $s (1-min load $load1) ==="
  if (( load1 >= 6.0 )); then
    echo "load too high, skipping $s"; continue
  fi
  /usr/bin/time -l nice -n 10 python3 "$s" > "out_${s%.py}.txt" 2> "time_${s%.py}.txt"
  cat "out_${s%.py}.txt"
  grep -E "real|maximum resident" "time_${s%.py}.txt" | sed 's/^ *//'
done
