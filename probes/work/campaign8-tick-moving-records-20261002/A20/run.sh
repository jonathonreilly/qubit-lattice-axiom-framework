#!/bin/zsh
# usage: ./run.sh script.py [args]  -- 60 s alarm, nice 10, single-threaded BLAS; time stats -> .time_<script>
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
exec nice -n 10 /usr/bin/time -l -o ".time_${1%.py}" perl -e 'alarm 60; exec @ARGV' python3 "$@"
