#!/bin/bash
# usage: run.sh script.py [args...]  -> writes out_<script>.txt ; nice 10, 1 thread, 60 s alarm, time + peak RSS
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
s="$1"; shift
tag="${s%.py}$(printf "_%s" "$@" | tr ",." "-p")"
/usr/bin/time -l nice -n 10 perl -e 'alarm 60; exec @ARGV' python3 "$s" "$@" > "out_${tag}.txt" 2> "time_${tag}.txt"
rc=$?
echo "exit=$rc"
grep -E "real|maximum resident" "time_${tag}.txt" | head -2
