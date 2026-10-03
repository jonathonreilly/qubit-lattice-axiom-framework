#!/bin/zsh
# A33 runner (adapted from A31's run.sh): nice 10, all four BLAS thread caps at 1,
# a 55 s alarm inside each script, a load gate (1-min load < 6), peak RSS from /usr/bin/time -l.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A33
s="$1"; shift
load=$(uptime | sed -E 's/.*load averages?: *([0-9.]+).*/\1/')
echo "=== $s $* (1-min load $load) ==="
if (( $(echo "$load >= 6" | bc -l) )); then echo "SKIPPED: load $load >= 6"; exit 0; fi
tag="${s%.py}${1:+_$1}${2:+_$2}"
/usr/bin/time -l nice -n 10 python3 "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
cat "out_${tag}.txt"
grep -E "real|maximum resident" "time_${tag}.txt" | sed 's/^ *//'
grep -E "Error|Traceback|Alarm" "time_${tag}.txt" | head -5
