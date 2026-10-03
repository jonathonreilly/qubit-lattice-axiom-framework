#!/bin/zsh
# Run one A30 check script with the campaign caps: nice 10, single-threaded BLAS,
# a 55 s in-script alarm (each script sets signal.alarm), peak RSS from /usr/bin/time -l.
# Refuses to run if the 1-minute load average is 6 or more.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A30
load1=$(sysctl -n vm.loadavg | awk '{print $2}')
echo "load1=$load1"
if (( $(echo "$load1 >= 6" | bc -l) )); then
  echo "LOAD TOO HIGH ($load1), not running"; exit 3
fi
s="$1"; shift
tag="${s%.py}"
if [ $# -gt 0 ]; then tag="${tag}_$(echo "$@" | tr ' ' '_')"; fi
echo "=== $s $@ ==="
/usr/bin/time -l nice -n 10 python3 "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
cat "out_${tag}.txt"
grep -E "real|maximum resident" "time_${tag}.txt" | sed 's/^ *//'
grep -v -E "real|user|sys|maximum resident|average|page|block|signal|swap|voluntary|involuntary|messages|instructions|cycles|peak memory|footprint" "time_${tag}.txt" | head -5
