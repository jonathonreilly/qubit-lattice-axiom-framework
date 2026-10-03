#!/bin/bash
# usage: ./run.sh script.py [args]  -- thread caps 1, nice 10, 60 s alarm, prints wall time + peak RSS
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
/usr/bin/time -l nice -n 10 perl -e 'alarm 60; exec @ARGV' python3 "$@" 2> .time_err
status=$?
grep -E 'real|maximum resident' .time_err | sed -E 's/^ +//' | tr '\n' ' '; echo " exit=$status"
