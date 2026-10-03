#!/bin/zsh
# usage: run.sh script.py [args]  -> script.out (stdout), script.time (stderr + /usr/bin/time -l)
# nice 10, BLAS thread caps 1, hard 60 s alarm (SIGALRM kills the process).
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
name=${1%.py}
/usr/bin/time -l nice -n 10 python3 -c "import signal,runpy,sys; signal.alarm(60); sys.argv=sys.argv[1:]; runpy.run_path(sys.argv[0], run_name='__main__')" "$@" > $name.out 2> $name.time
echo "exit=$?"; grep -E " real|maximum resident" $name.time
