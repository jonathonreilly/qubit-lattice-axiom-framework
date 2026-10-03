#!/bin/zsh
# Run ONE A37 script with arguments under the campaign caps: run1.sh <tag> <script.py> [args...]
# nice 10, all four BLAS thread caps = 1, in-script alarm (55 s), peak RSS from /usr/bin/time -l.
# Refuses to start if the 1-minute load average is 6 or more. Output: out_<tag>.txt, time_<tag>.txt.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A37
tag=$1; shift
load1=$(sysctl -n vm.loadavg | awk '{print $2}')
echo "=== $tag: $@ (1-min load $load1) ==="
if (( load1 >= 6.0 )); then
  echo "load too high, skipping"; exit 0
fi
/usr/bin/time -l nice -n 10 python3 "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
cat "out_${tag}.txt"
grep -E "real|maximum resident|Error|error" "time_${tag}.txt" | sed 's/^ *//'
