#!/bin/bash
# usage: run.sh script.py [args...] -> out_<tag>.txt, time_<tag>.txt ; nice 10, 1 thread, 58 s alarm, time + peak RSS
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
s="$1"; shift
tag="${s%.py}$(printf "_%s" "$@" | tr ",.:" "-pc")"
/usr/bin/time -l nice -n 10 perl -e 'alarm 58; exec @ARGV' python3 "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
rc=$?
echo "exit=$rc tag=${tag}"
grep -E "real|maximum resident" "time_${tag}.txt" | head -2
grep -v -E "real|user|sys|maximum|page|swaps|block|messages|signals|context|instructions|cycles|peak|average|involuntary|voluntary" "time_${tag}.txt" | head -5
