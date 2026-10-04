#!/bin/zsh
# A54 small-job runner (no NUMLOCK; the heavy slot belongs to A51): load gate (1-min < 6), free memory >= 28%,
# nice 15, four BLAS caps at 1; each script must carry its own signal.alarm <= 120 s and stay under ~300 MB.
# Wall time and peak RSS from /usr/bin/time -l.  Usage: run_small.sh script.py [args...]
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
cd $SP/c8/A54
s=$1; shift; tag=${s%.py}${1:+_$1}${2:+_$2}
load=$(uptime | sed -E 's/.*load averages?: *([0-9.]+).*/\1/')
free=$(memory_pressure | tail -1 | sed -E 's/.*: *([0-9]+)%.*/\1/')
echo "=== $s $* (1-min load $load, free mem ${free}%) ==="
if (( $(echo "$load >= 6" | bc -l) )); then echo "SKIPPED: load $load >= 6"; exit 2; fi
if (( free < 28 )); then echo "SKIPPED: free memory ${free}% < 28%"; exit 2; fi
/usr/bin/time -l nice -n 15 python3 -u "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
cat "out_${tag}.txt"
grep -E "real|maximum resident" "time_${tag}.txt" | sed 's/^ *//'
grep -iE "error|traceback|alarm" "time_${tag}.txt" | head -5
