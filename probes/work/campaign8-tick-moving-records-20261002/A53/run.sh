#!/bin/zsh
# A53 runner: load gate (1-min < 6), free memory >= 25%, shared NUMLOCK (stale after 600 s),
# nice 10, four BLAS caps at 1; each script carries its own signal.alarm cap (<= 290 s).
# Wall time and peak RSS from /usr/bin/time -l.  Usage: run.sh script.py [args...]
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
cd $SP/c8/A53
s=$1; shift; tag=${s%.py}${1:+_$1}${2:+_$2}
load=$(uptime | sed -E 's/.*load averages?: *([0-9.]+).*/\1/')
free=$(memory_pressure | tail -1 | sed -E 's/.*: *([0-9]+)%.*/\1/')
echo "=== $s $* (1-min load $load, free mem ${free}%) ==="
if (( $(echo "$load >= 6" | bc -l) )); then echo "SKIPPED: load $load >= 6"; exit 2; fi
if (( free < 25 )); then echo "SKIPPED: free memory ${free}% < 25%"; exit 2; fi
if [[ -d $SP/c8/NUMLOCK ]]; then
  age=$(( $(date +%s) - $(stat -f %m $SP/c8/NUMLOCK) ))
  if (( age < 600 )); then echo "SKIPPED: lock held, age ${age}s"; exit 3; fi
  echo "stale lock (age ${age}s) removed"; rmdir $SP/c8/NUMLOCK
fi
mkdir $SP/c8/NUMLOCK || { echo "SKIPPED: lock race"; exit 3; }
/usr/bin/time -l nice -n 10 python3 -u "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
rmdir $SP/c8/NUMLOCK
cat "out_${tag}.txt"
grep -E "real|maximum resident" "time_${tag}.txt" | sed 's/^ *//'
grep -iE "error|traceback|alarm" "time_${tag}.txt" | head -5
