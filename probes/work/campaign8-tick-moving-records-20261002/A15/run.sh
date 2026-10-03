#!/bin/zsh
# usage: ./run.sh script.py [args]  -- thread caps 1, nice 10, reports wall time and peak RSS
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd "$(dirname "$0")"
/usr/bin/time -l nice -n 10 python3 "$@" 2> .time.$$ ; rc=$?
awk '/real/{printf "[wall %s s] ", $1} /maximum resident set size/{printf "[peak RSS %.0f MB]\n", $1/1048576}' .time.$$
grep -v -E "real|user|sys|resident|page|swaps|block|messages|signals|context|instructions|cycles|footprint|elapsed" .time.$$ | head -20
rm -f .time.$$
exit $rc
